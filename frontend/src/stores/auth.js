import { defineStore } from 'pinia';
import axios from '../../axios'; // Adjust the path as needed

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
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
        localStorage.setItem('user', JSON.stringify(user));

        axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;

        return response.data;
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
      }
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
  },
});
