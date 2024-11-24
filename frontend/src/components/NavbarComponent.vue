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
                        <div class="icon-location">
                            <i class="fa-solid fa-user"></i>
                        </div> 
                        <a class="mb-0" data-bs-toggle="modal" data-bs-target="#ragisterModal"> Login 
                        </a>
                    </div>
                    <div class="follow-us d-flex align-items-center gap-3">
                        <span class="text-white top-text">Follow Us:</span>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
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

@media screen and (min-width:991.91px) {
  .desktop-menu{
    display: block;
  }
 
}

</style>
