import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/css/fontawesome.css';
import './style.css';
import App from './App.vue';
import router from './router';
import store from './store';
import 'bootstrap';
import 'animate.css';

// createApp(App).mount("#app");
createApp(App).use(router).use(store).mount('#app');
