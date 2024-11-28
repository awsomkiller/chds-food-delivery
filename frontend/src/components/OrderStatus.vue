<template>
    <!-- order shipped popup -->
<div class="modal modal-search-dish fade" id="orderSuccess" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">
        <div class="modal-body text-center ">
          <img class="mb-3 mx-auto " src="../assets/order-status/Order-shipped.svg" width="80px">
          <h5 class="text-secondary text-center"> Order Placed </h5>
        </div>
    </div>
  </div>
</div>

<div class="modal modal-search-dish fade" id="orderFailed" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body text-center ">
          <img class="mb-3 mx-auto " src="../assets/order-status/Order-canceled.svg" width="80px">
          <h5 class="text-secondary text-center text-danger"> Order Canceled/Failed </h5>
      </div>
    </div>
  </div>
</div>
</template>