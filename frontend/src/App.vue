<script setup>
import NavbarComponent from "./components/NavbarComponent.vue";
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
import {  onBeforeMount, computed } from "vue";

const translationStore = useTranslationStore();
const authStore = useAuthStore();
const addressStore = useAddressStore();

onBeforeMount(async () => {
  await translationStore.fetchTranslations();
  await authStore.fetchUserDetails();
  await addressStore.getEligiblePostalCodes();
});

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
  </div>
  <div v-else>
    <!-- Optional: A loading spinner or placeholder can go here -->
    <p>Loading translations...</p>
  </div>
</template>

<style></style>
