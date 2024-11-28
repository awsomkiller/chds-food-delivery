<script>
import { storeToRefs } from 'pinia';
import { useCartStore } from '@/stores/cart';
import { useWorkingDaysStore } from '@/stores/workingdays';
import { useAddressStore } from '@/stores/address';
import { useAuthStore } from '@/stores/auth';
import { onMounted, ref, watch, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { stripePromise } from '@/stripe.js';
import caxios from '../../axios';

export default {
  name: 'CheckoutPage',
  setup() {
    const cartStore = useCartStore();
    const workingDaysStore = useWorkingDaysStore();
    const addressStore = useAddressStore();
    const authStore = useAuthStore();

    const billing_address = authStore.getBillingAddress();
    const { cart, totalQty, TotalOrderPrice } = storeToRefs(cartStore);
    const {
      deliverydays,
      pickupdays,
      activeDeliveryDay,
      activePickUpDay,
      activePickupTimeSlot,
      activeDeliveryTimeSlot,
    } = storeToRefs(workingDaysStore);
    const { eligibleAddress, pickUpAddresses } = storeToRefs(addressStore);

    const selectedDeliveryDayId = ref('');
    const selectedDeliveryTimeSlotId = ref('');
    const selectedPickupDayId = ref('');
    const selectedPickupTimeSlotId = ref('');
    const selectedOption = ref('delivery');
    const selectedDeliveryAddress = ref({});
    const selectedPickupAddress = ref({});

    const router = useRouter();

    if (totalQty.value <= 0) {
      router.push({ name: 'Ordernow' });
    }

    const stripe = ref(null);
    const elements = ref(null);
    const cardElement = ref(null);
    const cardElementRef = ref(null);

    const initializeStripe = async () => {
      stripe.value = await stripePromise;
      elements.value = stripe.value.elements();
      cardElement.value = elements.value.create('card');

      if (cardElementRef.value) {
        cardElement.value.mount(cardElementRef.value);
      } else {
        console.error('cardElementRef is null');
      }
    };

    const handleCheckOutSubmit = async () => {
      const payload = {};
      if (selectedOption.value == 'delivery') {
        if (
          Object.keys(activeDeliveryDay.value).length === 0 ||
          Object.keys(activeDeliveryTimeSlot.value).length === 0
        ) {
          alert('Delivery Date/Time Not Selected');
          return;
        }
        if(Object.keys(selectedDeliveryAddress.value).length === 0){
            alert('Delivery Address is not selected')
        }
        payload.schedule_date = activeDeliveryDay.value.date;
        payload.time_slot = activeDeliveryTimeSlot.value.name;
        payload.order_type = 'DELIVERY';
        payload.delivery_location = formatAddress(selectedDeliveryAddress.value)
      } else {
        if (
          Object.keys(activePickUpDay.value).length === 0 ||
          Object.keys(activePickupTimeSlot.value).length === 0
        ) {
          alert('Pickup Date/Time Not Selected');
          return;
        }
        if(Object.keys(selectedPickupAddress.value).length === 0){
            alert('Delivery Address is not selected')
        }
        payload.schedule_date = activePickUpDay.value.date;
        payload.time_slot = activePickupTimeSlot.value.name;
        payload.order_type = 'PICKUP';
        payload.pickup_location = formatAddress(pickUpAddresses.value);
      }
      payload.amount = TotalOrderPrice.value;
      payload.menu_item = JSON.stringify(cart.value);

      try {
        const response = await caxios.post('/orders/create/', payload);
        const { order_id, client_secret } = response.data;

        // Confirm the payment
        const result = await stripe.value.confirmCardPayment(client_secret, {
          payment_method: {
            card: cardElement.value,
            billing_details: {
              // Include billing details if needed
            },
          },
        });

        if (result.error) {
          // Show error to customer
          console.error(result.error.message);
          alert('Payment failed: ' + result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            // Payment succeeded
            alert('Payment successful!');
            router.push({ name: 'OrderConfirmation', params: { orderId: order_id } });
          }
        }
      } catch (error) {
        console.error('Error during checkout:', error.response || error);
        alert('An error occurred during checkout: ' + (error.response?.data?.detail || error.message));
      }
    };

    // Handle delivery day selection change
    const handleDeliveryDayChange = (event) => {
      const dayId = event.target.value;
      workingDaysStore.setActiveDeliveryDay(dayId);
      selectedDeliveryTimeSlotId.value = workingDaysStore.activeDeliveryTimeSlot?.id || '';
    };

    // Handle delivery time slot selection change
    const handleDeliveryTimeSlotChange = (event) => {
      const timeSlotId = event.target.value;
      workingDaysStore.setActiveDeliveryTimeSlot(timeSlotId);
    };

    // Handle pickup day selection change
    const handlePickupDayChange = (event) => {
      const dayId = event.target.value;
      workingDaysStore.setActivePickupDay(dayId);
      selectedPickupTimeSlotId.value = workingDaysStore.activePickupTimeSlot?.id || '';
    };

    // Handle pickup time slot selection change
    const handlePickupTimeSlotChange = (event) => {
      const timeSlotId = event.target.value;
      workingDaysStore.setActivePickupTimeSlot(timeSlotId);
    };

    const handleDelete = (id) => {
      cartStore.removeFromCart(id);
    };

    const formatAddress = (addressObj) => {
        const {
            name,
            street_address1,
            street_address2,
            suburbs,
            city,
            postal_code
        } = addressObj;
        const addressParts = [];
        if (name) {
            addressParts.push(name);
        }
        let street = street_address1 || "";
        if (street_address2) {
            street += `, ${street_address2}`;
        }
        if (street) {
            addressParts.push(street);
        }
        if (suburbs) {
            addressParts.push(suburbs);
        }
        let cityLine = city || "";
        if (postal_code) {
            cityLine += postal_code ? `, ${postal_code}` : "";
        }
        if (cityLine) {
            addressParts.push(cityLine);
        }
        const formattedAddress = addressParts.join("\n");

        return formattedAddress;
        }

    watch(
      totalQty,
      (newCount, oldCount) => {
        if (newCount <= 0 && newCount !== oldCount) {
          router.push({ name: 'Ordernow' });
        }
      }
    );

    onMounted(async () => {
      await nextTick();
      initializeStripe();
      workingDaysStore.fetchWorkingDays();
    });

    return {
      cart,
      totalQty,
      billing_address,
      eligibleAddress,
      pickUpAddresses,
      TotalOrderPrice,
      handleDelete,
      selectedOption,
      deliverydays,
      pickupdays,
      activeDeliveryDay,
      activePickUpDay,
      selectedDeliveryDayId,
      selectedDeliveryTimeSlotId,
      selectedPickupDayId,
      selectedPickupTimeSlotId,
      selectedDeliveryAddress,
      selectedPickupAddress,
      handleCheckOutSubmit,
      handleDeliveryDayChange,
      handleDeliveryTimeSlotChange,
      handlePickupDayChange,
      handlePickupTimeSlotChange,
      cardElementRef,
    };
  },
};
</script>



<template>
    <div class="container">
        <div class="row">
            <div class="  col-lg-8 col-md-12 col-sm-12 col-12 p-3">
                <div class="store-n-diliveri bg-white p-2 rounded mb-3">
                    <div class="outlet-with-billing-add">
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
                        <div class="billing-addshown" v-if="billing_address">
                            <p> Billing-Address</p>
                            <h6> {{ billing_address }}</h6>
                        </div>
                    </div>

                    <div class="p-2">
                        <div class="order-type-container">           
                            <div class="delivery-option rounded w-100">
                            <!-- Delivery Option -->
                            <input
                                type="radio"
                                class="btn-check"
                                name="optionsdelivery"
                                id="deliverychosen"
                                autocomplete="off"
                                value="delivery"
                                v-model="selectedOption"
                                checked
                            >
                            <label class="btn btn-primary" for="deliverychosen">
                                <span> Delivery </span>  
                            </label>

                            <!-- Pickup Option -->
                            <input
                                type="radio"
                                class="btn-check"
                                name="optionsdelivery"
                                id="pickupchosen"
                                autocomplete="off"
                                value="pickup"
                                v-model="selectedOption"
                            >
                            <label class="btn btn-outline-primary" for="pickupchosen">
                                Pick Up
                            </label>
                            </div>

                    <!-- Uncomment and customize as needed -->
                    <!-- <button type="button" class="btn-inactive-order">In Car</button> -->
                </div>
                    <div class="selected-address-container mt-3 p-2" v-if="selectedOption == 'delivery'">
                        <div class="alert alert-danger" role="alert" v-if="!deliverydays.length">
                            Kitchen is not taking any delivery orders right now, Try Pick Up !
                        </div>
                        <div class="schedule-order mb-3" v-else>
                            <h6>Select Delivery Date and Time</h6>
                            <div class="row">
                            <!-- Select Delivery Day -->
                            <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                <label for="deliveryDay" class="form-label">Select Day</label>
                                <select 
                                id="deliveryDay" 
                                class="form-select" 
                                v-model="selectedDeliveryDayId" 
                                @change="handleDeliveryDayChange"
                                >
                                <option disabled value="">Select Day</option>
                                <option 
                                    v-for="day in deliverydays" 
                                    :key="day.id" 
                                    :value="day.id"
                                >
                                    {{ day.date }}
                                </option>
                                </select>
                            </div>

                            <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                <label for="deliveryTimeSlot" class="form-label">Choose Time Slot</label>
                                <select 
                                id="deliveryTimeSlot" 
                                class="form-select" 
                                v-model="selectedDeliveryTimeSlotId" 
                                :disabled="!activeDeliveryDay"
                                @change="handleDeliveryTimeSlotChange"
                                >
                                <option disabled value="">
                                    {{ activeDeliveryDay && activeDeliveryDay.time_slot && activeDeliveryDay.time_slot.length ? 'Choose Time Slot' : 'No Time Slots Available' }}
                                </option>
                                <option 
                                    v-for="slot in activeDeliveryDay.time_slot" 
                                    :key="slot.id" 
                                    :value="slot.id"
                                >
                                    {{ slot.name }}
                                </option>
                                </select>
                            </div>
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert" v-if="!eligibleAddress.length">
                            You don't have any address eligible for delivery, Please choose pickup option.
                        </div>
                        <div  class="address-radio">
                            <div v-for="address in eligibleAddress" :key="address.id">
                                <input 
                                    type="radio" 
                                    class="btn-check" 
                                    name="deliveryAddress" 
                                    :id="'delivery-' + address.id" 
                                    autocomplete="off" 
                                    v-model="selectedDeliveryAddress" 
                                    :value="address" 
                                >
                                <label class="btn btn-primary" :for="'delivery-' + address.id">
                                    <p class="address-name mb-0">{{ address.name }} </p>
                                    <p class="address-description mb-0"> {{ address.street_address1 }}, {{ address.street_address2 }}, {{ address.suburbs }}, {{ address.postal_code }} </p>
                                </label>
                            </div>

                            <a href="" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#addressModal" >
                                <div class="add-addrss-button">
                                    <div>
                                        <i class="fa-solid fa-plus"></i>
                                    </div>
                                    <p class="mb-0"> Add New Address </p>
                                </div>
                            </a>
                        </div>
                    </div>
                    
                    <div class="pickup-details-container mt-3 p-2" v-else>
                        <div class="alert alert-danger" role="alert" v-if="!pickupdays.length">
                            Kitchen is closed for new orders.
                        </div>
                        <div class="schedule-order mb-3" v-else>
                            <h6>Select Pickup Date and Time</h6>
                            <div class="row">
                                <!-- Select Pickup Day -->
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                    <label for="pickupDay" class="form-label">Select Day</label>
                                    <select 
                                        id="pickupDay" 
                                        class="form-select" 
                                        v-model="selectedPickupDayId" 
                                        @change="handlePickupDayChange"
                                    >
                                        <option disabled value="">Select Day</option>
                                        <option 
                                            v-for="day in pickupdays" 
                                            :key="day.id" 
                                            :value="day.id"
                                        >
                                            {{ day.date }}
                                        </option>
                                    </select>
                                </div>

                                <!-- Select Pickup Time Slot -->
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                    <label for="pickupTimeSlot" class="form-label">Choose Time Slot</label>
                                    <select 
                                        id="pickupTimeSlot" 
                                        class="form-select" 
                                        v-model="selectedPickupTimeSlotId" 
                                        :disabled="!activePickUpDay.time_slot || !activePickUpDay.time_slot.length"
                                        @change="handlePickupTimeSlotChange"
                                    >
                                        <option disabled value="">
                                            {{ activePickUpDay && activePickUpDay.time_slot && activePickUpDay.time_slot.length ? 'Choose Time Slot' : 'No Time Slots Available' }}
                                        </option>
                                        <option 
                                            v-for="slot in activePickUpDay.time_slot" 
                                            :key="slot.id" 
                                            :value="slot.id"
                                        >
                                            {{ slot.name }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div>
                            <h6> Select the outlet to pick up the order </h6>
                            <div  class="address-radio">
                                <div v-for="address in pickUpAddresses" :key="address.id">
                                    <input 
                                        type="radio" 
                                        class="btn-check" 
                                        name="outlets" 
                                        id="outlet1" 
                                        autocomplete="off" 
                                        v-model="selectedPickupAddress" 
                                        checked
                                    >
                                    <label class="btn btn-primary" :for="'pickup-' + address.id">
                                        <p class="address-name mb-0">{{ address.name }} </p>
                                        <p class="address-description mb-0"> {{ address.street_address1 }},{{ address.street_address2 }},</p>
                                        <p class="address-description mb-0">{{ address.city }}, {{ address.state }},</p>
                                        <p class="address-description mb-0">{{ address.postal_code }}, Australia</p>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- <div class="coupon-code-apply p-2">
                        <label for="inputZip" class="form-label">Coupon Code (Optional)</label>
                        <input type="text" class="form-control" placeholder="Enter Coupon Code" id="inputZip">
                    </div> -->
                </div>
            </div>
                <!-- items added in the cart list -->
                <h6>Items Added</h6>
                <div class="store-n-diliveri bg-white p-3 rounded mb-3">
                    <ul class="list-unstyled mb-0">

                        <!-- item for checkout -->
                        <li class="Item-for-checkout" v-for="item in cart" :key="item.id">
                            <div>
                                <p class="mb-0">{{ item.quantity }} <span> <i class="fa-solid fa-xmark"></i></span> {{ item.meal_name }} </p>
                                <p class="item-type-hd mb-0">size: {{ item.selected_meal_portion_name }} ({{item.selected_meal_portion_weight}}g)</p>
                                <p class="item-type-hd mb-0" v-for="addon in item.addons" :key="addon.id">Extra {{ addon.name }}</p>
                            </div>
                            <div class="price-n-item-option">
                                <button type="button" class="btn btn-danger" @click="handleDelete(item.id)">Delete</button>
                                <p class="mb-0"> $ {{ item.total_price }} </p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="  col-lg-4 col-md-12 col-sm-12 col-12 p-3">
                <!-- ---- addons ---------------------- -->
                <div class="p-3 bg-white rounded">
                    <h4 class="extra-status"> Select Payment Method </h4>
                    <div class="meal-addons payment-method rounded ">
                        <input type="radio" class="btn-check" name="options" id="addons1" checked>
                        <label class="btn btn-primary w-100" for="addons1">
                            <p class="mb-0">
                                Pay by Wallet
                            </p>
                            
                        </label>

                        <input type="radio" class="btn-check" name="options" id="addons2">
                        <label class="btn btn-primary w-100" for="addons2">
                            <p class="mb-0">
                                Pay Online
                            </p>
                            
                        </label>
                        
                    </div>
                </div>
                <div class="biling-details-container bg-white p-3 rounded">
                    <div class="billing-detail">
                        <p class=""> Subtotal </p>
                        <p class=""> $ {{ TotalOrderPrice }} </p>
                    </div>
                    <div class="billing-detail">
                        <p class=""> Tax </p>
                        <p class=""> $ 0</p>
                    </div>
                    <div class="billing-detail detail-green">
                        <p class=""> Delivery </p>
                        <p class=""> Yay! Free Delivery </p>
                    </div>     
                    <div class="billing-detail grand-total">
                        <p class=""> Grand Total </p>
                        <p class=""> $ {{ TotalOrderPrice }} </p>
                    </div>
                    <!-- <form @submit.prevent="handleCheckOutSubmit"> -->
                        <div id="card-element" ref="cardElementRef"></div>
                        <button type="button" class="btn btn-primary w-100 mt-2" @click="handleCheckOutSubmit"> Pay $ {{ TotalOrderPrice }} </button>
                    <!-- </form> -->
                </div>
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


    .delivery-option{
        display:flex;
        align-items: center;
        gap: 10px;
    }

    
.delivery-option .btn-check:checked+.btn{
    background-color: var(--order-background-color) ;
    border-color: var(--order-background-color) ;
    color: white;
}

.delivery-option .btn-check:checked+.btn:hover{
    background-color: var(--order-background-color) ;
    border-color: var(--order-background-color) ;
    color: white;
}

.delivery-option .btn-check+.btn{
    background-color: transparent ;
    color: var(--order-background-color);
    border-color: var(--order-background-color) ;
    padding: 0.75rem 2rem;
    border-radius:10px;
    width:100%;
}
.delivery-option .btn-check+.btn:hover{
    background-color: var(--order-background-color) ;
    color: white !important;
    color: var(--order-background-color);
    border-color: var(--order-background-color);
}

.biling-details-container{

}
.billing-detail{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap:10px;
}
.billing-detail p{
   width: fit-content;
   color: var(--card-location-color);
   font-size: 15px;
}

.detail-green p{
    font-size: 16px;
    color: var(--dark-brown-color);
}

.grand-total{
    font-weight: bold;
    color: var(--card-heading-color);
}

.outlet-with-billing-add{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    flex-wrap: wrap;
}

.outlet-with-billing-add .billing-addshown {
    padding: 0.5rem;
}

.outlet-with-billing-add .billing-addshown p{
    font-size: 12px;
    font-weight: 600;
    color: var(--card-location-color);
    margin-bottom: 0;

}
.outlet-with-billing-add .billing-addshown h6{
    font-size: 14px;
    color: var(--card-heading-color);

}

.payment-method{
    display: flex;
}
.payment-method .btn-check+.btn{
    width:fit-content !important;
    padding: 5px 20px !important;
    height: 36px;
    border:2px solid #d2d2d2 !important;
    color:#d2d2d2 !important ;
}
.payment-method .btn-check:checked+.btn{
    width:fit-content !important;
    background-color: #d2d2d2 !important;
    border:2px solid #d2d2d2 !important;
    color: var(--card-heading-color) !important;
    padding: 5px 20px !important;
    height: 36px;
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