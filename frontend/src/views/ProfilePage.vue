<script>
import { storeToRefs } from "pinia";
import { onMounted, ref, nextTick } from "vue";
import { useWalletStore } from "@/stores/wallet";
import axios from "../../axios";
import { stripePromise } from "@/stripe.js";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { useOrderStore } from "@/stores/order";
import { useTranslationStore } from "@/stores/translation";

export default {
  name: "ProfilePage",
  setup() {
    const walletStore = useWalletStore();
    const authStore = useAuthStore();
    const orderStore = useOrderStore();
    const translationStore = useTranslationStore();

    const { balance, transactions } = storeToRefs(walletStore);
    const { orders } = storeToRefs(orderStore);

    const { fullName, email, phoneNumber, profileImage, user } =
      storeToRefs(authStore);

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
    const profile_save_success = ref(null);
    const profile_save_error = ref(null);

    const initializeStripe = async () => {
      stripe.value = await stripePromise;
      elements.value = stripe.value.elements();
      cardElement.value = elements.value.create("card");

      if (cardElementRef.value) {
        cardElement.value.mount(cardElementRef.value);
      } else {
        console.error("cardElementRef is null");
      }
    };

    const rechargeValidation = () => {
      if (rechargeAmount.value > 0) {
        return false;
      }
      return true;
    };

    const handleRechargeClick = async () => {
      try {
        const response = await axios.post("/transactions/wallet/recharge/", {
          amount: rechargeAmount.value,
        });
        const { order_id, client_secret } = response.data;

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
          alert("Payment failed: " + result.error.message);
        } else {
          if (result.paymentIntent.status === "succeeded") {
            // Payment succeeded
            alert("Payment successful!");
            router.push({
              name: "OrderConfirmation",
              params: {
                orderId: order_id,
              },
            });
          }
        }
      } catch (error) {
        console.error("Error during checkout:", error.response || error);
        alert(
          "An error occurred during checkout: " +
            (error.response?.data?.detail || error.message)
        );
      }
    };

    const passwordChangeValidation = () => {
      if (
        !old_password.value ||
        !new_password.value ||
        !confirm_password.value
      ) {
        password_change_error.value = "All fields are mandatory";
        return false;
      }
      if (new_password.value !== confirm_password.value) {
        password_change_error.value = "Confirm Password doesn't match";
        return false;
      }
      return true;
    };

    const handlePasswordChange = async () => {
      password_change_error.value = null;
      if (!passwordChangeValidation()) {
        return;
      }
      const payload = {
        old_password: old_password.value,
        new_password: new_password.value,
        confirm_password: confirm_password.value,
      };
      try {
        await authStore.handlePasswordChange(payload);
        password_change_success.value = "Password Successfully Changed";
        resetPasswordChange();
      } catch (error) {
        if (error.response && error.response.data) {
          password_change_error.value = JSON.stringify(
            error.response.data.error
          );
        } else {
          password_change_error.value =
            "An unexpected error occurred. Please try again.";
        }
      }
    };

    const resetPasswordChange = () => {
      new_password.value = null;
      old_password.value = null;
      confirm_password.value = null;
    };

    function goBack() {
      router.go(-1);
    }

    const onImageChange = (event) => {
      const file = event.target.files[0];
      if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = (e) => {
          authStore.setProfileImage(e.target.result);
        };
        reader.readAsDataURL(file);
      } else {
        alert("Please select a valid image file.");
      }
    };

    const handleSave = async () => {
        profile_save_success.value = "";
        profile_save_error.value = "";
      try {
        if (fullName.value) {
          await authStore.saveProfile();
          profile_save_success.value = "Profile saved successfully !!"
        } else {
          profile_save_error.value = "Full name is required";
        }
      } catch (error) {
        console.log(error);
        profile_save_error.value = toString(error);
      }
    };

    const getProfileImage = () => {
        console.log(profileImage)
        console.log(user.profile)
      if (profileImage.value) {
        return profileImage.value;
        
      } else if (user.value && user.value.profile && user.value.profile.user_image) {
        const baseURL = process.env.VUE_APP_back_URL;
        return baseURL + user.value.profile.user_image;
      } else {
        return "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png";
      }
    };

    const t = (label, modules) => {
      return translationStore.translate(label, modules);
    };

    onMounted(async () => {
      await nextTick();
      initializeStripe();
      walletStore.fetchTransactions();
      authStore.initializeProfile();
      orderStore.fetchOrders();
    });

    return {
      t,
      orders,
      profileImage,
      getProfileImage,
      goBack,
      balance,
      user,
      fullName,
      handleSave,
      onImageChange,
      email,
      phoneNumber,
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
      profile_save_success,
      profile_save_error,
    };
  },
};
</script>

<template>
  <div class="main-layout mb-5">
    <div class="profile-heading">
      <!-- <h2>Profile</h2> -->
    </div>
    <div class="profile-text-wrap">
      <div class="d-flex gap-3">
        <div class="profile-form w-100">
          <div class="profile-form-wrap-content">
            <div class="profile-form-heading">
              <!-- <h4 class="form-heading">Personal Detail</h4> -->

              <ul class="nav nav-tabs" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link active"
                    id="home-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#home-tab-pane"
                    type="button"
                    role="tab"
                    aria-controls="home-tab-pane"
                    aria-selected="true"
                  >
                   {{ t('change_password', ['profile'])}}
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    id="ewallet-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#ewallet-tab-pane"
                    type="button"
                    role="tab"
                    aria-controls="ewallet-tab-pane"
                    aria-selected="false"
                  >
                  {{ t('wallet', ['profile'])}}
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    id="ewallethistory-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#ewallethistory-tab-pane"
                    type="button"
                    role="tab"
                    aria-controls="ewallethistory-tab-pane"
                    aria-selected="false"
                  >
                  {{ t('wallet_history', ['profile'])}}
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    id="orderhistory-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#orderhistory-tab-pane"
                    type="button"
                    role="tab"
                    aria-controls="profile-tab-pane"
                    aria-selected="false"
                  >
                  {{ t('order_history', ['profile'])}}
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    id="changepassword-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#changepassword-tab-pane"
                    type="button"
                    role="tab"
                    aria-controls="changepassword-tab-pane"
                    aria-selected="false"
                  >
                  {{ t('change_password', ['profile'])}}
                  </button>
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
                            <!-- Dummy image shown initially -->
                            <img
                              id="profileImg"
                              :src="getProfileImage()"
                              alt="Profile Picture"
                            />
                          </div>
                          <label for="fileInput" class="edit-icon">
                            <i class="fa fa-pencil-alt"></i>
                            <!-- Pencil icon for editing -->
                          </label>
                          <input
                            type="file"
                            id="fileInput"
                            class="file-input"
                            @change="onImageChange"
                            accept="image/*"
                          />
                        </div>
                        <div>
                            <div class="alert alert-success" role="alert" v-if="profile_save_success">
                            {{ profile_save_success }}
                            </div>
                            <div class="alert alert-danger" role="alert" v-if="profile_save_error">
                            {{profile_save_error}}
                            </div>

                        </div>
                      </div>

                      <div class="col-md-6 p-2">
                        <div
                          class="input-wrap-withouticon password-bottom-space"
                        >
                          <!-- <label>Company Name</label> -->
                          <label class="form-label">{{ t('email_address', ['profile'])}}</label>
                          <input
                            type="text"
                            name="email"
                            class="form-control"
                            placeholder="Enter Email Address"
                            v-model="email"
                            disabled
                          />
                        </div>
                      </div>
                      <div class="col-md-6 p-2">
                        <div
                          class="input-wrap-withouticon password-bottom-space"
                        >
                          <!-- <label>Company Name</label> -->
                          <label
                            for="exampleFormControlInput1"
                            class="form-label"
                            >{{ t('phone_number', ['profile'])}}</label
                          >
                          <input
                            type="text"
                            name="username"
                            class="form-control"
                            placeholder="Enter Phone Number"
                            v-model="phoneNumber"
                            disabled
                          />
                        </div>
                      </div>
                    </div>
                    <div class="col-md-8 p-2">
                      <div class="input-wrap-withouticon password-bottom-space">
                        <!-- <label>Company Name</label> -->
                        <label for="exampleFormControlInput1" class="form-label"
                          >{{ t('full_name', ['profile'])}}</label
                        >
                        <input
                          type="text"
                          name="firstname"
                          class="form-control"
                          placeholder="Enter Full Name"
                          v-model="fullName"
                        />
                      </div>
                    </div>
                    <div class="footer-button p-0 pt-3">
                      <button
                        class="btn btn-secondary sm"
                        style="background-color: #1d0b00"
                        @click="goBack"
                      >
                      {{ t('back', ['profile'])}}
                      </button>
                      <a class="btn btn-primary sm" @click="handleSave">{{ t('save', ['profile'])}}</a>
                    </div>
                  </div>
                </div>
                <div
                  class="tab-pane ewallet-tab fade"
                  id="ewallet-tab-pane"
                  role="tabpanel"
                  aria-labelledby="ewallet-tab"
                  tabindex="0"
                >
                  <div class="e-wallet bg-white rounded row p-3 mb-0">
                    <div
                      class="col-md-6 border wallet-container text-center p-3"
                    >
                      <div class="amount-box text-center p-3">
                        <div class="wallet-icon">
                          <i class="fa-solid fa-wallet"></i>
                        </div>
                        <p>{{ t('total_balance', ['profile'])}}</p>
                        <p class="amount">A$ {{ balance }}</p>
                      </div>
                    </div>
                    <div class="col-md-6 p-3 mb-3">
                      <label for="formGroupExampleInput" class="form-label"
                        >{{ t('add_amount_in_wallet', ['profile'])}}</label
                      >
                      <input
                        type="number mb-3"
                        class="form-control"
                        id="formGroupExampleInput"
                        placeholder="A$100"
                        v-model="rechargeAmount"
                      />
                      <label for="card-element" class="form-label"
                        >{{ t('enter_card_details', ['profile'])}}</label
                      >
                      <div id="card-element" ref="cardElementRef"></div>
                      <button
                        type="button"
                        class="mt-3 btn btn-primary"
                        :disabled="rechargeValidation()"
                        @click="handleRechargeClick"
                      >
                      {{ t('add_to_wallet', ['profile'])}}
                      </button>
                    </div>
                  </div>
                </div>
                <div
                  class="tab-pane ewallethistory-tab fade"
                  id="ewallethistory-tab-pane"
                  role="tabpanel"
                  aria-labelledby="ewallethistory-tab"
                  tabindex="0"
                >
                  <div class="e-wallet bg-white rounded mb-3">
                    <div class="wallet-container text-center">
                      <div class="txn-history">
                        <div class="wallet-section">
                          <!-- Wallet History Section -->
                          <div class="section wallet-history">
                            <h2>{{ t('wallet_history', ['profile'])}}</h2>
                            <!-- Wallet History -->
                            <div
                              v-for="txn in transactions"
                              :key="txn.id"
                              class="transaction"
                              :class="
                                txn.order_type === 'WALLET_RECHARGE'
                                  ? 'credit'
                                  : 'debit'
                              "
                            >
                              <div class="left">
                                <p>
                                  <span>Transaction ID:</span>
                                  {{ txn.transation_id }}
                                </p>
                                <p>
                                  <span>Operation Type:</span>
                                  {{ txn.order_type }}
                                </p>
                                <p class="text-danger">
                                  <span>Payment Status:</span> {{ txn.status }}
                                </p>
                                <p>
                                  <span>Date & Time:</span> 12 Dec 2024 10:30
                                </p>
                              </div>
                              <span class="payment-platform">{{
                                txn.transaction_from
                              }}</span>
                              <div class="amount">
                                {{
                                  txn.order_type === "WALLET_RECHARGE"
                                    ? "+"
                                    : "-"
                                }}
                                A${{ txn.amount }}
                              </div>
                            </div>
                          </div>
                        </div>
                        <p class="txn-list" v-if="!transactions">
                          No Transactions to display
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="tab-pane orderhistory-settings fade"
                  id="orderhistory-tab-pane"
                  role="tabpanel"
                  aria-labelledby="orderhistory-tab"
                  tabindex="0"
                >
                  <div
                    class="store-n-diliveri order-history bg-white rounded mb-3"
                  >
                    <div class="order-history">
                      <!-- Order Card 1 -->
                      <div class="order-card" v-for="order in orders" :key="order.id" >
                        <div class="order-header">
                          <div class="delivery">{{order.order_type}}</div>
                          <div class="status">{{ order.status }}</div>
                        </div>
                        <div class="order-details">
                          Order {{ order.order_id}} <br />
                          {{order.order_time}}
                        </div>
                        <div class="order-item" v-for="item in JSON.parse(order.menu_item)" :key="item.id">
                          <img
                            src="https://img.icons8.com/color/48/000000/checked--v1.png"
                            alt="Item Icon"
                          />
                          <span>{{item.meal_name}}</span>
                        </div>
                        <div class="order-footer">
                          <div class="price">A$ {{ order.total_price }}</div>
                          <div>
                            <button data-bs-toggle="modal" data-bs-target="orderDetails" class="orderdetails-btn mx-2" disabled>Details</button>
                            <button class="reorder-btn" @click="handleReOrder(order)" disabled >Reorder</button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="tab-pane changepassword-settings fade"
                  id="changepassword-tab-pane"
                  role="tabpanel"
                  aria-labelledby="changepassword-tab"
                  tabindex="0"
                >
                  <div class="row">
                    <div
                      class="alert alert-danger"
                      role="alert"
                      v-if="password_change_error"
                    >
                      {{ password_change_error }}
                    </div>
                    <div
                      class="alert alert-success"
                      role="alert"
                      v-if="password_change_success"
                    >
                      {{ password_change_success }}
                    </div>
                    <div class="col-md-12 p-2">
                      <div class="input-wrap-withouticon password-bottom-space">
                        <label for="oldpassword" class="form-label"
                          >{{ t('old_password', ['profile'])}}</label
                        >
                        <input
                          id="oldpassword"
                          type="password"
                          name="old_password"
                          v-model="old_password"
                          class="form-control"
                          placeholder="Enter old password"
                        />
                      </div>
                    </div>

                    <div class="col-md-12 p-2">
                      <div class="input-wrap-withouticon password-bottom-space">
                        <label for="newpassword" class="form-label"
                          >{{ t('new_password', ['profile'])}}</label
                        >
                        <input
                          id="newpassword"
                          type="password"
                          name="new_password"
                          v-model="new_password"
                          class="form-control"
                          placeholder="Enter new password"
                        />
                      </div>
                    </div>

                    <div class="col-md-12 p-2">
                      <div class="input-wrap-withouticon password-bottom-space">
                        <!-- <label>Company Name</label> -->
                        <label for="exampleFormControlInput1" class="form-label"
                          >{{ t('confirm_password', ['profile'])}}</label
                        >
                        <input
                          type="password"
                          name="confirm_password"
                          v-model="confirm_password"
                          class="form-control"
                          placeholder="Enter new password again"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="footer-button">
                    <a class="btn btn-primary sm" @click="handlePasswordChange"
                      >{{ t('change_password', ['profile'])}}</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* -----------profile-------------- */

.wallet-history h2 {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 15px;
}
.transaction {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 15px;
  background-color: #f4f8fb;
}
.transaction .left {
  flex: 1;
}
.transaction .left p {
  margin: 5px 0;
  font-size: 14px;
  color: #555;
}
.transaction .left span {
  font-weight: bold;
  color: #333;
}
.transaction .payment-platform {
  font-size: 14px;
  font-weight: bold;
  padding: 6px 12px;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
}
.transaction .amount {
  font-size: 16px;
  font-weight: bold;
}
.transaction.credit .amount {
  color: #28a745;
}
.transaction.debit .amount {
  color: #dc3545;
}

.order-details-container {
  max-width: 600px;
  margin: 20px auto;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.header {
  display: flex;
  justify-content: space-between;
  padding: 15px;
  align-items: center;
  border-bottom: 1px solid #ddd;
}
.header .title {
  font-size: 18px;
  font-weight: bold;
}
.header .help {
  color: #007bff;
  font-size: 14px;
  cursor: pointer;
}
.address-section {
  padding: 15px;
  border-bottom: 1px solid #ddd;
}
.address-section h3 {
  margin: 0;
  font-size: 16px;
  font-weight: bold;
  color: #333;
}
.address-section p {
  margin: 5px 0;
  font-size: 14px;
  color: #555;
}
.status-section {
  display: flex;
  align-items: center;
  padding: 15px;
  background-color: #f4f8fb;
  border-bottom: 1px solid #ddd;
}
.status-section img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
.status-section .status-text {
  font-weight: bold;
  color: #333;
}
.status-section .status-date {
  font-size: 14px;
  color: #555;
}
.order-summary {
  padding: 15px;
}
.order-summary h3 {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
.order-summary .summary-item {
  display: flex;
  justify-content: space-between;
  margin: 8px 0;
  font-size: 14px;
}
.order-summary .summary-item .bold {
  font-weight: bold;
}
.total {
  font-size: 18px;
  font-weight: bold;
  margin-top: 15px;
  text-align: right;
}

.order-history {
  max-width: 600px;
  margin: 20px auto;
}
.order-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 15px;
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
}
.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.order-header .delivery {
  font-weight: bold;
  font-size: 16px;
}
.order-header .status {
  background-color: #d4edda;
  color: #155724;
  font-size: 12px;
  padding: 3px 8px;
  border-radius: 15px;
  font-weight: bold;
  text-transform: uppercase;
}
.order-details {
  margin-bottom: 10px;
  font-size: 14px;
  color: #666;
}
.order-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.order-item img {
  width: 16px;
  height: 16px;
  margin-right: 8px;
}
.order-item span {
  font-weight: bold;
  font-size: 14px;
  color: #333;
}
.order-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.price {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}
.reorder-btn {
  background-color: #944c22;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
}
.reorder-btn:hover {
  background-color: #c82333;
}

.orderdetails-btn {
  background-color: #944c22;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
}
.orderdetails-btn:hover {
  background-color: #0D6EFD;
}

.profile-heading {
  margin: 16px 88px;
  /* background: linear-gradient(9deg, rgb(197 93 33) 0%, rgba(137, 65, 24, 1) 55%); */
  background-image: linear-gradient(
      45deg,
      rgba(22, 22, 22, 0.5),
      rgba(33, 38, 43, 0.5)
    ),
    url("@/assets/about-banner.png");
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
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: repeating-linear-gradient(
    328deg,
    rgba(255, 255, 255, 0.06),
    rgba(255, 255, 255, 0.06) 20px,
    rgba(255, 255, 255, 0) 20px,
    rgba(255, 255, 255, 0) 40px
  );
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

.meal-addons .btn-check:checked + .btn {
  background-color: var(--light-brown-color);
  border: 2px solid var(--dark-brown-color);
  color: var(--card-heading-color);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.meal-addons .btn-check + .btn {
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

@media screen and (max-width: 768px) {
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

@media screen and (max-width: 575px) {
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
