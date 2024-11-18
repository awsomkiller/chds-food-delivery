import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import OrderNow from '../views/OrderNow.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },

  {
    path: '/ordernow',
    name: 'Oredernow',
    component: OrderNow,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
