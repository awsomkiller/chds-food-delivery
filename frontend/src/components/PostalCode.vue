<template>
    

<!-- Login postal code popup -->
<div class="modal modal-search-dish fade" id="postalcodeModal" tabindex="-1" aria-labelledby="postalcodeModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <!-- <div class="modal-header">
            <h5 class="modal-title">Search Dish</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
 -->

        <div class="modal-body text-center ">

            
            
            <img class="mb-3 mx-auto " src="@/assets/icons/delivery-parcel.svg" width="80px">

            <div class="text-start mb-3">
                <label for="formGroupExampleInput" class="form-label">Postal Code</label>
                <form class="d-flex" role="search">
                    
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
                </form>

                <p class="text-danger mt-3"> Sorry, delivery is not available for this location. Please select the pickup option instead. </p>
            </div>
            
            <!-- for proceed -->
            <button type="button" class="btn btn-primary  mb-3">Proceed <i class="fa-solid fa-arrow-right"></i> </button>
                <br>

                <button type="button" class="btn btn-primary">Pick Up <i class="fa-solid fa-boxes-packing"></i> </button>
            
        </div>
      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-primary">Register</button>
        <button type="button" class="btn btn-primary">Login</button>
      </div> -->
    </div>
  </div>
</div>


</template>