// services/axios.js
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';

const caxios = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000,
});

// Request Interceptor
caxios.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.accessToken) {
      config.headers.Authorization = `Bearer ${authStore.accessToken}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor
caxios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const authStore = useAuthStore();

    // Handle 401 Unauthorized (token refresh)
    if (error.response?.status === 401 && authStore.refreshToken) {
      try {
        const refreshResponse = await caxios.post('/refresh', {
          refresh_token: authStore.refreshToken,
        });
        const { access_token } = refreshResponse.data;

        // Update tokens in store and localStorage
        authStore.accessToken = access_token;
        localStorage.setItem('accessToken', access_token);

        // Retry the failed request with the new token
        error.config.headers.Authorization = `Bearer ${access_token}`;
        return caxios.request(error.config);
      } catch (refreshError) {
        authStore.logout();
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export default caxios;
