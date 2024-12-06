<script setup>
// import FooterComponent from "./components/FooterComponent.vue";
import NavbarComponent from "./components/NavbarComponent.vue";
import LoginModule from "./components/LoginModule.vue";
import SignUp from "./components/SignUp.vue";
import PostalCode from "./components/PostalCode.vue";
import AddItem from "./components/AddItem.vue";
import MobileSidebar from "./components/MobileSidebar.vue";
import AddAddress from "./components/AddAddress.vue";
import OrderStatus from "./components/OrderStatus.vue";
import { useTranslationStore } from "./stores/translation";
import { onMounted } from "vue";

const translationStore = useTranslationStore();

onMounted(()=>{
  translationStore.fetchTranslations();
});

</script>
<template>
  <NavbarComponent />
  <router-view />
  <!-- <FooterComponent /> -->
  <LoginModule />
  <SignUp />
  <AddItem />
  <PostalCode/>
  <MobileSidebar />
  <AddAddress />
  <OrderStatus />
</template>

<style></style>
