<script setup>
import FooterComponent from "./components/FooterComponent.vue";
import NavbarComponent from "./components/NavbarComponent.vue";
import LoginModule from "./components/LoginModule.vue";
import SignUp from "./components/SignUp.vue";
import CartData from "./components/CartData.vue";
import LoginCheck from "./components/LoginCheck.vue";
import PostalCode from "./components/PostalCode.vue";
import AddItem from "./components/AddItem.vue";

</script>
<template>
  <NavbarComponent />
  <router-view />
  <FooterComponent />
  <LoginModule />
  <SignUp />
  <CartData />
  <AddItem />
  <PostalCode/>
  <LoginCheck />
</template>

<style></style>
