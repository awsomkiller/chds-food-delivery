<script>
import NavbarMenu from './NavbarMenu.vue';


export default {
  components: {
    NavbarMenu,
  }
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid p-0 m-0">
              <a class="navbar-brand w-15 p-0 m-0" href="#">
                <img src="@/assets/homepage/CHDS logo Blk on White.png" alt="">
              </a>
             
              <div class="d-flex flex-column w-100 home-wrap-nav">
                  <div class="top-address">
                    <div class="wlcm-text-wrap">
                        <p class="mb-0">Welcome To Chi Hun Da Su </p>
                    </div>
                    <div class="loctn-wrap d-flex align-items-center gap-3">
                        <div class="icon-location">
                            <i class="fa-solid fa-location-dot"></i>
                        </div>
                        <p class="mb-0">243 Burwood Rd Hawthorn, VIC 3122</p>
                    </div>
                    <div class="login-register d-flex align-items-center gap-3 login-hidden">
                        
                        <a class="mb-0" type="button" data-bs-toggle="modal" data-bs-target="#loginModal"> Login 
                        </a>

                        <a class="mb-0" type="button" data-bs-toggle="modal" data-bs-target="#ragisterModal"> Register 
                        </a>
                    </div>

                    <div class="dropdown ">
                      <button class=" profile-header d-flex align-items-center gap-2 btn p-0  dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <div>
                          <img class="profile-image"  src="../assets/homepage/45img.png">
                        </div>
                        <div class="text-mania">
                          <h6 class="mb-0" >John Doe</h6>
                          <small> Delivery Available</small>
                        </div>
                      </button>
                      <ul class="dropdown-menu py-3">
                        <li><a class="dropdown-item " href="#">My Profile</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item text-danger" href="#">Logout</a></li>
                      </ul>
                    </div>

                  </div>
                  <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#mobilemenu" aria-controls="mobilemenu"  >
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="desktop-menu">
                    <NavbarMenu />
                  </div>
                  
              </div>
            </div>
        </nav>









</template>


<!-- <script scoped>
import $ from 'jquery';


function openOverlay() {
  document.getElementById("overlay").style.display = "flex";
}

// Close overlay
document.getElementById("closeOverlay").addEventListener("click", function () {
  document.getElementById("overlay").style.display = "none";
});

// Optionally you can show the overlay on button click
document.querySelector(".theme-btn").addEventListener("click", openOverlay);

    $(window).scroll(function() {
if ($(this).scrollTop() > 1){  
    $('header').addClass("scroll");
  }
  else{
    $('header').removeClass("scroll");
  }
});
</script> -->

<style>

.desktop-menu{
    display: none
  }
  .profile-header{
    color:white;
    text-align: left;
    border-radius: none;
  }

  .profile-header:hover{
    background-color: transparent;
  }
  .profile-header:focus{
    border: none;
  }

  .profile-header .profile-image{
    width: 40px;
    height: 40px;
    object-fit: cover;
    border-radius: 50px;
    border: 1px solid #d2d2d2;
    background-color: white;
  }
  .text-mania{
    line-height: 1;
  }

  .profile-header h6{
    font-size: 14px;
    color: white;
  }

  .profile-header small{
    font-size: 12px;
    color: white;
  }



@media screen and (min-width:991.91px) {
  .desktop-menu{
    display: block;
  }
 
}

</style>
