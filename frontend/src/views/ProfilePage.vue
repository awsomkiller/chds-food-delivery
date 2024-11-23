<template>
    <div class="main-layout mb-5">
      <div class="profile-heading">
        <h2>Profile</h2>
      </div>
      <div class="profile-text-wrap">
        <div class="d-flex  gap-3">
          <!-- <div class="profile-side-bar">
            <ul>
              <li>
                <a href="" class="active">
                  <span>
                    <i class="fa-solid fa-user"></i>
                  </span>
                  <span>User Details
                  </span>
                </a>
              </li>
              <li>
                <a href="">
                  <span>
                    <i class="fa-solid fa-lock"></i>
                  </span>
                  <span>Password Change</span>
                </a>
              </li>
              <li>
                <a href="">
                  <span>
                    <i class="fa-solid fa-box"></i>
                  </span>
                  <span>Order History</span>
                </a>
              </li>
              <li>
                <a href="">
                  <span>
                    <i class="fa-solid fa-location-dot"></i>
                  </span>
                  <span>Address</span>
                </a>
              </li>
            </ul>
          </div> -->
          <div class="profile-form w-100">
            <div class="profile-form-wrap-content">
              <div class="profile-form-heading">
                <!-- <h4 class="form-heading">Personal Detail</h4> -->

                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Personal Detail</button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Order History</button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Change Password</button>
                        </li>
                    </ul>
                    
              </div>


              <div class="form-input-wrap">

                <div class="tab-content" id="myTabContent">
                    <div class="tab-pane profile-settings fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0"> <div class="input-wrap">
                        <div class="row">
                            <div class="col-md-12">
                            <div class="profile-img-container">
                                <div class="profile-img">
                                <!-- Dummy image shown initially -->
                                <img id="profileImg" src="https://images.news18.com/ibnlive/uploads/2017/05/pankhuri-gidwani.jpg" alt="Profile Picture">
                                </div>
                                <label for="fileInput" class="edit-icon">
                                <i class="fa fa-pencil-alt"></i> <!-- Pencil icon for editing -->
                                </label>
                                <input type="file" id="fileInput" class="file-input" accept="image/*">
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >First Name</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter First Name"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >Last Name</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter Last Name"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >Email Address</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter Email Address"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >Phone Number</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter Phone Number"
                                />
                            </div>
                            </div>

                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >First Name</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter First Name"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >Last Name</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter Last Name"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                        >Email Address</label>
                                <input
                                type="text"
                                name="username"
                                class="form-control"
                                placeholder="Enter Email Address"
                                />
                            </div>
                            </div>
                            <div class="col-md-6 p-2">
                            <div class="input-wrap-withouticon password-bottom-space">
                                <!-- <label>Company Name</label> -->
                                <label for="exampleFormControlInput1" class="form-label"
                            >Phone Number</label>
                                    <input
                                    type="text"
                                    name="username"
                                    class="form-control"
                                    placeholder="Enter Phone Number"
                                    />
                                </div>
                            </div>
                            
                            
                        </div>
                    </div>
                    <div class="footer-button">
                        <button class=" btn btn-secondary sm">Back</button>
                        <a href="#" class="btn btn-primary sm">Save</a>
                    </div>
                </div>
                    <div class="tab-pane profile-settings fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
                        <div class="store-n-diliveri bg-white p-3 rounded mb-3">
                            <ul class="list-unstyled mb-0">

                                <!-- History of order item -->
                                <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>


                                    <!-- History of order item -->
                                    <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>

                                    <!-- History of order item -->
                                    <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>

                                    <!-- History of order item -->
                                    <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>


                                    <!-- History of order item -->
                                    <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>


                                    <!-- History of order item -->
                                    <li class="Item-for-checkout">
                                    <div>
                                        <p class="mb-0">5 <span> <i class="fa-solid fa-xmark"></i></span> Wine-Marinated Chicken Hearts </p>
                                        <p class="item-type-hd mb-0">Q: Main Dish (300g)</p>
                                        <p class="item-type-hd mb-0">Extra Protein</p>
                                        <p class="item-type-hd mb-0">Extra Vegetable</p>
                                        <p class="item-type-hd mb-0">Extra Rice</p>
                                    </div>
                                    <div class="price-n-item-option">
                                        
                                        <p class="mb-0">2nd june 2024  </p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="tab-pane profile-settings fade" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabindex="0">
                        <div class="row">
                            
                            <div class="col-md-6 p-2">
                                <div class="input-wrap-withouticon password-bottom-space">
                                    <!-- <label>Company Name</label> -->
                                    <label for="exampleFormControlInput1" class="form-label"
                                    >New Password</label>
                                    <input
                                    type="text"
                                    name="username"
                                    class="form-control"
                                    placeholder="Enter First Name"
                                    />
                                </div>
                            </div>

                            <div class="col-md-6 p-2">
                                <div class="input-wrap-withouticon password-bottom-space">
                                    <!-- <label>Company Name</label> -->
                                    <label for="exampleFormControlInput1" class="form-label"
                                    >Confirm Password</label>
                                    <input
                                    type="text"
                                    name="username"
                                    class="form-control"
                                    placeholder="Enter First Name"
                                    />
                                </div>
                            </div>

                        </div>
                        <div class="footer-button">
                            <button class=" btn btn-secondary sm">Back</button>
                            <a href="#" class="btn btn-primary sm">Change Password</a>
                        </div>
                    </div>

                </div>
               
              </div>
            </div>
           
          </div>
        </div>
      </div>

      

    </div>


    
</template>


<style>
    

/* -----------profile-------------- */

.profile-heading {
    margin: 16px 88px;
    /* background: linear-gradient(9deg, rgb(197 93 33) 0%, rgba(137, 65, 24, 1) 55%); */
    background-image:  linear-gradient(45deg,rgba(22, 22, 22, 0.5), rgba(33, 38, 43, 0.5)), url('@/assets/about-banner.png');
    background-size: cover;
    border-radius: 8px;
    padding: 16px;
    height: 200px;
    position: relative;
    padding-left: 30px;
    display: flex;
}

.billing-content-wrap{
    min-height: 70vh;
}
.profile-heading::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: repeating-linear-gradient(328deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.06) 20px, rgba(255, 255, 255, 0) 20px, rgba(255, 255, 255, 0) 40px);
    background-size: 200% 100%;
    opacity: 0.3;
    pointer-events: none;
    background-position: left;
}

.profile-heading h2 {
    color: #fff;
    font-weight: 400 !important;
    margin-top: 8px;
    font-size: 30px !important;
}

.profile-text-wrap {
    background-color: #fffcfa;
    /* padding: 16px; */
    margin: -135px 118px 0;
    position: relative;
    border-radius: 8px;
}


.profile-settings{
    min-height: 50vh;
}
.profile-side-bar {
    width: 250px;
    border: 1px solid #ffe0ce;
    /* height: calc(100vh - 143px); */
    padding: 16px 0;
    border-radius: 8px;
    overflow-y: auto;
}

.profile-form {
    width: calc(100% - 250px);
    border: 1px solid #ffe0ce;
    border-radius: 8px;
    /* height: calc(100vh - 143px); */
    overflow: hidden;
}

.profile-side-bar ul {
    display: flex;
    align-items: left;
    flex-direction: column;
    height: auto;
    list-style-type: none;
    gap: 15px;
    margin-bottom: 30px;
}

.profile-side-bar ul li {
    padding: 0 16px;
}

.profile-side-bar a.active {
    background: linear-gradient(9deg, rgb(197 93 33) 0%, #894118 55%);
    color: #fff;
    border-radius: 6px;
}

.profile-side-bar ul a {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    padding: 12px 16px;
    color: #894118;
}

.profile-form-heading {
    padding: 16px;
    border-bottom: 1px solid #ffe0ce;
}

.form-input-wrap {
    padding: 16px;
    overflow-y: auto;
    /* height: calc(100vh - 145px); */
}

.footer-button {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 16px;
    border-top: 1px solid #ffe0ce;
    /* position: sticky; */
    /* bottom: 0; */
    width: 100%;
    gap: 8px;
    background-color: #fff;
}

.profile-img-container {
    position: relative;
    width: 200px;
    height: 147px;
    text-align: center;
  }
  
  /* Profile image styles */
  .profile-img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid white;
  }
  
  .profile-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  /* Edit icon */
  .edit-icon {
    position: absolute;
    top: 9px;
    right: 60px;
    background-color: rgb(194 92 33);
    color: white;
    padding: 5px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 15px;
    transition: background-color 0.3s ease;
    width: 32px;
    height: 32px;
}
  
 
  .file-input {
    display: none; /* Hide the file input */
  }

  .billing-header {
    width: 100%;
    background: #fff;
    position: sticky;
    top: 0;
    z-index: 9;
  }
  .billing-content-wrap {
    overflow: auto;
    height: 100%;
  }
  .sign-up-wrap {
    padding: 16px !important;
    background-color: #fff;
    position: sticky;
    bottom: 0;
    margin-top: 8px !important;
  }

  .profile-form-heading .nav-tabs .nav-link{
    color: var(----card-location-color) !important; 
  }

  .profile-form-heading .nav-tabs .nav-link.active{
    color: white !important; 
    background-color: var(--dark-brown-color);
  }
  

@media screen and (max-width:768px) {
    .profile-heading {
        margin: 0;
    }
    .profile-text-wrap{
        margin-left: 10px;
        margin-right: 10px;
    }

    .nav-link.active, .nav-link:hover {
        color: var(--dark-brown-color) !important;
    }
}
</style>