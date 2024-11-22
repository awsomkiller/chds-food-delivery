
<script>
export default {
  name: 'CheckoutPage',
}
</script>


<template>
    <div class="container">
        <div class="row">
            <div class="  col-lg-8 col-md-12 col-sm-12 col-12 p-3">
                <div class="store-n-diliveri bg-white p-2 rounded mb-3">
                    <div class="checkout-title-card">
                        <a href="" class="back-button text-decoration-none">
                            <i class="fa-regular fa-circle-left"></i>
                        </a>
                        <div class="outlet-card p-2 ">
                            <div class="outlet-detail">
                                <h5> Chi Hun Da Su </h5>
                                <p> Location </p>
                            </div>
                        </div>

                    </div>
                    
                    <div class="order-type-container">
                        <button type="button" class="btn-active-order"> <span> Delivery </span>  <span class="delhivery-time">(20 Minutes)</span> </button>
                        <button type="button" class="btn-inactive-order">Pick Up</button>
                        <!-- <button type="button" class="btn-inactive-order">In Car</button> -->
                    </div>

                    <div class="selected-address-container p-2">
                        <div class="no-address-container">
                            <div class="no-address my-3">

                                <i class="fa-solid fa-location-dot"></i>
                                <p class="mb-0"> No Delivery Address Selected</p>

                            </div>

                            <a class="my-3 " href=""> Select</a>

                        </div>
                        <div  class="address-radio">
                            <input type="radio" class="btn-check " name="options" id="option1" autocomplete="off" checked>
                            <label class="btn btn-primary" for="option1">
                                <p class="address-name mb-0">Address 1 </p>
                                <p class="address-description mb-0"> 2076, Sector 79, Mohali </p>
                            </label>

                            <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
                            <label class="btn btn-outline-primary" for="option2"> 
                                <p class="address-name mb-0">Address 2 </p>
                                <p class="address-description mb-0"> 2076, Sector 79, Mohali </p>
                            </label>

                            <a href="" class="text-decoration-none"  >
                                <div class="add-addrss-button">
                                    <div>
                                        <i class="fa-solid fa-plus"></i>
                                    </div>
                                    <p class="mb-0"> Add New Address </p>
                                </div>
                            </a>
                            
                        </div>

                    </div>
                </div>

                <!-- items added in the cart list -->
                <h6>Items Added</h6>
                <div class="store-n-diliveri bg-white p-3 rounded mb-3">
                    <ul class="list-unstyled mb-0">

                        <!-- item for checkout -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>


                         <!-- item for checkout -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>

                         <!-- item for checkout -->
                         <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>


                         <!-- item for checkout -->
                         <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>


                         <!-- item for checkout -->
                         <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>


                         <!-- item for checkout -->
                         <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-primary">Delete</button>
                                <p class="mb-0"> $ 765 </p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="  col-lg-4 col-md-12 col-sm-12 col-12 p-3">
                <div class="offer-card-container bg-white mb-3 p-2 rounded">
                    <div class="coupon-card bg-white rounded p-2 mb-3">
                        <div class="coupon-icon">
                            <i class="fa-solid fa-ticket"></i>
                        </div>
                        <div class="">
                            <p class="coupon-content"> LPN200 <span class="coupon-description"> Get Flat Discount of $ 20 on Minimum Billing of $ 999. </span> </p>

                        </div>

                        <a class="apply-coupon"> Apply</a>

                    </div>
                </div>
                checkout
            </div>

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


    .checkout-title-card{
        display: flex;
        align-items: center;
    }
    

    .back-button{
        font-size: 28px;
        margin-right: 0.5rem;
        color: var(--card-heading-color)
    }

    .checkout-title-card .outlet-detail p{
        font-size: 12px;
    }

    .store-n-diliveri{
        /* display: flex; */
        

    }

    .order-type-container button {
        width: 50%;
        font-size: 1rem;
    }

    .order-type-container button span:nth-child(2){
        /* font-size: 12px; */
    }


    /* ------------------- addresss setion ----------------- */

    .no-address-container{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .no-address{
        display: flex ;
        align-items: center;
        color: var(--card-heading-color);
        gap:1rem;
    }

    .no-address-container a{
       color: var(--order-background-color);
    }
    

    .no-address i{
        color: var(--dark-brown-color);
        font-size: 20px;
    }

    .address-name{
        font-size: 16px;
        font-weight: 600;
        color: var(--card-heading-color);
    }
    .address-description{
        font-size: 14px;
        color: var(--card-location-color);
    }

    .address-radio{
        display: flex;
        align-items: flex-start;
        flex-wrap: wrap;
        row-gap: 1rem;
    }
    .address-radio .btn-check:checked+.btn{
        background-color:white;
        margin-right: 1rem;
        text-align:left;
        border-color: var(--dark-brown-color);
    }

    .address-radio .btn-check+.btn{
        background-color:white;
        margin-right: 1rem;
        text-align:left;
        border: 2px solid var(--body-color);
    }

    .add-addrss-button{
        padding: 16px 16px;
        height: 100%;
        width: fit-content;
        text-align:center;
        background-color: var(--light-green-color);
        /* text-align:left; */
        border: 2px solid var(--light-green-color);
        color: white;
        display: flex;
        gap: 10px;
        height: 100%;
        font-size: 1rem;
        border-radius: 0.375rem;
    }

    a.add-addrss-button{
        cursor: pointer;
    }

    .Item-for-checkout{
        display: flex;
        align-items: start;
        justify-content: space-between;
        /* margin-bottom: 1rem; */
        padding: 1rem 0;
        border-bottom:  1px dashed var(--divider-color);
    }



    .price-n-item-option{
        display: flex;
        gap: 1rem;
        align-items: center;
    }

    .offer-card-container{

    }

    .coupon-card{
        padding: 10px;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }

    .coupon-card .coupon-icon{
        color: var(--dark-brown-color);
    }

    .coupon-description{
        display: block;
        font-size: 10px;
        column-rule-color: var(--card-location-color);
    }

    .coupon-content{
        font-size: 12px;
    }

    .apply-coupon{
        color: var(--order-background-color);
        font-size: 12px
    }


    @media screen and (max-width:767.91px) {

        .address-radio .btn-check:checked+.btn{
            width: 100%;
        }
        .address-radio .btn-check+.btn{
            width: 100%;
        }
        .price-n-item-option{
            flex-direction: column;
        }
        .Item-for-checkout{
            align-items: flex-start;
        }
    
    }
</style>