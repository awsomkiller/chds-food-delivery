<!-- AddItem.vue -->
<script>
import { useMenuStore } from "@/stores/menu";
import { useTranslationStore } from "@/stores/translation";
import { storeToRefs } from "pinia";
import { useCartStore } from "@/stores/cart";
import { computed, onMounted } from "vue";

export default {
  setup() {
    const menuStore = useMenuStore();
    const cartStore = useCartStore();
    const translationStore = useTranslationStore();

    const { selectedItem } = storeToRefs(menuStore);
    const { active } = storeToRefs(cartStore);

    const t = (label, modules) => {
      return translationStore.translate(label, modules);
    };

    onMounted(() => {
      cartStore.resetActive();
    });

    const getItemImage = (item) => {
      if (!item || !item.item_images) return "";
      const mainImage = item.item_images.find((img) => img.is_main);
      const path = mainImage ? mainImage.image : "";
      return "https://api.chds.com.au" + path;
    };

    const selectPortion = (portion) => {
      cartStore.resetActive()
      cartStore.updateActivePortion(portion);
    };

    const toggleAddon = (addon) => {
      const index = cartStore.active.addons.findIndex((a) => a.id === addon.id);
      if (index > -1) {
        cartStore.active.addons.splice(index, 1);
      } else {
        cartStore.active.addons.push(addon);
      }
      cartStore.updateActiveAddons();
    };

    const incrementQuantity = () => {
      cartStore.updateActiveQuantity(cartStore.active.quantity + 1);
    };

    const decrementQuantity = () => {
      cartStore.updateActiveQuantity(cartStore.active.quantity - 1);
    };

    const addToCart = () => {
      if (!cartStore.active.selected_meal_portion_id) {
        alert("Please select a meal portion before adding to cart.");
        return;
      }
      cartStore.addToCart(selectedItem.value);
      cartStore.resetActive();
    };

    const currentPortion = computed(() => {
      if (
        !selectedItem.value ||
        cartStore.active.selected_meal_portion_id == null
      ) {
        return null;
      }
      return selectedItem.value.portion.find(
        (portion) => portion.id == cartStore.active.selected_meal_portion_id
      );
    });

    const isAddonSelected = (addon) => {
      return cartStore.active.addons.some((a) => a.id === addon.id);
    };

    return {
      t,
      active,
      selectedItem,
      getItemImage,
      selectPortion,
      toggleAddon,
      incrementQuantity,
      decrementQuantity,
      addToCart,
      cartStore,
      currentPortion,
      isAddonSelected,
    };
  },
};
</script>

<template>
  <!-- item detail popup -->
  <div
    class="modal modal-food-item fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div
      class="modal-dialog modal-dialog-scrollable modal-dialog-centered"
      v-if="selectedItem"
    >
      <div class="modal-content">
        <div class="modal-body">
          <div class="item-img mb-3">
            <button
              type="button"
              class="btn-close btn-close-modal"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
            <img class="mb-3" :src="getItemImage(selectedItem)" />

            <div>
              <h5>{{ t(selectedItem.trans_code, ["menu_item"]) }}</h5>
              <p>
                {{ t(selectedItem.trans_desc_code, ["menu_item"]) }}
              </p>

              <div class="price-text">
                <span class="fw-bold" v-if="active.selected_meal_portion_id">A$ {{ active.selected_meal_addon_price + active.selected_meal_portion_price }}</span>
                <span class="fw-bold" v-else>{{ selectedItem.price }}</span>
              </div>
              <div class="d-flex justify-content-start">
                <span
                  class="badge badge-success me-2"
                  style="background-color: #576d27"
                  v-for="tag in selectedItem.tags"
                  :key="tag.id"
                  >{{ tag.name }}</span
                >
              </div>
            </div>
          </div>

          <div class="px-3 py-2">
            <h4 class="extra-status">
              Meal Size:
            </h4>
            <div class="meal-category rounded p-3">
              <div v-for="portion in selectedItem.portion" :key="portion.id">
                <input
                  type="radio"
                  class="btn-check"
                  name="options"
                  :id="'portion-' + portion.id"
                  :value="portion.id"
                  v-model.number="cartStore.active.selected_meal_portion_id"
                  @change="selectPortion(portion)"
                />
                <label class="btn btn-primary" :for="'portion-' + portion.id"
                  >{{ portion.portion_name }} {{
                    portion.portion_weight !== '0' ? `(${portion.portion_weight}g)`: ``
                  }}</label
                >
              </div>
            </div>
          </div>

          <!-- Addons -->
          <div
            v-if="currentPortion && currentPortion.addons.length"
            class="px-3 py-2"
          >
            <h4 class="extra-status">
              Extra Add-ons 
            </h4>
            <div class="meal-addons rounded">
              <!-- Dynamically loop through the addons -->
              <div v-for="addon in currentPortion.addons" :key="addon.id">
                <input
                  type="checkbox"
                  class="btn-check"
                  :id="'addon-' + addon.id"
                  :checked="isAddonSelected(addon)"
                  @change="toggleAddon(addon)"
                />
                <label class="btn btn-primary w-100" :for="'addon-' + addon.id">
                  <p class="mb-0">Extra {{ addon.name }}</p>
                  <p class="mb-0"><b>+</b>A$ {{ addon.price }}</p>
                </label>
              </div>
            </div>
          </div>


          <!-- nutritions facts -->
          <div class="px-3 py-2 pt-4">
            <h4 class="nutrients-facts text-center" v-if="active.isMealSet">
              Nutrition Facts – Per Meal Set (150g Dish + 150g Vegetables + 150g Rice)
            </h4>
            <h4 class="nutrients-facts text-center" v-else>
              Nutrition Facts - Per 100g Of Main Dish
            </h4>
            <div class="meal-category-table rounded">
              <table class="table w-100">
                <thead>
                  <tr>
                    <th scope="col">Protein</th>
                    <th scope="col">Carb</th>
                    <th scope="col">Fat</th>
                    <th scope="col">Calories</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-if="active.selected_meal_portion_id">
                    <td>{{ active.selected_meal_portion_protein }} g</td>
                    <td>{{ active.selected_meal_portion_carbs }} g</td>
                    <td>{{ active.selected_meal_portion_fat }} g</td>
                    <td>{{ active.selected_meal_portion_calories }} Kcal</td>
                  </tr>
                  <tr v-else>
                    <td>{{ selectedItem.protein }} g</td>
                    <td>{{ selectedItem.carbs }} g</td>
                    <td>{{ selectedItem.fats }} g</td>
                    <td>{{ selectedItem.calories }} Kcal</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div
            class="px-3 py-2 pb-4 bg-white d-flex justify-content-between align-items-center"
          >
            <div class="item-action item-ippopup-action">
              <a
                href="javascript:void(0)"
                class="subtract"
                @click.prevent="decrementQuantity"
              >
                <i class="fa-solid fa-minus"></i>
              </a>
              <p>{{ cartStore.active.quantity }}</p>
              <a
                href="javascript:void(0)"
                class="add"
                @click.prevent="incrementQuantity"
              >
                <i class="fa-solid fa-plus"></i>
              </a>
            </div>
            <button
              type="button"
              class="btn btn-primary"
              @click="addToCart"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              {{ t("add_to_cart", ["ordernow"]) }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
