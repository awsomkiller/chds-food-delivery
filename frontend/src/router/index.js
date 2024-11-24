import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import OrderNow from '../views/OrderNow.vue';
import CheckoutPage from '@/views/CheckoutPage.vue';
import OurStory from '@/views/OurStory.vue';
import ProfilePage from '@/views/ProfilePage.vue';
import ContactUs from '@/views/ContactUs.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },

  {
    path: '/ordernow',
    name: 'Ordernow',
    component: OrderNow,
  },

  {
    path: '/Checkout',
    name: 'CheckoutPage',
    component: CheckoutPage,
  },
  
  {
    path: '/ourstory',
    name: 'Ourstory',
    component: OurStory,
  },

  {
    path: '/profile',
    name: 'profilepage',
    component: ProfilePage,
  },

  {
    path: '/contact-us',
    name: 'contactus',
    component: ContactUs,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
