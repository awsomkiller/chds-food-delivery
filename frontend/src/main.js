import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/css/fontawesome.css';
import 'animate.css';
import './style.css';

import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import { useAuthStore } from '@/stores/auth';

// Create the Pinia store
const pinia = createPinia();

// Create the Vue app instance
const app = createApp(App);

router.afterEach((to) => {
    // Update the document title
    if (to.meta.title) {
      document.title = to.meta.title;
    } else {
      document.title = 'Chi Hun Da Su'; 
    }
  });

// Use the Pinia store and router
app.use(pinia);
app.use(router);

// Initialize authentication before mounting the app
const authStore = useAuthStore(); 
authStore.initializeAuth();

// Mount the app to the DOM
app.mount('#app');
