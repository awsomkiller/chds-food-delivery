<script>
import CartData from "@/components/CartData.vue";
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useMenuStore } from "@/stores/menu";
import { useCartStore } from "@/stores/cart";
import { useAuthStore } from "@/stores/auth";

import { storeToRefs } from "pinia";

export default {
  components: {
    CartData,
  },
  setup() {
    const menuStore = useMenuStore();
    const cartStore = useCartStore();
    const authStore = useAuthStore();
    
    const {
      items,
      cart,
      selectedItem,
      selectedCategory,
      cartItemCount,
      loading,
      isAllItemsLoaded,
      categories,
      categoriesLoading,
      categoriesError,
    } = storeToRefs(menuStore);

    const {
        totalQty
    } = storeToRefs(cartStore)
    const searchQuery = ref("");
    const quantity = ref(1);

    const performSearch = () => {
        console.log(searchQuery.value)
      menuStore.searchItems(searchQuery.value);
    };

    const getItemImage = (item) => {
      if (!item || !item.item_images) return "";
      const mainImage = item.item_images.find((img) => img.is_main);
      const path = mainImage ? mainImage.image : "";
      return "https://api.chds.com.au" + path;
    };

    const incrementCartItem = (item) => {
      menuStore.updateCartItemQuantity(item, item.quantity + 1);
    };

    const decrementCartItem = (item) => {
      if (item.quantity > 1) {
        menuStore.updateCartItemQuantity(item, item.quantity - 1);
      } else {
        menuStore.removeFromCart(item);
      }
    };

    const openItemModal = (item) => {
      menuStore.updateSelectedItem(item);
    };

    const incrementQuantity = () => {
      quantity.value += 1;
    };

    const decrementQuantity = () => {
      if (quantity.value > 1) {
        quantity.value -= 1;
      }
    };

    const addItemToCart = () => {
      if (selectedItem.value) {
        menuStore.addToCart(selectedItem.value, quantity.value);
        quantity.value = 1;
        menuStore.updateSelectedItem(null);
      }
    };

    // Infinite Scroll Logic
    const handleScroll = () => {
      const bottomOfWindow =
        window.innerHeight + window.scrollY >= document.body.offsetHeight - 2;
      if (bottomOfWindow && !isAllItemsLoaded.value && !loading.value) {
        menuStore.loadItems();
      }
    };

    // Method to truncate description
    const truncateDescription = (text, maxLength=60) => {
      if (!text) return "";
      return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
    };

    const handleCategoryChange = (category) =>{
        menuStore.selectCategory(category);
    }

    onMounted(() => {
      menuStore.resetItems();
      menuStore.loadCategories();
      menuStore.loadItems();
      authStore.fetchUserDetails();
      window.addEventListener("scroll", handleScroll);

      const modalElement = document.getElementById("exampleModal");
      if (modalElement) {
        modalElement.addEventListener("hidden.bs.modal", () => {
          openItemModal(null);
        });
      }
    });

    onBeforeUnmount(() => {
      window.removeEventListener("scroll", handleScroll);
    });

    return {
      items,
      selectedItem,
      cart,
      totalQty,
      searchQuery,
      performSearch,
      getItemImage,
      addToCart: menuStore.addToCart,
      incrementCartItem,
      decrementCartItem,
      cartItemCount,
      loading,
      isAllItemsLoaded,
      openItemModal,
      quantity,
      incrementQuantity,
      decrementQuantity,
      addItemToCart,
      truncateDescription,
      categories,
      categoriesLoading,
      categoriesError,
      CartData,
      selectedCategory,
      handleCategoryChange,
    };
  },
};
</script>


<template>
    <div class="container-xxl">
      <div class="row">
        <!-- Menu Items -->
        <div
          class="col-xxl-10 col-xl-9 col-lg-8 col-md-12 col-sm-12 col-12 p-3"
        >
          <div class="menu-items">
            <div class="row">
              <div class="col-lg-8 col-md-6 col-sm-12 col-12 p-2 pt-0">
                <div class="outlet-card p-2">
                  <input
                    class="form-control"
                    type="search"
                    placeholder="Search Dish"
                    aria-label="Search"
                    v-model="searchQuery"
                    @keyup.enter="performSearch"
                  />
                </div>
              </div>
              <!-- Category Dropdown -->
                <div class="col-lg-4 col-md-6 col-sm-12 col-12 p-2 pt-0">
                    <div class="search-filter h-100 p-2">
                        <div class="">
                            <div class="col-12">
                                <select
                                    id="inputState"
                                    class="form-select"
                                    v-model="selectedCategory"
                                    @change="handleCategoryChange(selectedCategory)"
                                    >
                                    <option value="">All CHDS Food</option>
                                    
                                    <option v-if="categoriesLoading" disabled>Loading categories...</option>
                                    <option v-else-if="categoriesError" disabled>Error loading categories</option>
                                    
                                    <option
                                        v-for="category in categories"
                                        :key="category.id"
                                        :value="category.id"
                                    >
                                        {{ category.name }}
                                    </option>
                                </select>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
  
            <!-- Items List -->
            <div class="row p-0">
              <div
                class="col-xxl-4 col-xl-6 col-md-6 col-sm-12 col-12 p-2"
                v-for="item in items"
                :key="item.id"
              >
                <div
                  class="card-item"
                  type="button"
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModal"
                  @click="openItemModal(item)"
                >
                  <div class="card-item-food p-3">
                    <div class="food-item-detail">
                      <h5>{{ item.name }}</h5>
                      <p class="item-price">{{ item.price }}</p>
                      <p class="item-description">{{ truncateDescription(item.description) }}</p>
                    </div>
                    <div class="food-image-n-add-item">
                      <div class="position-relative">
                        <img class="" :src="getItemImage(item)" />
                        <a href="" class="add-item-action" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="openItemModal(item)">Add +</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
  
              <!-- Loading Indicator -->
              <div v-if="loading" class="loading-indicator">
                Loading more items...
              </div>
              <div v-if="isAllItemsLoaded" class="end-of-items">
                All items loaded.
              </div>
            </div>
          </div>
        </div>
  
        <!-- Cart -->
        <div class="col-xxl-2 col-xl-3 col-lg-4 col-md-12 col-sm-12 col-12 p-2 cart-desktop"        >
          <CartData />
        </div>
      </div>
    </div>

<!-- cart-button-mobile -->
<div class="mobile-cart">
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample">
        <div class="view-cart-mobile">
            <p class="mb-0"> {{ totalQty }} Items</p>
            <p class="mb-0"> View Cart </p>
        </div>
    </button>
</div>

<!-- item cart mobile popup -->

<div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
    <div class="offcanvas-header">
        <!-- <h5 class="offcanvas-title" id="offcanvasExampleLabel">Your Cart</h5> -->
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
        <CartData />
    </div>
</div>
</template>

<style>
:root {
    --body-color: #f1f0f5;
    --divider-color: #e4e4e4;
    --card-heading-color: #333333;
    --card-location-color: #787878;

    --darkest-green-bg-color: #576d27;
    --order-background-color: #76923b;
    --light-green-color: #b3c677;
    --dark-brown-color: #944c22;
    --light-brown-colo: #c5886b;
    --lightest-brown-colo: #f7d9ba;

}

.outlet-card {
    background-color: white;
    border-radius: 0.5rem;
    display: flex;
    gap: 10px;
}

.search-filter {
    background-color: white;
    border-radius: 0.5rem;
    vertical-align: middle;
}

.restaurent-img {
    border: 1px solid var(--divider-color);
    border-radius: 4px;

}

.restaurent-img img {
    width: 66px;
    height: 66px;
    object-fit: cover;
}

.outlet-detail h5 {
    font-size: 17px;
    margin-bottom: 0;
    color: var(--card-heading-color);
}

.outlet-detail p {
    font-size: 15px;
    margin-bottom: 0;
    color: var(--card-location-color);
}

.divider-heading {
    border-top: 1px solid var(--divider-color);
    width: 100%;
    height: 5px;
    margin-top: 2.5rem;
    margin-bottom: 2.5rem;
    position: relative;
}

.divider-heading h3 {
    position: absolute;
    text-transform: uppercase;
    top: -0.75rem;
    left: 50%;
    right: 0;
    color: var(--card-heading-color);
    background-color: var(--body-color) !important;
    width: max-content;
    padding: 0 10px;
    font-size: 20px;
    transform: translate(-50%, 0);
}

.card-item {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0px 0px 8px rgb(0 0 0 / 10%);
}

.card-item-food {
    display: flex;
    padding-bottom: 30px !important;

}

.food-item-detail {
    flex: 0 0 60%;
    padding-right: 0.5rem;
}

.food-image-n-add-item {
    flex: 0 0 40%;
}

.item-price {
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 8px;
    line-height: 15px;
    cursor: pointer;
}

.item-price small {
    color: #848484;
    font-size: 85%;
}

.food-item-detail h5 {
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: var(--order-background-color);
}

.food-item-detail .item-description {
    font-size: 12px;
    color: var(--card-location-color);
}

.food-image-n-add-item {
    position: relative;

}

.food-image-n-add-item img {
    width: 100%;
    border-radius: 1rem;
    object-fit: cover;

}

.add-item-action {
    font-size: 16px;
    font-weight: 600;
    padding: 3px 12px;
    border: 1px solid var(--order-background-color);
    border-radius: 8px;
    width: max-content !important;
    text-align: center;
    position: absolute;
    background-color: white;
    position: absolute;
    bottom: -18px;
    left: 50%;
    transform: translate(-50%, 0%);
    text-decoration: none;
    color: var(--order-background-color)
}

.item-action {
    display: flex;
}

.item-action {
    position: absolute;
    bottom: -18px;
    left: 50%;
    transform: translate(-50%, 0%);
    color: white;
}

.item-action .subtract {
    padding: 5px;
    background-color: var(--order-background-color);
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    color: white;
    text-decoration: none;
    height: 32px;
}

.item-action p {
    padding: 5px;
    background-color: var(--order-background-color);
    margin-bottom: 0;
    height: 32px;
    width: 30px;
    text-align: center;
}

.item-action .add {
    padding: 5px;
    background-color: var(--order-background-color);
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    color: white;
    text-decoration: none;
    height: 32px;
}

.calories-detail {
    margin-top: 10px;
}

.calories-detail .overall-cal {
    background-color: #b3c677;
    width: 100%;
    display: block;
    text-align: center;
}

.ingridients-list {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 1rem 1rem;
    flex-wrap: wrap;
}

.ingridients-list li {
    display: flex;
    align-items: center;
    flex-direction: column;
}

.ingridients-list li .nutreents {
    font-weight: 500;
    color: var(--card-location-color);
    font-size: 12px;
}

.ingridients-list li span:nth-child(2) {
    font-size: 13px;
}

.cart-section {
    position: sticky;
    position: -webkit-sticky;
    top: 72px;
    z-index: 1;
    background: #fff;
    padding: 10px 10px;
    border-radius: 10px 10px 0px 0px;
    height: calc(100vh - 88px);
}

.categories-section {
    position: sticky;
    position: -webkit-sticky;
    top: 72px;
    z-index: 1;
    background: #fff;
    border-radius: 10px 10px 0px 0px;
    height: calc(100vh - 88px);
    /* border-bottom: 1px solid var(--card-heading-color); */
}

/* --------------------cart ---------------- */
.cart-heading {
    font-weight: 600;
    font-size: 17px;
    margin-bottom: 15px;
    color: var(--card-heading-color)
}

.order-type-container {
    display: flex;
    padding: 10px 0;
    border: 1px solid var(--divider-color);
    padding: 4px;
    border-radius: 1rem;
}

.btn-active-order {
    background-color: #76923b;
    color: white;
    outline: none;
    padding: 10px 1rem;
    border: none;
    /* font-size: 12px; */
    border-radius: 12px;
    width: 33%;
}

.btn-active-order:hover {
    background-color: #76923b;
    color: white;
}

.btn-active-order:active {
    background-color: #76923b;
    color: white;
}

.btn-inactive-order {
    color: var(--card-heading-color);
    padding: 10px 1rem;
    border: none;
    background-color: transparent;
    font-size: 12px;
    width: 33%;
}

.btn-inactive-order:hover {
    color: var(--card-heading-color);
    border: none;
}

.btn-inactive-order:active {
    border: none;
    border-radius: 12px;
}

.orderl-list {
    overflow-y: auto;
    max-height: 350px;
    padding-right: 10px;
    padding-left: 10px;
}

.order-item {
    display: flex;
    align-items: start;
    justify-content: space-between;
}

.order-item {
    display: flex;
    align-items: start;
    margin-bottom: 10px;
    border-bottom: 1px dashed var(--order-background-color);
    padding: 10px 0;
}

.order-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.delhivery-time {
    font-size: 12px;
    width: 100%;

}

.item-small-hd {
    font-size: 14px;
    margin-bottom: 3px;
    font-weight: 500;
    line-height: 20px;

}

.item-type-hd {
    font-size: 12px;
}

.item-price {
    margin-bottom: 10px;
    color: var(--dark-brown-color);
}

.item-price span {
    font-weight: 400;
    margin-right: 8px;
    font-size: 13px;
}

.item-action-cart {
    position: relative;
    bottom: 0
}

.item-action-cart a,
.item-action-cart p {
    background-color: white !important;
    color: var(--order-background-color) !important;
    border-color: var(--order-background-color);
    border-top: 1px solid;
    border-bottom: 1px solid;
}

.item-action-cart .add {
    border-right: 1px solid var(--order-background-color);
}

.item-action-cart .subtract {
    border-left: 1px solid var(--order-background-color);
}

.order-desscription {
    padding-right: 10px;
    margin-bottom: 0.5rem;
}

.final-subtotal {
    color: var(--order-background-color);
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-weight: 600;
}

/* category */
.category-item {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    color: var(--card-heading-color);
    padding: 10px;
}

.category-item .order-count {
    font-weight: 600;
    color: var(--order-background-color);
}

.category-item .order-count p {
    margin-bottom: 0;
}

.category-item.active {
    background: linear-gradient(90deg, var(--order-background-color) 0%, #ffffff 100%);
    color: white;
    border-left: 3px solid #364e08;
}

/* .modal-food-item{
        max-width: 300px;
    } */

.modal-food-item .modal-content {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

.modal-food-item .modal-body {
    background-color: var(--body-color);
    padding: 0;
}

.btn-close-modal {
    position: absolute;
    top: 30px;
    right: 30px;
    background-color: white;
    padding: 10px;
    border-radius: 30px;
}

.item-img {
    background-color: white;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    padding: 1rem;
}

.item-img h5 {
    color: var(--order-background-color);
    font-size: 24px;
    font-weight: 700;
}

.item-img img {
    border-radius: 1rem;
    width: 100%
}

.price-text {
    font-size: 20px;
    color: var(--card-heading-color);
}

.meal-category {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    background-color: white
}

.extra-status {
    text-transform: uppercase;
    font-size: 13px;

    color: var(--card-location-color);
}

.toggle-button-extra {
    flex-direction: column;
    width: 33%;
    height: 100%;
}

.toggle-button-extra .extra-status {
    height: 30px;
}

.extra-options {
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

.text-status {
    color: var(--card-heading-color);
}

.nutrients-facts {
    color: var(--dark-brown-color);
    font-size: 1rem;
    font-weight: 700;
}

.meal-category-table table th {
    background-color: var(--dark-brown-color);
    color: white;
    text-align: center;
}

.meal-category-table table td {
    text-align: center;
}

.item-ippopup-action {
    position: relative;
    left: 0;
    bottom: 0;
    transform: translate(0, 0)
}

.item-ippopup-action a,
.item-ippopup-action p {
    border-top: 1px solid var(--order-background-color);
    border-bottom: 1px solid var(--order-background-color);
    background-color: white !important;
    color: var(--darkest-green-bg-color) !important;
    height: 38px !important;

}

.item-ippopup-action .subtract {
    border-left: 1px solid var(--order-background-color);

}

.item-ippopup-action .add {
    border-right: 1px solid var(--order-background-color);
}

.modal-search-dish {}

.search-item-list {
    width: 100%;
    border-bottom: 0;
}

.search-item-list li {
    border-bottom: 1px dashed var(--card-location-color);
    width: 100%;
}

.search-item-list li:last-child {
    border: none;
}

.modal-search-dish .bg-modal-body-color {
    background-color: var(--body-color);
}

.searchitem-dish-image {
    width: 100px;
    height: 70px;
    object-fit: cover;
    border-radius: 10px;
}

.searchitem-dish-name {
    font-size: 1rem;
    color: var(--card-heading-color);
    padding-left: 1rem;
}

.mobile-cart {
    display: none;
}

.view-cart-mobile {
    display: flex;
    font-size: 18px;
    align-items: center;
    font-weight: 700;
    justify-content: space-between;
}

@media screen and (max-width:991.91px) {
    .mobile-cart {
        display: block;
        position: fixed;
        bottom: 30px;
        z-index: 99;
        padding: 10px;
        width: 100%;
    }

    .mobile-cart button {
        width: calc(100vw - 2rem);
        padding: 1rem;
    }

    .cart-desktop {
        display: none;
    }
}
</style>
