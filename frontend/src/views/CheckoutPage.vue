<script>
import { storeToRefs } from 'pinia';
import { useCartStore } from '@/stores/cart';
import { useWorkingDaysStore } from '@/stores/workingdays';
import { useAddressStore } from '@/stores/address';
import { useAuthStore } from '@/stores/auth';
import { useWalletStore } from '@/stores/wallet';
import { useTranslationStore } from '@/stores/translation';
import {
    onUpdated,
    computed,
    onMounted,
    ref,
    watch,
    nextTick
} from 'vue';
import { useRouter } from 'vue-router';
import { stripePromise } from '@/stripe.js';
import caxios from '../../axios';
import flatpickr from "flatpickr";
import "flatpickr/dist/flatpickr.min.css";

export default {
    name: 'CheckoutPage',
    setup() {
        const cartStore = useCartStore();
        const workingDaysStore = useWorkingDaysStore();
        const addressStore = useAddressStore();
        const authStore = useAuthStore();
        const walletStore = useWalletStore();
        const translationStore = useTranslationStore();

        const billing_address = authStore.getBillingAddress();
        const { user } = storeToRefs(authStore);
        const { billing_object } = user;
        const {
            cart,
            totalQty,
            TotalOrderPrice
        } = storeToRefs(cartStore);
        const {
            delivery_time_slots,
            pickup_time_slots,
            schedule_date,
            schedule_time,
        } = storeToRefs(workingDaysStore);
        const {
            eligibleAddress,
            pickUpAddresses
        } = storeToRefs(addressStore);
        const {
            balance
        } = storeToRefs(walletStore)

        const selectedOption = ref('delivery');
        const selectedDeliveryAddress = ref({});
        const selectedPickupAddress = ref({});
        const showFail = ref(null);
        const showSuccess = ref(null);
        // const scheduleDate = ref('');
        const router = useRouter();

        if (totalQty.value <= 0) {
            router.push({
                name: 'Ordernow'
            });
        }

        const stripe = ref(null);
        const elements = ref(null);
        const cardElement = ref(null);
        const cardElementRef = ref(null);
        const selectPaymentMethod = ref(null);
        const cardErrors = ref(null);
        const cardComplete = ref(false);

        const deliveryDatepicker = ref(null);
        const pickupDatepicker = ref(null);

        // Restaurant notes
        const notesTextField = ref('');
        const displayTextField = ref(false);

        const activeDatePickerRef = computed(() => {
            return selectedOption.value === 'delivery' ? deliveryDatepicker : pickupDatepicker;
        });

        const initializeStripe = async () => {
            try {
                stripe.value = await stripePromise;
                elements.value = stripe.value.elements();

                if (selectPaymentMethod.value === 'stripe') {
                    createAndMountCardElement();
                }
            } catch (error) {
                console.error('Error initializing Stripe:', error);
            }
        };

        const createAndMountCardElement = () => {
            if (cardElement.value) return;

            cardElement.value = elements.value.create('card', {
                style: {
                    base: {
                        fontSize: '16px',
                        color: '#32325d',
                    },
                },
            });

            if (cardElementRef.value) {
                cardElement.value.mount(cardElementRef.value);
            } else {
                console.error('cardElementRef is null');
            }

            cardElement.value.on('change', (event) => {
                cardErrors.value = event.error ? event.error.message : '';
                cardComplete.value = event.complete;
            });
        };

        const unmountCardElement = () => {
            if (cardElement.value) {
                cardElement.value.unmount();
                cardElement.value = null;
                cardErrors.value = null;
                cardComplete.value = false;
            }
        };

        const handleCheckOutSubmit = async () => {
            const payload = {};
            if (!schedule_date.value) {
                alert('Select Schedule date');
                return;
            }
            if (selectedOption.value == 'delivery') {
                if (Object.keys(selectedDeliveryAddress.value).length === 0) {
                    alert('Delivery Address is not selected');
                    return;
                }
                payload.order_type = 'DELIVERY';
                payload.delivery_location = selectedDeliveryAddress.value.id;
                payload.pickup_location = "";
            } else {
                if (Object.keys(selectedPickupAddress.value).length === 0) {
                    alert('Pickup Address not selected');
                    return;
                }

                payload.order_type = 'PICKUP';
                payload.delivery_location = "";
                payload.pickup_location = selectedPickupAddress.value.id;
            }
            payload.menu_item = JSON.stringify(cart.value);
            payload.payment_type = selectPaymentMethod.value;
            payload.schedule_date = schedule_date.value;
            payload.time_slot = schedule_time.value;
            payload.notes = notesTextField.value;

            if (selectPaymentMethod.value === "wallet") {
                try {
                    const response = await caxios.post('/orders/create/', payload);
                    if (response.status === 201) {
                        showSuccess.value.click();
                    } else {
                        showFail.value.click();
                    }
                } catch (error) {
                    console.log(error);
                    showFail.value.click();
                }
            } else {
                try {
                    const response = await caxios.post('/orders/create/', payload);
                    const { client_secret } = response.data;

                    let result;

                    if (selectPaymentMethod.value === 'stripe') {
                        // Handle Card Payment
                        result = await stripe.value.confirmCardPayment(client_secret, {
                            payment_method: {
                                card: cardElement.value,
                                billing_details: {
                                    address: {
                                        line1: `${billing_object.street_address1},${billing_object.street_address2}, ${billing_object.suburbs}`,
                                        city: billing_object.city,
                                        country: 'Australia',
                                        postal_code: billing_object.postal_code
                                    },
                                }
                            },
                        });
                    } else if (selectPaymentMethod.value === 'alipay') {
                        // Handle Alipay Payment
                        console.log(stripe.value);
                        result = await stripe.value.confirmAlipayPayment(client_secret,{
                            return_url: 'https://chds.com.au/order/success/',
                        });
                    } else if (selectPaymentMethod.value === 'wechat') {
                        // Handle WeChat Pay Payment
                        result = await stripe.value.confirmWeChatPayPayment(client_secret,{
                            return_url: 'https://chds.com.au/order/success/',
                        });
                    }

                    if (result.error) {
                        // Show error to customer
                        console.error(result.error.message);
                        showFail.value.click();
                    } else {
                        if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
                            // Payment succeeded
                            showSuccess.value.click();
                        }
                        // For redirect-based payment methods, the user will be redirected automatically
                    }
                } catch (error) {
                    console.error('Error during checkout:', error.response || error);
                    alert('An error occurred during checkout: ' + (error.response?.data?.detail || error.message));
                }
            }
        };

        // Handle pickup time slot selection change
        const handleTimeSlotChange = (event) => {
            const timeSlotId = event.target.value;
            workingDaysStore.setScheduleTime(timeSlotId);
        };

        const handleDelete = (id) => {
            cartStore.removeFromCart(id);
        };

        const getCurrentDateInGMT11 = () => {
            // Get the current date/time in GMT+11
            const currentDate = new Date();
            const gmt11Offset = 11 * 60; // Offset in minutes for GMT+11
            const gmt11Date = new Date(currentDate.getTime() + gmt11Offset * 60000 - currentDate.getTimezoneOffset() * 60000);
            return gmt11Date;
        };
        const calculateMinSelectableDate = () => {
            const currentDate = getCurrentDateInGMT11();
            const currentDay = currentDate.getDay(); // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
            const currentHour = currentDate.getHours();
            const functionalDays = [1, 3, 5]; // Monday, Wednesday, Friday
            const nonFunctionalDays = [0, 2, 4, 6]; // Sunday, Tuesday, Thursday, Saturday
            let minDate = new Date(currentDate);

            if (nonFunctionalDays.includes(currentDay)) {
                // If the current day is non-functional, minimum date is 2 days in advance
                minDate.setDate(currentDate.getDate() + 2);

                // Move to the next functional day
                while (!functionalDays.includes(minDate.getDay())) {
                    minDate.setDate(minDate.getDate() + 1);
                }
            } else if (functionalDays.includes(currentDay)) {
                // If the current day is functional
                if (currentHour < 20) {
                    // Before 8 PM, move to the next functional day
                    minDate.setDate(currentDate.getDate() + 1);
                } else {
                    // After 8 PM, move to the next-to-next functional day
                    minDate.setDate(currentDate.getDate() + 2);
                }

                // Ensure we land on a functional day
                while (!functionalDays.includes(minDate.getDay())) {
                    minDate.setDate(minDate.getDate() + 1);
                }
            }

            // Reset time to the start of the day
            minDate.setHours(0, 0, 0, 0);
            return minDate;
        }

        const initializeFlatpickr = async() => {
            await nextTick(); // Wait for DOM update
            const el = activeDatePickerRef.value?.value;
            if (el) {
                flatpickr(el, {
                    dateFormat: "Y-m-d",
                    minDate: calculateMinSelectableDate(),
                    enable: [
                        function (date) {
                            const functionalDays = [1, 3, 5];
                            // const isoDate = date.toISOString().split("T")[0];
                            return functionalDays.includes(date.getDay()) 
                        }
                    ],
                    onChange: (selectedDates, dateStr) => {
                        console.log(selectedDates)
                        console.log(dateStr);
                        workingDaysStore.setScheduleDate(dateStr);
                    }
                });
            }    
        };

        const handleClear = () => {
            notesTextField.value = "";
        }

        const toggleNoteVisibility = () => {
            displayTextField.value = !displayTextField.value;
        }

        const t = (label, modules) => {
            return translationStore.translate(label, modules);
        };

        watch(
            totalQty,
            (newCount, oldCount) => {
                if (newCount <= 0 && newCount !== oldCount) {
                    router.push({
                        name: 'Ordernow'
                    });
                }
            }
        );

        watch(
            selectPaymentMethod,
            (newValue, oldValue) => {
                console.log("Moving from", oldValue)
                if (newValue !== "wallet") {
                    initializeStripe();
                } else {
                    unmountCardElement();
                }
            }
        );

        watch(selectedOption, async (newVal) => {
            await nextTick();
            if (newVal === 'delivery') {
                initializeFlatpickr(deliveryDatepicker);
            } else {
                initializeFlatpickr(pickupDatepicker);
            }
        });

        onMounted(async () => {
            await nextTick();
            workingDaysStore.fetchTimeSlots();
            if (TotalOrderPrice.value > balance.value || !balance.value) {
                selectPaymentMethod.value = "stripe";
                await initializeStripe();
            } else {
                selectPaymentMethod.value = "wallet";
            }
            await initializeFlatpickr();
        });

        onUpdated(async () => {
            await initializeFlatpickr();
        });

        return {
            t,
            cart,
            totalQty,
            cardComplete,
            billing_address,
            eligibleAddress,
            pickUpAddresses,
            TotalOrderPrice,
            handleDelete,
            selectedOption,
            deliveryDatepicker,
            pickupDatepicker,
            showFail,
            balance,
            showSuccess,
            selectPaymentMethod,
            selectedDeliveryAddress,
            selectedPickupAddress,
            handleCheckOutSubmit,
            cardElementRef,
            handleTimeSlotChange,
            delivery_time_slots,
            pickup_time_slots,
            displayTextField,
            notesTextField,
            handleClear,
            toggleNoteVisibility,
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
                        <router-link to="/ordernow" class="back-button text-decoration-none">
                            <i class="fa-regular fa-circle-left"></i>
                        </router-link>
                        <div class="outlet-card p-2 ">
                            <div class="outlet-detail">
                                <h5>{{ t('chi_hun_da_su', ['checkout'])}}</h5>
                                <p> {{ t('location', ['checkout'])}}</p>
                            </div>
                        </div>
                    </div>
                    <div class="billing-addshown" v-if="billing_address">
                        <p> {{ t('billing_address', ['checkout'])}}</p>
                        <h6> {{ billing_address }}</h6>
                    </div>
                </div>

                <div class="p-2">
                    <div class="order-type-container">
                        <div class="delivery-option rounded w-100">
                            <!-- Delivery Option -->
                            <input type="radio" class="btn-check" name="optionsdelivery" id="deliverychosen" autocomplete="off" value="delivery" v-model="selectedOption">
                            <label class="btn btn-primary" for="deliverychosen">
                                <span> {{ t('delivery', ['checkout'])}} </span>
                            </label>

                            <!-- Pickup Option -->
                            <input type="radio" class="btn-check" name="optionsdelivery" id="pickupchosen" autocomplete="off" value="pickup" v-model="selectedOption">
                            <label class="btn btn-outline-primary" for="pickupchosen">
                                {{ t('pick_up', ['checkout'])}}
                            </label>
                        </div>
                    </div>
                    <div class="selected-address-container mt-3 p-2" v-if="selectedOption == 'delivery'">
                        <div class="alert alert-danger" role="alert" v-if="!delivery_time_slots.length">
                            Kitchen is not taking any delivery orders !!
                        </div>
                        <div class="schedule-order mb-3" v-else>
                            <h6>{{ t('select_delivery_date_and_time', ['checkout'])}}</h6>
                            <div class="row">
                                <!-- Select Delivery Day -->
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2"> 
                                    <label for="delivery-datepicker" class="form-label" >{{ t('choose_a_date', ['checkout'])}}</label>
                                    <input type="text" ref="deliveryDatepicker" id="delivery-datepicker" class="form-control datepicker" @load="initializeFlatpickr" />
                                </div>
                                
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                    <label for="deliveryTimeSlot" class="form-label">{{ t('choose_time_slot', ['checkout'])}}</label>
                                    <select id="deliveryTimeSlot" class="form-select" v-model="schedule_date" @change="handleTimeSlotChange">
                                        <option disabled value="">
                                            {{  delivery_time_slots.length ? t('choose_time_slot', ['checkout']) : t('no_time_slots', ['checkout']) }}
                                        </option>
                                        <option v-for="slot in delivery_time_slots" :key="slot.id" :value="slot.name">
                                            {{ slot.name }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert" v-if="!eligibleAddress.length">
                            {{ t('eligible _delivery_address_warning', ['checkout']) }}
                        </div>
                        <div class="address-radio">
                            <div v-for="address in eligibleAddress" :key="address.id">
                                <input type="radio" class="btn-check" name="deliveryAddress" :id="'delivery-' + address.id" autocomplete="off" v-model="selectedDeliveryAddress" :value="address">
                                <label class="btn btn-primary" :for="'delivery-' + address.id">
                                    <p class="address-name mb-0">{{ address.name }} </p>
                                    <p class="address-description mb-0"> {{ address.street_address1 }}, {{ address.street_address2 }}, {{ address.suburbs }}, {{ address.postal_code }} </p>
                                </label>
                            </div>

                            <a href="" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#addressModal">
                                <div class="add-addrss-button">
                                    <div>
                                        <i class="fa-solid fa-plus"></i>
                                    </div>
                                    <p class="mb-0">{{ t('add_new_address',['checkout'])}} </p>
                                </div>
                            </a>
                        </div>
                    </div>

                    <div class="pickup-details-container mt-3 p-2" v-else>
                        <div class="alert alert-danger" role="alert" v-if="!pickup_time_slots.length">
                            Kitchen is closed for Pickup order.
                        </div>
                        <div class="schedule-order mb-3" v-else>
                            <h6>{{ t('select_pickup_date_and_time',['checkout'])}}</h6>
                            <div class="row">
                                <!-- Select Pickup Day -->
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2"> 
                                    <label for="pickup-datepicker" class="form-label" @click="initializeFlatpickr">Choose a date</label>
                                    <input type="text" ref="pickupDatepicker" id="pickup-datepicker" class="form-control datepicker" />
                                </div>

                                <!-- Select Pickup Time Slot -->
                                <div class="col-lg-6 col-md-6 col-sm-12 col-12 p-2">
                                    <label for="pickupTimeSlot" class="form-label">{{ t('choose_time_slot',['checkout'])}}</label>
                                    <select id="pickupTimeSlot" class="form-select" v-model="schedule_date"  @change="handleTimeSlotChange">
                                        <option disabled value="">
                                            {{  pickup_time_slots.length ? t('choose_time_slot',['checkout']) : t('no_time_slots',['checkout']) }}
                                        </option>
                                        <option v-for="slot in pickup_time_slots" :key="slot.id" :value="slot.name">
                                            {{ slot.name }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div>
                            <h6> {{ t('select_the_outlet',['checkout']) }} </h6>
                            <div class="address-radio">
                                <div v-for="address in pickUpAddresses" :key="address.id">
                                    <input type="radio" class="btn-check" name="outlets" :id="'pickup-' + address.id" autocomplete="off" v-model="selectedPickupAddress" :value="address">
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
            <h6>{{ t('items_added',['checkout']) }}</h6>
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
                            <button type="button" class="btn btn-danger" @click="handleDelete(item.id)">{{ t('delete',['checkout']) }}</button>
                            <p class="mb-0"> A$ {{ item.total_price }} </p>
                        </div>
                    </li>
                </ul>
                <div id="app-note">
                    <!-- Button with pencil icon to toggle visibility -->
                    <button @click="toggleNoteVisibility" v-if="!notesTextField && !displayTextField" class="btn btn-secondary">
                    <i class="fa fa-pencil"></i> {{ t('add_notes_restaurant',['checkout']) }}
                    </button>

                    <p v-if="notesTextField && !displayTextField">{{ notesTextField }} <span @click="toggleNoteVisibility"><i class="fa fa-pencil"></i></span></p>

                    <!-- The note section, initially hidden -->
                    <div id="app-restaurant" v-if="displayTextField">
                    <textarea placeholder="Write your note here..." v-model="notesTextField"></textarea>
                    <div class="order-type-container">
                        <div class="delivery-option rounded w-100">
                        <input
                            type="radio"
                            class="btn-check"
                            name="optionsdelivery"
                            id="Clear"
                            autocomplete="off"
                            @click="handleClear"
                            checked
                            value="delivery"
                        />
                        <label class="btn btn-primary" for="Clear"><span> {{ t('clear',['checkout']) }} </span></label>
                        <input
                            type="radio"
                            class="btn-check"
                            name="optionsdelivery"
                            id="Save"
                            autocomplete="off"
                            @click="toggleNoteVisibility"
                            value="pickup"
                        />
                        <label class="btn btn-outline-primary" for="Save"> {{ t('save',['checkout']) }} </label>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
       <div class="col-lg-4 col-md-12 col-sm-12 col-12 p-3">
    <!-- Addons Section -->
    <div class="p-3 bg-white rounded">
        <h4 class="extra-status">{{ t('select_payment_method',['checkout']) }}</h4>
        <div class="meal-addons payment-method rounded">
            <!-- Wallet Option -->
            <input type="radio" class="btn-check" name="options" id="addons1" value="wallet" v-model="selectPaymentMethod" checked>
            <label class="btn btn-primary w-100" for="addons1">
                <p class="mb-0">
                    <img class="payment-icon" src="@/assets/wallet.png" alt="Wallet">
                </p>
            </label>

            <!-- Stripe Option -->
            <input type="radio" class="btn-check" name="options" id="addons2" value="stripe" v-model="selectPaymentMethod">
            <label class="btn btn-primary w-100" for="addons2">
                <p class="mb-0">
                    <img class="payment-icon" src="@/assets/stripe.png" alt="Stripe">
                </p>
            </label>

            <!-- WeChat Option -->
            <input type="radio" class="btn-check" name="options" id="addons3" value="wechat" v-model="selectPaymentMethod">
            <label class="btn btn-primary w-100" for="addons3">
                <p class="mb-0">
                    <img class="payment-icon" src="@/assets/wechat.png" alt="WeChat">
                </p>
            </label>

            <!-- PayPal Option -->
            <input type="radio" class="btn-check" name="options" id="addons4" value="paypal" v-model="selectPaymentMethod">
            <label class="btn btn-primary w-100" for="addons4">
                <p class="mb-0">
                    <img class="payment-icon" src="@/assets/money.png" alt="PayPal">
                </p>
            </label>

            <!-- Alipay Option -->
            <input type="radio" class="btn-check" name="options" id="addons5" value="alipay" v-model="selectPaymentMethod">
            <label class="btn btn-primary w-100" for="addons5">
                <p class="mb-0">
                    <img class="payment-icon" src="@/assets/logo-alipay.png" alt="Alipay">
                </p>
            </label>
        </div>
    </div>

    <!-- Billing Details Section -->
    <div class="billing-details-container bg-white p-3 rounded">
        <div class="billing-detail grand-total">
            <p>{{ t('subtotal',['checkout']) }}</p>
            <p>A$ {{ TotalOrderPrice }}</p>
        </div>

        <!-- Display balances for specific payment methods -->
        <div class="billing-detail detail-green my-2" v-if="selectPaymentMethod === 'wallet'">
            <p>{{ t('wallet_balance',['checkout']) }}</p>
            <p>A$ {{ balance }}</p>
        </div>

        <!-- Credit Card Option -->
        <div v-if="selectPaymentMethod === 'stripe'">
            <div id="card-element" ref="cardElementRef"></div>
            <button type="button" class="btn btn-primary w-100 mt-2" @click="handleCheckOutSubmit" :disabled="!cardComplete">{{ t('continue_payment',['checkout']) }}</button>
        </div>

        <!-- Wallet Payment Option -->
        <button type="button" class="btn btn-primary w-100 mt-2" v-else-if="selectPaymentMethod === 'wallet'" @click="handleCheckOutSubmit" :disabled="TotalOrderPrice >= balance">{{ t('continue_payment',['checkout']) }}</button>

        <!-- WeChat Payment Option -->
        <button type="button" class="btn btn-primary w-100 mt-2" v-else @click="handleCheckOutSubmit">{{ t('continue_payment',['checkout']) }}</button>
    </div>
</div>

    </div>
</div>
<button type="button" ref="showFail" class="d-none" data-bs-toggle="modal" data-bs-target="#orderFailed"></button>
<button type="button" ref="showSuccess" class="d-none" data-bs-toggle="modal" data-bs-target="#orderSuccess"></button>
</template>

<style>


div#app-note {
    padding-top: 20px;
}

#app-restaurant {
    text-align: center;
    padding: 20px 0;
}

#app-restaurant textarea {
    width: 100%;
    height: 150px;
    border: 2px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    font-size: 16px;
    background-color: #f9f9f9;
    color: #333;
    resize: none;
    transition: all 0.3s ease;
}

#app-restaurant textarea:focus {
    border-color: #007BFF;
    background-color: #ffffff;
    outline: none;
}

.payment-icon {
    max-width: 30px;
    max-height: 30px;
    margin: 0 auto;
    display: block;
}
.payment-method label {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px;
}

.billing-detail p {
    font-size: 14px;
    margin-bottom: 0;
}

.billing-detail.grand-total p {
    font-weight: bold;
    font-size: 16px;
}

.billing-detail.detail-green p {
    color: green;
}

button:disabled {
    background-color: #d3d3d3;
    cursor: not-allowed;
}

button {
    transition: background-color 0.3s;
}


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

.checkout-title-card {
    display: flex;
    align-items: center;
}

.back-button {
    font-size: 28px;
    margin-right: 0.5rem;
    color: var(--card-heading-color)
}

.checkout-title-card .outlet-detail p {
    font-size: 12px;
}

.store-n-diliveri {
    /* display: flex; */

}

.order-type-container button {
    width: 50%;
    font-size: 1rem;
}

.order-type-container button span:nth-child(2) {
    /* font-size: 12px; */
}

/* ------------------- addresss setion ----------------- */

.no-address-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.no-address {
    display: flex;
    align-items: center;
    color: var(--card-heading-color);
    gap: 1rem;
}

.no-address-container a {
    color: var(--order-background-color);
}

.no-address i {
    color: var(--dark-brown-color);
    font-size: 20px;
}

.address-name {
    font-size: 16px;
    font-weight: 600;
    color: var(--card-heading-color);
}

.address-description {
    font-size: 14px;
    color: var(--card-location-color);
}

.address-radio {
    display: flex;
    align-items: flex-start;
    flex-wrap: wrap;
    row-gap: 1rem;
}

.address-radio .btn-check:checked+.btn {
    background-color: white;
    margin-right: 1rem;
    text-align: left;
    border-color: var(--dark-brown-color);
}

.address-radio .btn-check+.btn {
    background-color: white;
    margin-right: 1rem;
    text-align: left;
    border: 2px solid var(--body-color);
}

.add-addrss-button {
    padding: 16px 16px;
    height: 100%;
    width: fit-content;
    text-align: center;
    background-color: var(--order-background-color);
    /* text-align:left; */
    border: 2px solid var(--order-background-color);
    color: white;
    display: flex;
    gap: 10px;
    height: 100%;
    font-size: 1rem;
    border-radius: 0.375rem;
}

a.add-addrss-button {
    cursor: pointer;
}

.Item-for-checkout {
    display: flex;
    align-items: start;
    justify-content: space-between;
    /* margin-bottom: 1rem; */
    padding: 1rem 0;
    border-bottom: 1px dashed var(--divider-color);
}

.price-n-item-option {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.offer-card-container {}

.coupon-card {
    padding: 10px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
}

.coupon-card .coupon-icon {
    color: var(--dark-brown-color);
}

.coupon-description {
    display: block;
    font-size: 10px;
    column-rule-color: var(--card-location-color);
}

.coupon-content {
    font-size: 12px;
}

.apply-coupon {
    color: var(--order-background-color);
    font-size: 12px
}

.delivery-option {
    display: flex;
    align-items: center;
    gap: 10px;
}

.delivery-option .btn-check:checked+.btn {
    background-color: var(--order-background-color);
    border-color: var(--order-background-color);
    color: white;
}

.delivery-option .btn-check:checked+.btn:hover {
    background-color: var(--order-background-color);
    border-color: var(--order-background-color);
    color: white;
}

.delivery-option .btn-check+.btn {
    background-color: transparent;
    color: var(--order-background-color);
    border-color: var(--order-background-color);
    padding: 0.75rem 2rem;
    border-radius: 10px;
    width: 100%;
}

.delivery-option .btn-check+.btn:hover {
    background-color: var(--order-background-color);
    color: white !important;
    color: var(--order-background-color);
    border-color: var(--order-background-color);
}

.biling-details-container {}

.billing-detail {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
}

.billing-detail p {
    width: fit-content;
    color: var(--card-location-color);
    font-size: 15px;
}

.detail-green p {
    font-size: 16px;
    color: var(--dark-brown-color);
}

.grand-total {
    font-weight: bold;
    color: var(--card-heading-color);
}

.outlet-with-billing-add {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    flex-wrap: wrap;
}

.outlet-with-billing-add .billing-addshown {
    padding: 0.5rem;
}

.outlet-with-billing-add .billing-addshown p {
    font-size: 12px;
    font-weight: 600;
    color: var(--card-location-color);
    margin-bottom: 0;

}

.outlet-with-billing-add .billing-addshown h6 {
    font-size: 14px;
    color: var(--card-heading-color);

}

.payment-method {
    display: flex;
}

.payment-method .btn-check+.btn {
    width: fit-content !important;
    padding: 2px 10px !important;
    height: 36px;
    color: #d2d2d2 !important;
}

.payment-method .btn-check:checked+.btn {
    width: fit-content !important;
    background-color: #d2d2d2 !important;
    border: 2px solid #d2d2d2 !important;
    color: var(--card-heading-color) !important;
    padding: 2px 10px !important;
    height: 36px;
}

.btn-primary:disabled {
  background-color: var(--light-green-color) !important;
  border: 1px solid var(--light-green-color);
}
.btn-primary:disabled:hover {
  background-color: var(--light-green-color) !important;
}

@media screen and (max-width:767.91px) {

    .address-radio .btn-check:checked+.btn {
        width: 100%;
    }

    .address-radio .btn-check+.btn {
        width: 100%;
    }

    .price-n-item-option {
        flex-direction: column;
    }

    .Item-for-checkout {
        align-items: flex-start;
    }

}
</style>
