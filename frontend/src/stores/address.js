import { defineStore } from 'pinia';
import axios from '../../axios';
import { useAuthStore } from './auth';


export const useAddressStore = defineStore('address', {
  state: () => ({
    addresses: [],
    pickUpAddresses: [],
    activeAddress: {
      id: null,
      postal_code: '',
      name: '',
      street_address1: '',
      street_address2: '',
      suburbs: '',
      city: '',
    },
    eligibleAddress: [],
    eligibityError:'',
    eligiblePostalCodes: [],
  }),

  getters: {
    getActiveAddress(state) {
      return state.activeAddress;
    },
    getAllAddresses(state) {
      return state.addresses;
    },
    getEligibleAddresses(state) { // Optional: Getter for eligible addresses
      return state.eligibleAddress;
    },
  },

  actions: {
    // Define eligible postal codes as a constant
    async getEligiblePostalCodes() {
      const response = await axios.get('/menu/delivery-point/')
      const data = response.data.results
      this.eligiblePostalCodes = data.map((item)=>{return parseInt(item.postal_code)});
      const authStore = useAuthStore();
      authStore.deliveryEligibilityCheck();
    },

    fetchEligiblePostalCodes(){
      return this.eligiblePostalCodes;
    },

    // Method to update eligibleAddress based on postal codes
    updateEligibleAddress() {
      console.log(this.eligiblePostalCodes);
      this.eligibleAddress = this.addresses.filter(address =>
        this.eligiblePostalCodes.includes(parseInt(address.postal_code))
      );
    },

    async fetchAddresses() {
      try {
        const response = await axios.get('/user-address/');
        this.addresses = response.data.results;
        this.updateEligibleAddress();
      } catch (error) {
        console.error('Failed to fetch addresses:', error);
      }
      try {
        const response = await axios.get('/menu/pickup-location/');
        this.pickUpAddresses = response.data.results;
      } catch (error) {
        console.error('Failed to fetch addresses:', error);
      }
    },

    initializeActiveAddress() {
      this.activeAddress = {
        id: null,
        postal_code: '',
        name: '',
        street_address1: '',
        street_address2: '',
        suburbs: '',
        city: '',
      };
    },

    setActiveAddress(address) {
      this.activeAddress = { ...address };
    },

    async addAddress(addressData) {
      this.eligibityError = "";
      try {
        const response = await axios.post('/user-address/', addressData);
        this.addresses.push(response.data);
        this.updateEligibleAddress(); // Update eligibleAddress after adding
        this.initializeActiveAddress();
      } catch (error) {
        console.error('Failed to add address:', error);
      }
    },

    async updateAddress(addressId, updatedData) {
      try {
        const response = await axios.put(`/user-address/${addressId}`, updatedData);
        const index = this.addresses.findIndex(addr => addr.id === addressId);
        if (index !== -1) {
          this.addresses.splice(index, 1, response.data);
          this.updateEligibleAddress();
        }
        this.initializeActiveAddress();
      } catch (error) {
        console.error('Failed to update address:', error);
      }
    },

    async deleteAddress(addressId) {
      try {
        await axios.delete(`/user-address/${addressId}`);
        this.addresses = this.addresses.filter(addr => addr.id !== addressId);
        this.updateEligibleAddress();
      } catch (error) {
        console.error('Failed to delete address:', error);
      }
    },

    async saveActiveAddress() {
      if (this.activeAddress.id) {
        await this.updateAddress(this.activeAddress.id, this.activeAddress);
      } else {
        await this.addAddress(this.activeAddress);
      }
    },
    checkDeliveryEligibility(postal_code){
      if(this.eligiblePostalCodes.includes(parseInt(postal_code))){
        this.eligibityError = "Delivery available";
      }
      else{
        this.eligibityError = "Delivery not available";
      }
      return;
    }
  },
});
