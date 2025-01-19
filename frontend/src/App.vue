<script setup>
import NavbarComponent from "./components/NavbarComponent.vue";
import FooterComponent from '@/components/FooterComponent.vue';
import LoginModule from "./components/LoginModule.vue";
import SignUp from "./components/SignUp.vue";
import PostalCode from "./components/PostalCode.vue";
import AddItem from "./components/AddItem.vue";
import MobileSidebar from "./components/MobileSidebar.vue";
import AddAddress from "./components/AddAddress.vue";
import OrderStatus from "./components/OrderStatus.vue";
import { useTranslationStore } from "./stores/translation";
import { useAuthStore } from "./stores/auth";
import { useAddressStore } from "./stores/address";
import {  onBeforeMount, computed, watch } from "vue";
import { useWalletStore } from "./stores/wallet";
import { storeToRefs } from "pinia";

const translationStore = useTranslationStore();
const authStore = useAuthStore();
const addressStore = useAddressStore();
const walletStore = useWalletStore();

const { user } = storeToRefs(authStore);


onBeforeMount(async () => {
  await translationStore.fetchTranslations();
  if(user.value){
    await authStore.fetchUserDetails();
    await addressStore.getEligiblePostalCodes();
    await addressStore.fetchAddresses();
    await walletStore.fetchWallet();
  }
});

watch(
     user,
     async(newUser, oldUser) => {
         if (newUser != null && newUser !== oldUser) {
             console.log("userupdated")
             await addressStore.getEligiblePostalCodes();
             await addressStore.fetchAddresses();
             await walletStore.fetchWallet();
         }
     }
 );

const isLoaded = computed(() => translationStore.isLoaded);
</script>

<template>
  <div v-if="isLoaded">
    <NavbarComponent />
    <router-view />
    <LoginModule />
    <SignUp />
    <AddItem />
    <PostalCode />
    <MobileSidebar />
    <AddAddress />
    <OrderStatus />
    <FooterComponent />
  </div>
  <div v-else>
    <!-- Optional: A loading spinner or placeholder can go here -->
    <p>Loading translations...</p>
  </div>
</template>

<style></style>
