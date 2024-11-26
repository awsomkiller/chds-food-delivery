import { defineStore } from 'pinia';
import axios from '../../axios';

export const useAddressStore = defineStore('address', {
  state: () => ({
    addresses: [],
    activeAddress: {
      id: null,
      postal_code: '',
      name: '',
      street_address1: '',
      street_address2: '',
      suburbs: '',
      city: '',
    },
  }),

  getters: {
    getActiveAddress(state) {
      return state.activeAddress;
    },
    getAllAddresses(state) {
      return state.addresses;
    },
  },

  actions: {
    async fetchAddresses() {
      try {
        const response = await axios.get('/user-address/');
        this.addresses = response.data.results;
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
      try {
        const response = await axios.post('/user-address/', addressData);
        this.addresses.push(response.data);
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
  },
});
