<script setup>
import FooterComponent from "./components/FooterComponent.vue";
import NavbarComponent from "./components/NavbarComponent.vue";
import LoginModule from "./components/LoginModule.vue";
import SignUp from "./components/SignUp.vue";
import LoginCheck from "./components/LoginCheck.vue";
import PostalCode from "./components/PostalCode.vue";
import AddItem from "./components/AddItem.vue";
import MobileSidebar from "./components/MobileSidebar.vue";
import AddAddress from "./components/AddAddress.vue";


</script>
<template>
  <NavbarComponent />
  <router-view />
  <FooterComponent />
  <LoginModule />
  <SignUp />
  <AddItem />
  <PostalCode/>
  <LoginCheck />
  <MobileSidebar />
  <AddAddress />
</template>

<style></style>
