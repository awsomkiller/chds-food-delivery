<!-- AddItem.vue -->
<script>
import { useMenuStore } from '@/stores/menu';
import { storeToRefs } from 'pinia';
import { useCartStore } from '@/stores/cart';
import { computed, onMounted } from 'vue';
import { Modal } from 'bootstrap';

export default {
    setup() {
        const menuStore = useMenuStore();
        const cartStore = useCartStore();
        const { selectedItem } = storeToRefs(menuStore);

        onMounted(() => {
            cartStore.resetActive();
        });

        const getItemImage = (item) => {
            if (!item || !item.item_images) return "";
            const mainImage = item.item_images.find((img) => img.is_main);
            const path = mainImage ? mainImage.image : "";
            return "http://localhost:8000" + path;
        };

        const selectPortion = (portion) => {
            cartStore.updateActivePortion(portion);
        };

        const toggleAddon = (addon) => {
            const index = cartStore.active.addons.findIndex(a => a.id === addon.id);
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
                alert('Please select a meal portion before adding to cart.');
                return;
            }
            cartStore.addToCart(selectedItem.value);
            cartStore.resetActive();
            const modalElement = document.getElementById('exampleModal');
            if (modalElement) {
                const modalInstance = Modal.getInstance(modalElement);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        };

        const currentPortion = computed(() => {
            if (!selectedItem.value || cartStore.active.selected_meal_portion_id == null) {
                return null;
            }
            return selectedItem.value.portion.find(portion => portion.id == cartStore.active.selected_meal_portion_id);
        });

        const isAddonSelected = (addon) => {
            return cartStore.active.addons.some(a => a.id === addon.id);
        };

        return {
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
    <div class="modal modal-food-item fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered" v-if="selectedItem">
        <div class="modal-content">
         
          <div class="modal-body">
            <div class="item-img mb-3">
                <button type="button" class="btn-close btn-close-modal" data-bs-dismiss="modal" aria-label="Close"></button>
                <img class="mb-3" :src="getItemImage(selectedItem)">
                
                <div>
                    <h5> {{ selectedItem.name }}</h5>
                    <p>
                        {{ selectedItem.description }}
                    </p>

                    <div class="price-text"> <span class="fw-bold">{{ selectedItem.price }}</span> </div>
                    <div class="d-flex justify-content-start">
                        <span class="badge badge-success me-2" style="background-color: #576d27;" v-for="tag in selectedItem.tags" :key="tag.id">{{ tag.name }}</span>
                    </div>
                </div>
            </div>
            
            <div class="px-3 py-2">
                <h4 class="extra-status"> Meal Size : <span  class="text-status"> Meal Set </span> </h4>
                <div class="meal-category rounded p-3">
                    <div v-for="portion in selectedItem.portion" :key="portion.id">
                        <input type="radio" class="btn-check" name="options" :id="'portion-'+portion.id" :value="portion.id" v-model.number="cartStore.active.selected_meal_portion_id" @change="selectPortion(portion)">
                        <label class="btn btn-primary" :for="'portion-'+portion.id">{{ portion.portion_name }} ({{ portion.portion_weight }}g)</label>
                    </div>
                </div>
            </div>

            <!-- Addons -->
            <div v-if="currentPortion && currentPortion.addons.length" class="px-3 py-2 extra-options">
                <div class="meal-category toggle-button-extra rounded p-3" v-for="addon in currentPortion.addons" :key="addon.id">
                    <h4 class="extra-status"> {{ addon.name }} </h4>
                    <div class="">
                        <div class="can-toggle">
                            <input :id="'addon-'+addon.id" type="checkbox" :checked="isAddonSelected(addon)" @change="toggleAddon(addon)">
                            <label :for="'addon-'+addon.id">
                                <div class="can-toggle__switch" data-checked="Yes" data-unchecked="No"></div>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="px-3 py-2 pt-4">
                <h4 class="nutrients-facts"> Nutrition Facts – Per Meal Set
                    (150g Dish + 150g Vegetables + 150g Rice) </h4>
                <div class="meal-category-table rounded ">
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
                        <tr>
                            <td >{{ selectedItem.protein}} g</td>
                            <td>{{ selectedItem.carbs}} g</td>
                            <td>{{ selectedItem.fats}} g</td>
                            <td>{{ selectedItem.calories}} Kcal</td>
                        </tr>
                    </tbody>
                    </table>
                </div>
            </div>
            <div class="px-3 py-2 pb-4 bg-white d-flex justify-content-between align-items-center">
                <div class="item-action item-ippopup-action">
                    <a href="javascript:void(0)" class="subtract" @click.prevent="decrementQuantity">
                        <i class="fa-solid fa-minus"></i>
                    </a>
                    <p>{{ cartStore.active.quantity }}</p>
                    <a href="javascript:void(0)" class="add" @click.prevent="incrementQuantity">
                        <i class="fa-solid fa-plus"></i>
                    </a>
                </div>
                <button type="button" class="btn btn-primary" @click="addToCart">Add to Cart</button>
            </div>

          </div>
        </div>
      </div>
    </div>
</template>
