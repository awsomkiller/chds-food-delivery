import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import OrderNow from '../views/OrderNow.vue';
import CheckoutPage from '@/views/CheckoutPage.vue';
import OurStory from '@/views/OurStory.vue';
import ProfilePage from '@/views/ProfilePage.vue';
import ContactUs from '@/views/ContactUs.vue';
import OrderSuccess from '@/views/OrderSuccess.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
    meta: {
      title: 'Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },

  {
    path: '/ordernow',
    name: 'Ordernow',
    component: OrderNow,
    meta: {
      title: 'Order Now - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },

  {
    path: '/checkout',
    name: 'CheckoutPage',
    component: CheckoutPage,
    meta: {
      title: 'Check Out - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },
  
  {
    path: '/ourstory',
    name: 'Ourstory',
    component: OurStory,
    meta: {
      title: 'Our Story - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },

  {
    path: '/profile',
    name: 'profilepage',
    component: ProfilePage,
    meta: {
      title: 'Profile Page - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },

  {
    path: '/order/success',
    name: 'ordersuccess',
    component: OrderSuccess,
    meta: {
      title: 'Order Success - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },

  {
    path: '/contact-us',
    name: 'contactus',
    component: ContactUs,
    meta: {
      title: 'Contact Us - Chi Hun Da Su',
      favicon: '@/assets/icons/CHDS logo Blk on White.ico',
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
