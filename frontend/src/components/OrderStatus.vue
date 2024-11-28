<template>
  <!-- Order Success Modal -->
  <div
    class="modal modal-search-dish fade"
    id="orderSuccess"
    tabindex="-1"
    aria-labelledby="orderSuccessModal"
    aria-hidden="true"
    ref="orderSuccessModal">
  >
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body text-center">
          <img
            class="mb-3 mx-auto"
            src="../assets/order-status/Order-shipped.svg"
            width="80px"
            alt="Order Shipped"
          />
          <h5 class="text-secondary text-center">Order Placed Successfully !!</h5>
        </div>
        <button
          type="button"
          class="btn btn-success"
          data-bs-dismiss="modal"
          aria-label="Close"
          @click="redirectToOrderNow"
        >
          Okay
        </button>
      </div>
    </div>
  </div>

  <!-- Order Failed Modal (Unchanged) -->
  <div
    class="modal modal-search-dish fade"
    id="orderFailed"
    tabindex="-1"
    aria-labelledby="orderFailedModal"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body text-center">
          <img
            class="mb-3 mx-auto"
            src="../assets/order-status/Order-canceled.svg"
            width="80px"
            alt="Order Canceled"
          />
          <h5 class="text-secondary text-center text-danger">Payment Failed !!</h5>
        </div>
        <button
          type="button"
          class="btn btn-success"
          data-bs-dismiss="modal"
          aria-label="Close"
        >
          Okay
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCartStore } from '@/stores/cart';

const router = useRouter();
const cartStore = useCartStore();

// Reference to the success modal
const orderSuccessModal = ref(null);

// Function to handle redirection after modal is hidden
const redirectToOrderNow = () => {
  cartStore.resetCart();
  router.push({ name: 'Ordernow' });
};

// Event handler for when the modal is hidden
const handleModalHidden = () => {
  redirectToOrderNow();
};

onMounted(() => {
  if (orderSuccessModal.value) {
    // Attach the event listener to the modal's hidden event
    orderSuccessModal.value.addEventListener('hidden.bs.modal', handleModalHidden);
  }
});


</script>

<style scoped>
/* Add any component-specific styles here */
</style>
