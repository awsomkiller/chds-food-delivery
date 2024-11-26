<template>
    
<!-- Login check popup popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <!-- <div class="modal-header">
            <h5 class="modal-title">Search Dish</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
 -->

        <div class="modal-body text-center ">
            
            <img class="mb-3 mx-auto " src="../assets/icons/place-order.svg" width="80px">


            <h5 class="text-secondary"> For going to checkout page you need to register or login first.</h5>
           
        </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#postalcodeModal">Register</button>
        <button type="button" class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#postalcodeModal">Login</button>
      </div>
    </div>
  </div>
</div>




<!-- Order Placed popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <div class="modal-body text-center ">
            
            <img class="mb-3 mx-auto " src="../assets/order-status/order-delivered.svg" width="80px">

            <h5 class="text-secondary text-center"> Order Placed </h5>
           
        </div>
      
    </div>
  </div>
</div>



<!-- Order preparing popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

      
        <div class="modal-body text-center ">
            
            <img class="mb-3 mx-auto " src="../assets/order-status/order-preparing.svg" width="80px">
            <h5 class="text-secondary text-center"> Order Preparing </h5>
           
        </div>
     
    </div>
  </div>
</div>



<!-- order shipped popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <div class="modal-body text-center ">
          <img class="mb-3 mx-auto " src="../assets/order-status/Order-shipped.svg" width="80px">
          <h5 class="text-secondary text-center"> Order Shipped </h5>
        </div>
      
    </div>
  </div>
</div>




<!-- Order failed popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

      <div class="modal-body text-center ">
          <img class="mb-3 mx-auto " src="../assets/order-status/Order-canceled.svg" width="80px">
          <h5 class="text-secondary text-center text-danger"> Order Canceled/Failed </h5>
      </div>
      
    </div>
  </div>
</div>



<!-- Order delivered popup -->
<div class="modal modal-search-dish fade" id="loginregisterModal" tabindex="-1" aria-labelledby="loginregisterModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

      <div class="modal-body text-center ">
          <img class="mb-3 mx-auto " src="../assets/order-status/Order-shipped.svg" width="80px">
          <h5 class="text-secondary text-center"> Order Delivered </h5>
      </div>
    </div>
  </div>
</div>

</template>