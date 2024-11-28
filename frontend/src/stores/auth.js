import { defineStore } from 'pinia';
import axios from '../../axios'; // Adjust the path as needed

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
    delivery: false,
  }),

  actions: {
    async login(credentials) {
      try {
        const response = await axios.post('/login/', credentials);
        const { access_token, refresh_token, user } = response.data;

        this.accessToken = access_token;
        this.refreshToken = refresh_token;
        this.user = user;

        localStorage.setItem('accessToken', access_token);
        localStorage.setItem('refreshToken', refresh_token);

        axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
        await this.fetchUserDetails()
        return response.data;
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
      }
    },

    async fetchUserDetails() {
      try {
        const response = await axios.get('/details/');

        this.user = response.data;
        localStorage.setItem('user', JSON.stringify(this.user));
        this.deliveryEligibilityCheck()
        return;
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
      }
    },

    deliveryEligibilityCheck(){
      const postal_code = this.user.primary_address?.postal_code;
      const eligible_postal_code = this.getEligiblePostalCodes();
      this.delivery = eligible_postal_code.includes(parseInt(postal_code));
    },

    getEligiblePostalCodes() {
      return [
        3067, 3103, 3121, 3124, 3068, 3066, 3002,
        3078, 3065, 3123, 3101, 3102, 3144, 3141,
        3142, 3000, 3008, 3006, 3122
      ];
    },


    async handlePasswordChange(payload) {
      try {
        await axios.post('/change-password/', payload);
      } catch (error) {
        console.error('Password Change failed:', error.response?.data || error.message);
        throw error;
      }
    },

    async register(credentials) {
      try {
        const response = await axios.post('/register-user/', credentials);
        await this.login({
          email: credentials.email,
          password: credentials.password,
        });
        return response.data;
      } catch (error) {
        console.error('Registration failed:', error.response?.data || error.message);

        if (error.response && error.response.data) {
          const errorData = error.response.data;
          const formattedErrors = {};

          for (const key in errorData) {
            if (Object.prototype.hasOwnProperty.call(errorData, key)) {
              formattedErrors[key] = errorData[key].join(' ');
            }
          }

          throw formattedErrors;
        } else {
          throw { general: 'An unexpected error occurred. Please try again later.' };
        }
      }
    },

    logout() {
      this.user = null;
      this.accessToken = null;
      this.refreshToken = null;

      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('user');

      delete axios.defaults.headers.common['Authorization'];
    },

    initializeAuth() {
      const accessToken = localStorage.getItem('accessToken');
      const refreshToken = localStorage.getItem('refreshToken');
      const user = JSON.parse(localStorage.getItem('user'));

      if (accessToken && refreshToken && user) {
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
        this.user = user;

        axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;
      }
    },
    getBillingAddress(){
      return this.formatAddressSingleLine(this.user.billing_address)
    },

    formatAddressSingleLine({
      street_address1,
      street_address2,
      suburbs,
      city,
      postal_code,
    }) {
      return [
        [street_address1, street_address2].filter(Boolean).join(', '),
        suburbs?.trim(),
        [city, postal_code].filter(Boolean).join(', '),
      ].filter(Boolean).join(', ');
    },
  },
});
