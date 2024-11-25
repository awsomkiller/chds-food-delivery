<template>
    <!-- Login postal code popup -->
<div class="modal modal-search-dish fade" id="addressModal" tabindex="-1" aria-labelledby="addressModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <div class="modal-header">
            <h5 class="modal-title">Add New Address</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>


        <div class="modal-body ">
                <div class="login-content p-0">
                
                    <!-- <  div class="other-option-login d-flex gap-2 align-items-center">
                    <button
                        type="button"
                        class="login-by-google google-btn btn d-flex gap-1 align-items-center"
                    >
                        <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="12"
                        height="25"
                        viewBox="88.428 12.828 107.543 207.085"
                        id="facebook"
                        >
                        <path
                            fill="#3c5a9a"
                            d="M158.232 219.912v-94.461h31.707l4.747-36.813h-36.454V65.134c0-10.658 2.96-17.922 18.245-17.922l19.494-.009V14.278c-3.373-.447-14.944-1.449-28.406-1.449-28.106 0-47.348 17.155-47.348 48.661v27.149H88.428v36.813h31.788v94.461l38.016-.001z"
                        ></path>
                        </svg>

                        <p class="mb-0">Continue with Google</p>
                    </button>
                    <button
                        type="button"
                        class="login-by-facebook google-btn btn d-flex gap-1 align-items-center"
                    >
                        <svg
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 48 48"
                        class="LgbsSe-Bz112c"
                        >
                        <g>
                            <path
                            fill="#EA4335"
                            d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"
                            ></path>
                            <path
                            fill="#4285F4"
                            d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"
                            ></path>
                            <path
                            fill="#FBBC05"
                            d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"
                            ></path>
                            <path
                            fill="#34A853"
                            d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"
                            ></path>
                            <path fill="none" d="M0 0h48v48H0z"></path>
                        </g>
                        </svg>
                        <p class="mb-0">Continue with Facebook</p>
                    </button>
                    </>
                    <div class="or-div">
                    <p>OR</p>
                    </div> -->
                    <form>

                        
                    <div class="form-wrap ">
                        
                        
                        <div class="row">

                            <div class="col-md-12">
                                <div class="mb-2">
                                <label for="exampleFormControlInput1" class="form-label"
                                    >Pincode</label
                                >
                                <div class="position-relative">
                                
                                    <input
                                    type="number"
                                    class="form-control"
                                    placeholder="Enter Pincode"
                                    />
                                    
                                </div>
                                <!-- <div class="error-wrap d-none">
                                    <p>Please enter a 10-digit phone number.</p>
                                </div> -->
                                </div>
                            </div>
                        <div class="col-md-12">
                            <div class="mb-2">
                            <label for="exampleFormControlInput1" class="form-label"
                                >Name</label
                            >
                            <div class="position-relative">
                                
                                <input
                                type="text"
                                class="form-control"
                                placeholder="Home/Office"
                                />
                                
                            </div>
                            <!-- <div class="error-wrap d-none">
                                <p>Password is required.</p>
                            </div> -->
                            </div>
                        </div>
                        <div class="col-md-12">
                            <div class="mb-2">
                            <label for="exampleFormControlInput1" class="form-label"
                                >Street 1</label
                            >
                            <div class="position-relative">
                                
                                <input
                                type="text"
                                class="form-control"
                                placeholder="Enter Street 1"
                                />
                                
                            </div>
                            <!-- <div class="error-wrap d-none">
                                <p>Password is required.</p>
                            </div> -->
                            </div>
                        </div>
                        <div class="col-md-12">
                            <div class="mb-2">
                            <label for="exampleFormControlInput1" class="form-label"
                                >Street 2</label
                            >
                            <div class="position-relative">
                            
                                <input
                                type="text"
                                class="form-control"
                                placeholder="Enter Street 2"
                                />
                                
                            </div>
                            <!-- <div class="error-wrap d-none">
                                <p>Please enter a 10-digit phone number.</p>
                            </div> -->
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-2">
                            <label for="exampleFormControlInput1" class="form-label"
                                >Suburb</label
                            >
                            <div class="position-relative">
                            
                                <input
                                type="text"
                                class="form-control"
                                placeholder="Enter Suburb"
                                />
                                
                            </div>
                            <!-- <div class="error-wrap d-none">
                                <p>Please enter a 10-digit phone number.</p>
                            </div> -->
                            </div>
                        </div>
                       
                        <div class="col-md-6">
                            <div class="mb-2">
                            <label for="exampleFormControlInput1" class="form-label"
                                >State</label
                            >
                            <div class="position-relative">
                            
                                <input
                                type="text"
                                class="form-control"
                                placeholder="Enter State"
                                />
                                
                            </div>
                            <!-- <div class="error-wrap d-none">
                                <p>Please enter a 10-digit phone number.</p>
                            </div> -->
                            </div>
                        </div>
                        
                        </div>
                        
                    
                    </div>
                    
                    </form>
                    <div class="button-wrap sign-up-wrap p-0">
                    <button class="btn btn-primary w-100" type="button"><i class="fa-solid fa-plus"></i> Add Address</button>
                    </div>
                </div>
                

        </div>

      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-primary">Register</button>
      </div> -->
    </div>
  </div>
</div>


</template>