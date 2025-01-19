// axios.js
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';

const caxios = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 5000,
});

// Function to get the CSRF token from cookies
function getCsrfToken() {
  const name = 'csrftoken';
  const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith(name + '='));
  return cookieValue ? cookieValue.split('=')[1] : null;
}

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });

  failedQueue = [];
};

// Request Interceptor
caxios.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.accessToken) {
      config.headers.Authorization = `Bearer ${authStore.accessToken}`;
    }

    // Set CSRF token in headers
    const csrfToken = getCsrfToken();
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
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
    const originalRequest = error.config;

    // Check if error response exists and status is 401 or 403
    if (
      error.response &&
      (error.response.status === 401 || error.response.status === 403) &&
      !originalRequest._retry
    ) {
      if (authStore.refreshToken) {
        if (isRefreshing) {
          // If a refresh request is already in progress, queue the request
          return new Promise(function (resolve, reject) {
            failedQueue.push({ resolve, reject });
          })
            .then((token) => {
              originalRequest.headers.Authorization = 'Bearer ' + token;
              return caxios(originalRequest);
            })
            .catch((err) => {
              return Promise.reject(err);
            });
        }

        originalRequest._retry = true;
        isRefreshing = true;

        try {
          const refreshResponse = await axios.post('/api/refresh/', {
            refresh_token: authStore.refreshToken,
          });

          const { access_token, refresh_token } = refreshResponse.data;

          // Update tokens in store and localStorage
          authStore.accessToken = access_token;
          authStore.refreshToken = refresh_token;
          localStorage.setItem('accessToken', access_token);
          localStorage.setItem('refreshToken', refresh_token);

          // Update the Authorization header for future requests
          caxios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;

          processQueue(null, access_token);

          // Retry the original request with the new token
          originalRequest.headers.Authorization = `Bearer ${access_token}`;
          return caxios(originalRequest);
        } catch (refreshError) {
           processQueue(refreshError, null);
           authStore.logout();
           window.location = '/ordernow'
           return Promise.reject(refreshError);
        } finally {
           isRefreshing = false;
        }
      } else {
        // No refresh token available, logout the user
        authStore.logout();
      }
    }

    return Promise.reject(error);
  }
);

export default caxios;