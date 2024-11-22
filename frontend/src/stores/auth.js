import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
  }),

  actions: {
    async login(credentials) {
      try {
        const response = await axios.post('/login', credentials);
        const { access_token, refresh_token, user } = response.data;

        // Save tokens and user data in state
        this.accessToken = access_token;
        this.refreshToken = refresh_token;
        this.user = user;

        // Save tokens in localStorage
        localStorage.setItem('accessToken', access_token);
        localStorage.setItem('refreshToken', refresh_token);
        localStorage.setItem('user', JSON.stringify(user));

        // Set Axios Authorization Header
        axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;

        return response.data;
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
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
