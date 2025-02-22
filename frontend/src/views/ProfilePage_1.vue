<script>
import {
    storeToRefs
} from 'pinia';
import {
    onMounted,
    ref,
    nextTick
} from 'vue';
import {
    useWalletStore
} from '@/stores/wallet';
import axios from '../../axios';
import {
    stripePromise
} from '@/stripe.js';
import {
    useRouter
} from 'vue-router';
import {
    useAuthStore
} from '@/stores/auth';

export default {
    name: 'ProfilePage',
    setup() {
        const walletStore = useWalletStore();
        const authStore = useAuthStore();

        const {
            balance,
            transactions
        } = storeToRefs(walletStore);

        const { profileImage } = storeToRefs(authStore);

        const router = useRouter();

        //Wallet Recharge
        const rechargeAmount = ref(0);
        const stripe = ref(null);
        const elements = ref(null);
        const cardElement = ref(null);
        const cardElementRef = ref(null);

        //Password Change
        const old_password = ref(null);
        const new_password = ref(null);
        const confirm_password = ref(null);
        const password_change_error = ref(null);
        const password_change_success = ref(null);

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

        const rechargeValidation = () => {
            if (rechargeAmount.value > 0) {
                return false;
            }
            return true;
        }

        const handleRechargeClick = async () => {
            try {
                const response = await axios.post('/transactions/wallet/recharge/', {
                    amount: rechargeAmount.value
                });
                const {
                    order_id,
                    client_secret
                } = response.data;

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
                        router.push({
                            name: 'OrderConfirmation',
                            params: {
                                orderId: order_id
                            }
                        });
                    }
                }
            } catch (error) {
                console.error('Error during checkout:', error.response || error);
                alert('An error occurred during checkout: ' + (error.response?.data?.detail || error.message));
            }
        }

        const passwordChangeValidation = () => {
            if (!old_password.value || !new_password.value || !confirm_password.value) {
                password_change_error.value = "All fields are mandatory"
                return false;
            }
            if (new_password.value !== confirm_password.value) {
                password_change_error.value = "Confirm Password doesn't match"
                return false;
            }
            return true;
        }

        const handlePasswordChange = async () => {
            password_change_error.value = null
            if (!passwordChangeValidation()) {
                return;
            }
            const payload = {
                old_password: old_password.value,
                new_password: new_password.value,
                confirm_password: confirm_password.value
            }
            try {
                await authStore.handlePasswordChange(payload)
                password_change_success.value = "Password Successfully Changed"
                resetPasswordChange();
            } catch (error) {
                if (error.response && error.response.data ) {
                    password_change_error.value = JSON.stringify(error.response.data.error);
                } else {
                    password_change_error.value = 'An unexpected error occurred. Please try again.';
                }
            }
        }

        const resetPasswordChange = () => {
            new_password.value = null;
            old_password.value = null;
            confirm_password.value = null;
        }
      

        const onImageChange = (event) => {
        const file = event.target.files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
            authStore.setProfileImage(e.target.result);
            // Optionally, upload the image to the server here
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please select a valid image file.');
        }
        };

        const saveProfile = () => {
        // Add form validation here if needed
        authStore.saveProfile();
        };



        onMounted(async () => {
            await nextTick();
            initializeStripe();
            walletStore.fetchTransactions()
        });

        return {
            balance,
            transactions,
            cardElementRef,
            rechargeAmount,
            rechargeValidation,
            handleRechargeClick,
            old_password,
            new_password,
            confirm_password,
            password_change_error,
            passwordChangeValidation,
            handlePasswordChange,
            password_change_success,
            authStore,
            textFields,
            onImageChange,
            profileImage,
            saveProfile,
        }
    }
}
</script>

<template>
<div class="main-layout mb-5">
    <div class="profile-heading">
        <!-- <h2>Profile</h2> -->
    </div>
    <div class="profile-text-wrap">
        <div class="d-flex  gap-3">
            <div class="profile-form w-100">
                <div class="profile-form-wrap-content">
                    <div class="profile-form-heading">
                        <!-- <h4 class="form-heading">Personal Detail</h4> -->

                        <ul class="nav nav-tabs" id="myTab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Personal Detail</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="ewallet-tab" data-bs-toggle="tab" data-bs-target="#ewallet-tab-pane" type="button" role="tab" aria-controls="ewallet-tab-pane" aria-selected="false">Wallet</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="ewallethistory-tab" data-bs-toggle="tab" data-bs-target="#ewallethistory-tab-pane" type="button" role="tab" aria-controls="ewallethistory-tab-pane" aria-selected="false">Wallet History</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="orderhistory-tab" data-bs-toggle="tab" data-bs-target="#orderhistory-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Order History</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="changepassword-tab" data-bs-toggle="tab" data-bs-target="#changepassword-tab-pane" type="button" role="tab" aria-controls="changepassword-tab-pane" aria-selected="false">Change Password</button>
                            </li>
                        </ul>

                    </div>

                    <div class="form-input-wrap">

                        <div class="tab-content" id="myTabContent">
                            <div
                            class="tab-pane profile-settings fade show active"
                            id="home-tab-pane"
                            role="tabpanel"
                            aria-labelledby="home-tab"
                            tabindex="0"
                            >
                            <div class="input-wrap">
                                <div class="row m-0">
                                <div class="col-md-12">
                                    <div class="profile-img-container">
                                    <div class="profile-img">
                                        <!-- Profile Image -->
                                        <img :src="profileImage" alt="Profile Picture">
                                    </div>
                                    <label for="fileInput" class="edit-icon">
                                        <i class="fa fa-pencil-alt"></i> <!-- Pencil icon for editing -->
                                    </label>
                                    <input
                                        type="file"
                                        id="fileInput"
                                        class="file-input"
                                        accept="image/*"
                                        @change="onImageChange"
                                    />
                                    </div>
                                </div>

                                <div class="col-md-6 p-2" v-for="field in textFields" :key="field.id">
                                    <div class="input-wrap-withouticon password-bottom-space">
                                    <label :for="field.id" class="form-label">{{ field.label }}</label>
                                    <input
                                        :type="field.type"
                                        :name="field.name"
                                        class="form-control"
                                        :placeholder="field.placeholder"
                                        v-model="authStore[field.model]"
                                        :disabled="field.disabled"
                                    />
                                    </div>
                                </div>

                               
                                </div>
                                <div class="footer-button p-0 pt-3">
                                <!-- <button @click="goBack" class="btn btn-secondary sm" style="background-color: #1d0b00;">Back</button> -->
                                <button @click="saveProfile" class="btn btn-primary sm">Save</button>
                                </div>
                            </div>
                            </div>
                        </div>
                            <div class="tab-pane ewallethistory-tab fade" id="ewallethistory-tab-pane" role="tabpanel" aria-labelledby="ewallethistory-tab" tabindex="0">
                                <div class="e-wallet bg-white rounded mb-3">
                                    <div class="wallet-container text-center">
                                        <div class="txn-history">
                                            <p class=""><b>Paymeny History</b></p>
                                            <p class="txn-list" v-for="transaction in transactions" :key="transaction.id">
                                                {{ transaction.transaction_id }}
                                                <span class="credit-amount" v-if="transaction.order_type=='WALLET_RECHARGE'">+A${{ transaction.amount }}</span>
                                                <span class="debit-amount" v-else>-${{ transaction.amount }}</span>
                                            </p>
                                            <p class="txn-list" v-if="!transactions">No Transactions to display</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane orderhistory-settings fade" id="orderhistory-tab-pane" role="tabpanel" aria-labelledby="orderhistory-tab" tabindex="0">
                                <div class="store-n-diliveri order-history bg-white  rounded mb-3">
                                    <ul class="list-unstyled mb-0">

                                        <!-- History of order item -->
                                        <li class="Item-for-checkout" type="button" data-bs-toggle="modal" data-bs-target="#orderhistorydetailModal">
                                            <div class="order-item">
                                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                                <p class="mb-0">3 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts 1</p>
                                                <p class="mb-0">2<span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts 2</p>
                                            </div>
                                            <div class="price-n-item-option">
                                                <p class="mb-0 ">2nd june 2024 </p>
                                                <p class="mb-0 w-100 overall-price fw-bold fs-5 ">$ 20 </p>
                                                <div class="payment-type-history">
                                                    <p class="mb-0">Payment Type </p>
                                                    <p class="payment-portal mb-0"> Payment Portal Name</p>
                                                </div>

                                            </div>
                                        </li>

                                    </ul>

                                    <!-- ---- addons ---------------------- -->
                                    <!-- <div class=" py-2">
                                <h4 class="extra-status"> Extra Add-ons : <span  class="text-status"> Meal Set </span> </h4>
                                <div class="meal-addons rounded ">
                                    <input type="checkbox" class="btn-check" name="options" id="addons1">
                                    <label class="btn btn-primary w-100" for="addons1">
                                        <p class="mb-0">
                                            Extra Protein
                                        </p>
                                        <p class="mb-0">
                                            $ 20
                                        </p>
                                    </label>

                                    <input type="checkbox" class="btn-check" name="options" id="addons2">
                                    <label class="btn btn-primary w-100" for="addons2">
                                        <p class="mb-0">
                                            Extra Vagetables
                                        </p>
                                        <p class="mb-0">
                                            $ 20
                                        </p> 
                                    </label>

                                    <input type="checkbox" class="btn-check" name="options" id="addons3">
                                    <label class="btn btn-primary w-100" for="addons3">
                                        <p class="mb-0">
                                            Extra Rice
                                        </p>
                                        <p class="mb-0">
                                            $ 20
                                        </p> 
                                    </label>
                                </div>
                               
                            </div> -->

                                </div>
                            </div>
                            <div class="tab-pane changepassword-settings fade" id="changepassword-tab-pane" role="tabpanel" aria-labelledby="changepassword-tab" tabindex="0">
                                <div class="row">
                                    <div class="alert alert-danger" role="alert" v-if="password_change_error">
                                        {{ password_change_error }}
                                    </div>
                                    <div class="alert alert-success" role="alert" v-if="password_change_success">
                                        {{ password_change_success }}
                                    </div>
                                    <div class="col-md-12 p-2">
                                        <div class="input-wrap-withouticon password-bottom-space">
                                            <label for="oldpassword" class="form-label">Old Password</label>
                                            <input id="oldpassword" type="password" name="old_password" v-model="old_password" class="form-control" placeholder="Enter old password" />
                                        </div>
                                    </div>

                                    <div class="col-md-12 p-2">
                                        <div class="input-wrap-withouticon password-bottom-space">
                                            <label for="newpassword" class="form-label">New Password</label>
                                            <input id="newpassword" type="password" name="new_password" v-model="new_password" class="form-control" placeholder="Enter new password" />
                                        </div>
                                    </div>

                                    <div class="col-md-12 p-2">
                                        <div class="input-wrap-withouticon password-bottom-space">
                                            <!-- <label>Company Name</label> -->
                                            <label for="exampleFormControlInput1" class="form-label">Confirm Password</label>
                                            <input type="password" name="confirm_password" v-model="confirm_password" class="form-control" placeholder="Enter new password again" />
                                        </div>
                                    </div>

                                </div>
                                <div class="footer-button">
                                    <a class="btn btn-primary sm" @click="handlePasswordChange">Change Password</a>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </div>

<!-- order detail popup -->
<div class="modal modal-food-item fade" id="orderhistorydetailModal" tabindex="-1" aria-labelledby="orderhistorydetailModalLabel" aria-hidden="true">
    <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Order History Detail</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="store-n-diliveri bg-white p-3 rounded mb-3">
                    <ul class="list-unstyled mb-0">

                        <!-- History of order item -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">

                                <p class="mb-0">2nd june 2024 </p>
                            </div>
                        </li>

                        <!-- History of order item -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">

                                <p class="mb-0">2nd june 2024 </p>
                            </div>
                        </li>

                        <!-- History of order item -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <p class="mb-0">2nd june 2024 </p>
                            </div>
                        </li>

                        <!-- History of order item -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">
                                <p class="mb-0">2nd june 2024 </p>
                            </div>
                        </li>

                        <!-- History of order item -->
                        <li class="Item-for-checkout">
                            <div>
                                <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                <p class="item-type-hd mb-0">Extra Protein</p>
                                <p class="item-type-hd mb-0">Extra Vegetable</p>
                                <p class="item-type-hd mb-0">Extra Rice</p>
                            </div>
                            <div class="price-n-item-option">

                                <p class="mb-0">2nd june 2024 </p>
                            </div>
                        </li>
                    </ul>
                </div>

            </div>
        </div>
    </div>
</div>
</template>

<style>
/* -----------profile-------------- */

.profile-heading {
    margin: 16px 88px;
    /* background: linear-gradient(9deg, rgb(197 93 33) 0%, rgba(137, 65, 24, 1) 55%); */
    background-image: linear-gradient(45deg, rgba(22, 22, 22, 0.5), rgba(33, 38, 43, 0.5)), url('@/assets/about-banner.png');
    background-size: cover;
    border-radius: 8px;
    padding: 16px;
    height: 200px;
    position: relative;
    padding-left: 30px;
    display: flex;
}

.billing-content-wrap {
    min-height: 70vh;
}

.profile-heading::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: repeating-linear-gradient(328deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.06) 20px, rgba(255, 255, 255, 0) 20px, rgba(255, 255, 255, 0) 40px);
    background-size: 200% 100%;
    opacity: 0.3;
    pointer-events: none;
    background-position: left;
}

.profile-heading h2 {
    color: #fff;
    font-weight: 400 !important;
    margin-top: 8px;
    font-size: 30px !important;
}

.profile-text-wrap {
    background-color: #ffffff;
    /* padding: 16px; */
    margin: -174px 118px 0;
    position: relative;
    border-radius: 8px;
}

.profile-settings {
    min-height: 50vh;
}

.profile-side-bar {
    width: 250px;
    border: 1px solid #ffe0ce;
    /* height: calc(100vh - 143px); */
    padding: 16px 0;
    border-radius: 8px;
    overflow-y: auto;
}

.profile-form {
    width: calc(100% - 250px);
    border: 1px solid #d2d2d2;
    border-radius: 8px;
    /* height: calc(100vh - 143px); */
    overflow: hidden;
}

.profile-side-bar ul {
    display: flex;
    align-items: left;
    flex-direction: column;
    height: auto;
    list-style-type: none;
    gap: 15px;
    margin-bottom: 30px;
}

.profile-side-bar ul li {
    padding: 0 16px;
}

.profile-side-bar a.active {
    background: linear-gradient(9deg, rgb(197 93 33) 0%, #894118 55%);
    color: #fff;
    border-radius: 6px;
}

.profile-side-bar ul a {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    padding: 12px 16px;
    color: #894118;
}

.profile-form-heading {
    padding-top: 16px;
    border-bottom: 1px solid #ffe0ce;
}

.profile-form-wrap-content .form-input-wrap {
    min-height: 50vh;
}

.form-input-wrap {
    padding: 16px;
    overflow-y: auto;
    /* height: calc(100vh - 145px); */
}

.footer-button {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 16px;
    border-top: 1px solid #ffe0ce;
    /* position: sticky; */
    /* bottom: 0; */
    width: 100%;
    gap: 8px;
    background-color: #fff;
}

.profile-img-container {
    position: relative;
    width: 200px;
    height: 147px;
    text-align: center;
}

/* Profile image styles */
.profile-img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid white;
}

.profile-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Edit icon */
.edit-icon {
    position: absolute;
    top: 9px;
    right: 60px;
    background-color: rgb(194 92 33);
    color: white;
    padding: 5px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 15px;
    transition: background-color 0.3s ease;
    width: 32px;
    height: 32px;
}

.file-input {
    display: none;
    /* Hide the file input */
}

.billing-header {
    width: 100%;
    background: #fff;
    position: sticky;
    top: 0;
    z-index: 9;
}

.billing-content-wrap {
    overflow: auto;
    height: 100%;
}

.sign-up-wrap {
    padding: 16px !important;
    background-color: #fff;
    position: sticky;
    bottom: 0;
    margin-top: 8px !important;
}

.profile-form-heading .nav-tabs .nav-link {
    color: var(----card-location-color) !important;
}

.profile-form-heading .nav-tabs .nav-link.active {
    color: white !important;
    background-color: var(--dark-brown-color);
}

.order-history {
    /* padding: 0.75rem; */
}

.order-history .Item-for-checkout {
    padding: 0.75rem;
    border-radius: 0.5rem;
    border: 1px solid #d2d2d2;
    margin-bottom: 10px;
}

.order-history .order-item {
    flex-direction: column;
    border: none;
    margin-bottom: 0;
    padding: 0;
}

.order-history .order-item p {
    color: var(--card-location-color);
}

.order-history .Item-for-checkout .price-n-item-option {
    flex-direction: column;
    justify-content: flex-end;
    gap: 0;
}

.meal-addons {
    gap: 10px;
    width: 100%;
}

.meal-addons .btn-check:checked+.btn {
    background-color: var(--light-brown-color);
    border: 2px solid var(--dark-brown-color);
    color: var(--card-heading-color);
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
}

.meal-addons .btn-check+.btn {
    background-color: white;
    border: 1px solid var(--card-location-color);
    color: var(--card-heading-color);
    width: 100%;
    justify-content: space-between;
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 1rem;
}

.price-n-item-option {
    text-align: left;
}

.price-n-item-option .payment-type-history {
    padding-top: 0.5rem;
    bottom: 1px solid #d2d2d2;
    width: 100%;
}

.price-n-item-option .payment-type-history p {
    color: var(--card-location-color);
    font-size: 12px;
    text-align: left;
}

.price-n-item-option .payment-type-history .payment-portal {
    font-size: 12px;
    color: var(--order-background-color);
    font-weight: 700;
}

.price-n-item-option .overall-price {
    color: var(--order-background-color);
}

/* ------------------------- e-wallet -------------------- */

.e-wallet {}

.wallet-icon i {
    font-size: 48px;
    color: var(--card-location-color);
}

.wallet-container {
    /* background: #f1f5f0; */

}

.page-title {
    text-align: left;
}

.fa-user {
    float: right;
}

.fa-align-left {
    margin-right: 15px;
}

.amount-box img {
    width: 50px;
}

.amount {
    font-size: 35px;
}

.amount-box p {
    margin-top: 10px;
    margin-bottom: -10px;
}

.btn-group {
    margin: 20px auto;
    max-width: 150px;

}

.btn-group .btn {
    /* margin: 8px; */
    /* border-radius: 20px !important; */
    font-size: 12px;
}

.txn-history {
    text-align: left;
    background-color: #d2d2d2;
    padding: 0.5rem;
    border-radius: 0.75rem;
}

.txn-list {
    background-color: #fff;
    padding: 12px 10px;
    color: #777;
    font-size: 14px;
    margin: 7px 0;
}

.debit-amount {
    color: red;
    float: right;
}

.credit-amount {
    color: green;
    float: right;

}

.footer-menu {
    margin: 20px -20px 0;
    bottom: 0;
    border-top: 1px solid #ccc;
    padding: 10px 10px 0;
}

.footer-menu p {
    font-size: 12px;
}

@media screen and (max-width: 800px) {
    .wallet-container {
        height: 115%;
        bottom: 20px;
        /* margin-top: 100px; */
    }

}

@media screen and (max-width:768px) {
    .profile-heading {
        margin: 0;
    }

    .profile-text-wrap {
        margin-left: 10px;
        margin-right: 10px;
    }

    .nav-link.active,
    .nav-link:hover {
        color: var(--dark-brown-color) !important;
    }

    .order-history .Item-for-checkout {
        flex-direction: column;
        row-gap: 1rem;
    }

    .order-history .Item-for-checkout .order-item {
        width: 100%;
    }

    .order-history .Item-for-checkout .price-n-item-option {
        width: 100%;
        border-top: 1px dashed var(--card-location-color);
        padding-top: 1rem;
    }

    .order-history .Item-for-checkout .price-n-item-option p {
        width: 100%;
        text-align: start;
    }

}

@media screen and (max-width:575px) {
    .profile-form-heading {
        padding: 10px;
        border: none;
    }

    .profile-form-heading .nav-tabs {
        display: flex;
        flex-direction: column;
    }

    .profile-form-heading .nav-tabs .nav-item .nav-link {
        width: 100%;
        border-radius: 0.5rem;
        margin-bottom: 0.25rem;
    }

    .profile-form-heading .nav-tabs .nav-item .nav-link:hover {
        width: 100%;
        color: white !important;

    }

}
</style>
