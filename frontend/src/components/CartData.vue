<!-- CartData.vue -->
<script> 
    import { storeToRefs } from 'pinia';
    import { useCartStore } from '@/stores/cart';
    import { useAuthStore } from '@/stores/auth';
    import { useTranslationStore } from '@/stores/translation';
    
    export default {
        name: 'CartData',
        setup(){
            const cartStore = useCartStore();
            const authStore = useAuthStore();
            const translationStore = useTranslationStore();

            const t = (label, modules) => {
                return translationStore.translate(label, modules);
            };

            const { cart, totalQty, TotalOrderPrice } = storeToRefs(cartStore);
            const { user } = storeToRefs(authStore);

            const incrementItem = (itemId) => {
                cartStore.increaseItemQuantity(itemId);
            };

            const decrementItem = (itemId) => {
                cartStore.decreaseItemQuantity(itemId);
            };

            return{
                t,
                cart,
                user,
                totalQty,
                TotalOrderPrice,
                incrementItem,
                decrementItem,
            };
        }
    };
</script>

<template>
    <div class="bg-white cart-section p-2 rounded ">
        <div class="pb-3">
            <div class="outlet-card p-2 mb-4">
                <div class="restaurent-img">
                    <img class="" src="../assets/CHDS logo Blk transparent.png"> 
                </div>
                <div class="outlet-detail">
                    <h5> {{ t('chi_hun_da_su', ['cart']) }} </h5>
                </div>
            </div>
            <h4 class="cart-heading mb-0"> {{ t('your_cart', ['cart']) }}</h4>
        </div>
        <div>
            <ul class="list-unstyled orderl-list">
                <li class="order-item" v-for="item in cart" :key="item.id">
                    <div class="order-desscription">
                        <p class="item-small-hd">{{ item.meal_name }}</p>
                        <p class="item-type-hd mb-0">Size: {{ item.selected_meal_portion_name }} ({{ item.selected_meal_portion_weight }}g)</p>
                        <p class="item-type-hd mb-0" v-for="addon in item.addons" :key="addon.id">Extra {{ addon.name }}</p>
                        <p class="item-price">
                            <span>{{ item.quantity }} x A${{ (item.selected_meal_portion_price + item.selected_meal_addon_price) }}</span>
                            <b style="display: inline-block; font-weight: 500;"> A${{ item.total_price }}</b>
                        </p>
                    </div>
                    <div class="order-count">
                        <div class="item-action item-action-cart">
                            <a href="javascript:void(0)" class="subtract" @click.prevent="decrementItem(item.id)">
                                <i class="fa-solid fa-minus"></i>
                            </a>
                            <p>{{ item.quantity }}</p>
                            <a href="javascript:void(0)" class="add" @click.prevent="incrementItem(item.id)">
                                <i class="fa-solid fa-plus"></i>
                            </a>
                        </div>
                    </div>
                </li>
            </ul> 
        </div>
        <div>
            <div class="final-subtotal">
                <span>{{ t('subtotal', ['cart']) }} </span>
                <span> A${{ TotalOrderPrice }}</span>
            </div>
            <div class="final-subtotal fw-normal">
                <span>{{ t('you_have_total', ['cart']) }} {{ totalQty }} {{ t('items_in_your_cart', ['cart']) }} </span>
            </div>
            <button type="button" class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#loginModal" v-if="!user"> {{ t('login_to_continue', ['cart']) }}</button>
            <button type="button" class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#addressModal" v-else-if="user && !user.primary_address"> {{ t('add_your_address', ['cart']) }}</button>
            <router-link to="/checkout" class="btn btn-primary w-100" v-else-if="user && totalQty > 0">{{ t('proceed_to_checkout', ['cart']) }} </router-link>
            <button v-else-if="user && totalQty <= 0" class="btn btn-primary w-100 " disabled >{{ t('proceed_to_checkout', ['cart']) }} </button>
        </div>         
    </div>
</template>


<style>
    :root{
        --body-color: #f1f0f5;
        --divider-color: #e4e4e4;
        --card-heading-color: #333333;
        --card-location-color:#787878;
       
        --darkest-green-bg-color: #576d27;
        --order-background-color: #76923b;
        --light-green-color: #b3c677;
        --dark-brown-color : #944c22;
        --light-brown-colo: #c5886b;
        --lightest-brown-colo: #f7d9ba;

    }

    .outlet-card{
        background-color: white;
        border-radius: 0.5rem;
        display: flex;
        gap: 10px;
    }
    .search-filter{
        background-color: white;
        border-radius: 0.5rem;
        vertical-align: middle;
    }

    .restaurent-img{
       border: 1px solid var(--divider-color);
       border-radius: 4px;
        
    }
    .restaurent-img img{
        width: 66px;
        height: 66px;
        object-fit: cover;
    }

    .outlet-detail h5{
        font-size: 17px;
        margin-bottom: 0;
        color: var(--card-heading-color);
    }
    .outlet-detail p{
        font-size: 15px;
        margin-bottom: 0;
        color: var(--card-location-color);
    }


    .divider-heading{
        border-top: 1px solid var(--divider-color);
        width: 100%;
        height: 5px;
        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
        position: relative;
    }

    .divider-heading h3{
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

    .card-item-food{
        display: flex;
        padding-bottom: 30px !important;
        
    }
    .food-item-detail{
        flex: 0 0 60%;
        padding-right: 0.5rem;
    }

    .food-image-n-add-item{
        flex: 0 0 40%;
    }

    .item-price {
        font-weight: 600;
        font-size: 15px;
        margin-bottom: 8px;
        line-height: 15px;
        cursor: pointer;
    }
    .item-price small{
        color: #848484;
        font-size: 85%;
    }

    .food-item-detail h5{
        font-size: 1rem;
        margin-bottom: 0.5rem;
        color: var(--order-background-color);
    }
    .food-item-detail .item-description{
        font-size: 12px;
        color: var(--card-location-color);
    }


    .food-image-n-add-item{
        position: relative;

    }

    .food-image-n-add-item img{
        width: 100%;
        border-radius: 1rem;
        object-fit: cover;
        
    }

    .add-item-action{
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

    .item-action{
        display: flex;
    }

    .item-action{
        position: absolute;
        bottom: -18px;
        left: 50%;
        transform: translate(-50%, 0%);
        color: white;
    }
    .item-action .subtract{
        padding:5px;
        background-color: var(--order-background-color);
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        color: white;
        text-decoration: none;
        height: 32px;
    }

    .item-action p{
        padding: 5px;
        background-color: var(--order-background-color);
        margin-bottom: 0;
        height: 32px;
        width: 30px;
        text-align: center;
    }
    .item-action .add{
        padding: 5px;
        background-color: var(--order-background-color);
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        color: white;
        text-decoration: none;
        height: 32px;
    }

    .calories-detail{
        margin-top: 10px;
    }
    .calories-detail .overall-cal{
        background-color: #b3c677;
        width: 100%;
        display: block;
        text-align: center;
    }
    

    .ingridients-list{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 1rem 1rem;
        flex-wrap: wrap;
    }

    .ingridients-list li{
        display: flex;
        align-items: center;
        flex-direction: column;
    }
    .ingridients-list li .nutreents{
        font-weight: 500;
        color: var(--card-location-color);
        font-size: 12px;
    }

    .ingridients-list li span:nth-child(2){
        font-size: 13px;
    }


    .cart-section{
        position: sticky;
        position: -webkit-sticky;
        top: 72px;
        z-index: 1;
        background: #fff;
        padding: 10px 10px;
        border-radius: 10px 10px 0px 0px;
        height: calc(100vh - 88px);
    }

    .categories-section{
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
    .cart-heading{
        font-weight: 600;
        font-size: 17px;
        margin-bottom: 15px;
        color: var(--card-heading-color)
    }
    .order-type-container{
        display: flex;
        padding: 10px 0;
        border: 1px solid var(--divider-color);
        padding: 4px;
        border-radius: 1rem;
    }

    .btn-active-order{
        background-color: #76923b;
        color: white;
        outline: none;
        padding: 10px 1rem;
        border:none;
        font-size: 12px;
        border-radius: 12px;
        width: 33%;
    }

    .btn-active-order:hover{
        background-color: #76923b;
        color: white;
    }
    .btn-active-order:active{
        background-color: #76923b;
        color: white;
    }

    .btn-inactive-order{
       color: var(--card-heading-color);
       padding: 10px 1rem;
       border:none;
       background-color: transparent;
       font-size: 12px;
       width: 33%;
    }
    .btn-inactive-order:hover{
       color: var(--card-heading-color);
        border: none;
    }
    .btn-inactive-order:active{
       border: none;
       border-radius: 12px;
    }


    .orderl-list{
        overflow-y: auto;
        max-height: 400px;
        padding-right: 10px;
        padding-left: 10px;
    }

    .order-item{
        display: flex;
        align-items: start;
        justify-content: space-between;
    }

    
    .order-item{
        display: flex;
        align-items: start;
        margin-bottom: 10px;
        border-bottom: 1px dashed var(--order-background-color);
        padding: 10px 0;
    }

    .order-item:last-child{
        border-bottom: none;
        margin-bottom: 0;
    }

    .delhivery-time{
        font-size: 9px;
        width: 100%;
        
    }
    .item-small-hd{
        font-size: 13px;
        margin-bottom: 3px;
        font-weight: 500;
        line-height: 20px;
    }

    .item-price{
        margin-bottom: 10px;
        color: var(--dark-brown-color);
    }

    .item-price span {
    font-weight: 400;
    margin-right: 8px;
    font-size: 13px;
    }

    .item-action-cart{
        position: relative;
        bottom:0
    }

    .item-action-cart a, .item-action-cart p {
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

    .order-desscription{
        padding-right: 10px;
        margin-bottom: 0.5rem;
    }
    .final-subtotal{
        color: var(--order-background-color);
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        font-weight: 600;
    }



    /* category */
    .category-item{
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        color: var(--card-heading-color);
        padding: 10px;
    }

    .category-item .order-count{
        font-weight: 600;
        color: var(--order-background-color);
    }
    .category-item .order-count p{
        margin-bottom: 0 ;
    }

    .category-item.active{
        background: linear-gradient(90deg, var(--order-background-color) 0%, #ffffff 100%);
        color: white;
        border-left: 3px solid #364e08;
    }







    /* .modal-food-item{
        max-width: 300px;
    } */

    .modal-food-item .modal-content{
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
    }
    .modal-food-item .modal-body{
        background-color: var(--body-color);
        padding: 0;
    }

    .btn-close-modal{
        position:absolute;
        top: 30px;
        right: 30px;
        background-color: white;
        padding: 10px;
        border-radius: 30px;
    }

    .item-img{
        background-color: white;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
        padding: 1rem;
    }

    .item-img h5{
       color: var(--order-background-color);
       font-size: 24px;
       font-weight: 700;
    }


    .item-img img{
        border-radius: 1rem;
        width:100%
    }

    .price-text{
        font-size: 20px;
        color:var(--card-heading-color);
    }
    .meal-category{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        background-color: white
    }

    .extra-status{
        text-transform: uppercase;
        font-size: 1rem;
       
        color: var(--card-location-color);
    }

    .text-status{
        color: var(--card-heading-color);
    }
    .nutrients-facts{
        color: var(--dark-brown-color);
        font-size: 1rem ;
        font-weight: 700;
    }

    .meal-category-table table th{
        background-color: var(--dark-brown-color);
        color: white;
        text-align: center;
    }

    .meal-category-table table td{
        text-align: center;
    }

    .item-ippopup-action{
        position: relative;
        left: 0;
        bottom:0;
        transform: translate(0,0)
    }

    .item-ippopup-action a, .item-ippopup-action p{
       border-top: 1px solid var(--order-background-color) ;
       border-bottom:1px solid var(--order-background-color) ;
       background-color: white !important;
       color: var(--darkest-green-bg-color) !important;
       height:38px !important;

    }
    .item-ippopup-action .subtract{
       border-left: 1px solid var(--order-background-color) ;
       
    }

    .item-ippopup-action .add{
       border-right:1px solid var(--order-background-color) ;
    }


    .modal-search-dish{

    }

    .search-item-list{
        width:100%;
        border-bottom: 0;
    }

    .search-item-list li{
        border-bottom: 1px dashed var(--card-location-color);
        width: 100%;
    }

    .search-item-list li:last-child{
        border: none;
    }

    .modal-search-dish .bg-modal-body-color {
        background-color: var(--body-color) ;
    }

    .searchitem-dish-image{
        width: 100px;
        height: 70px;
        object-fit: cover;
        border-radius: 10px;
    }

    .searchitem-dish-name{
        font-size: 1rem;
        color: var(--card-heading-color);
        padding-left: 1rem;
    }




</style>