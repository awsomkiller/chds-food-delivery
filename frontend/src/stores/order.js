import { defineStore } from 'pinia';
import axios from '../../axios';

export const useOrderStore = defineStore('orders', {
  state: () => ({
    orders: [],
  }),
  actions:{
    async fetchOrders() {
        try {
          const response = await axios.get('/orders/list-orders/');
          this.orders = response.data;
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
  
  }
});