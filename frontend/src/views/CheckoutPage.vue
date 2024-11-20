
<script>
export default {
  name: 'CheckoutPage',
}
</script>


<template>
    <div class="container">
        <div class="row">
            <div class="  col-lg-8 col-md-12 col-sm-12 col-12 p-3">
                <div class="store-n-diliveri bg-white p-2 rounded">
                    <div class="checkout-title-card">
                        <div class="back-button">
                            <i class="fa-regular fa-circle-left"></i>
                        </div>
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
                        </div>

                    </div>
                </div>
            </div>
            <div class="  col-lg-4 col-md-12 col-sm-12 col-12 p-3">
                <div class="bg-white  p-2 rounded">

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
        margin-right: 1rem;
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

</style>