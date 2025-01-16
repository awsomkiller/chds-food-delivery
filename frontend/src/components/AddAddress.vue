<template>
    <!-- Address Modal -->
    <div
      class="modal fade"
      id="addressModal"
      tabindex="-1"
      aria-labelledby="addressModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
  
          <div class="modal-header">
            <h5 class="modal-title" id="addressModalLabel">
              {{ activeAddress.id ? 'Edit Address' : 'Add New Address' }}
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
  
          <div class="modal-body">
            <div class="login-content p-0">
              <form @submit.prevent="handleSubmit">
                <div class="form-wrap">
                  <div class="row">
                    <!-- Pincode -->
                    <div class="col-md-12">
                      <div class="mb-2">
                        <label for="postal_code" class="form-label">Postal Code</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.postal_code"
                            type="number"
                            class="form-control"
                            id="postal_code"
                            placeholder="Enter Postal Code"
                            @blur="handlePostalCodeChange"
                            required
                          />
                          <span class="text-info" v-if="eligibityError">
                            {{ eligibityError }}
                          </span>
                        </div>
                      </div>
                    </div>
  
                    <!-- Name -->
                    <div class="col-md-12">
                      <div class="mb-2">
                        <label for="name" class="form-label">Name</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.name"
                            type="text"
                            class="form-control"
                            id="name"
                            placeholder="Home/Office"
                            required
                          />
                        </div>
                      </div>
                    </div>
  
                    <!-- Street 1 -->
                    <div class="col-md-12">
                      <div class="mb-2">
                        <label for="street_address1" class="form-label">Street 1</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.street_address1"
                            type="text"
                            class="form-control"
                            id="street_address1"
                            placeholder="Enter Street 1"
                            required
                          />
                        </div>
                      </div>
                    </div>
  
                    <!-- Street 2 -->
                    <div class="col-md-12">
                      <div class="mb-2">
                        <label for="street_address2" class="form-label">Street 2</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.street_address2"
                            type="text"
                            class="form-control"
                            id="street_address2"
                            placeholder="Enter Street 2"
                          />
                        </div>
                      </div>
                    </div>
  
                    <!-- Suburb -->
                    <div class="col-md-6">
                      <div class="mb-2">
                        <label for="suburb" class="form-label">Suburb</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.suburbs"
                            type="text"
                            class="form-control"
                            id="suburbs"
                            placeholder="Enter Suburb"
                            required
                          />
                        </div>
                      </div>
                    </div>
  
                    <!-- State -->
                    <div class="col-md-6">
                      <div class="mb-2">
                        <label for="state" class="form-label">City</label>
                        <div class="position-relative">
                          <input
                            v-model="activeAddress.city"
                            type="text"
                            class="form-control"
                            id="city"
                            placeholder="Enter city"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
  
                <div class="button-wrap sign-up-wrap p-0">
                  <button class="btn btn-primary w-100" type="submit">
                    <i class="fa-solid fa-plus"></i>
                    {{ activeAddress.id ? 'Update Address' : 'Add Address' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
          <button class="d-none" data-bs-dismiss="modal" aria-label="Close" ref="closeButton"></button>  
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, onMounted } from 'vue';
  import { useAddressStore } from '@/stores/address';
  import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';
  
  export default {
    name: 'AddAddress',
    setup() {
      const addressStore = useAddressStore();
      const authStore = useAuthStore();
  
      const closeButton = ref(null);

      const { eligibityError } = storeToRefs(addressStore);

      onMounted(() => {
        addressStore.fetchAddresses();
      });
  
      // Computed properties for activeAddress and addresses
      const activeAddress = computed({
        get: () => addressStore.activeAddress,
        set: (value) => {
          Object.assign(addressStore.activeAddress, value);
        },
      });
  
      const addresses = computed(() => addressStore.getAllAddresses);
  
      // Handle form submission
      const handleSubmit = async () => {
        await addressStore.saveActiveAddress();
        authStore.fetchUserDetails();
        closeButton.value.click()
      };
      
      const handlePostalCodeChange = (event) => {
        const code = event.target.value;
        addressStore.checkDeliveryEligibility(code);
      }

      return {
        activeAddress,
        addresses,
        handleSubmit,
        closeButton,
        eligibityError,
        handlePostalCodeChange,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  .addresses-list {
    margin-bottom: 20px;
  }
  
  .address-item {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 10px;
  }
  </style>
  