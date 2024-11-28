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
import { useAuthStore } from '@/stores/auth'; // Ensure this path is correct for your project

// Create the Pinia store
const pinia = createPinia();

// Create the Vue app instance
const app = createApp(App);

router.afterEach((to, from) => {
    // Update the document title
    if (to.meta.title) {
      document.title = to.meta.title;
    } else {
      document.title = 'Chi Hun Da Su'; 
    }
  
    // Update the favicon
    if (to.meta.favicon) {
      let link = document.querySelector("link[rel~='icon']");
      if (!link) {
        // If no favicon link exists, create one
        link = document.createElement('link');
        link.rel = 'icon';
        document.head.appendChild(link);
      }
      link.href = `${to.meta.favicon}`;
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
