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
                        <p class="mb-0"> Login / Register
                        </p>
                    </div>
                    <div class="follow-us d-flex align-items-center gap-3">
                        <span class="text-white top-text">Follow Us:</span>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                  </div>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <div class="d-flex hidden-collapse align-items-start justify-content-between">
                      <a class="navbar-brand w-15 p-0 m-0" href="#">
                        <img src="@/assets/CHDS logo Blk on White.png" alt="">
                      </a>
                      <div class="cross-icon">
                        <i class="fa-solid fa-xmark"></i>
                      </div>

                    </div>
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">Order Now</a>
                      </li>
                      
                      <li class="nav-item">
                        <a class="nav-link">Our Story</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link">My Account</a>
                      </li>
                      <div class="login-register d-flex align-items-center gap-3 show-login nav-link">
                        <!-- <div class="icon-location">
                            <i class="fa-solid fa-user"></i>
                        </div> -->
                        <p class="mb-0"> Login / Register
                        </p>
                    </div>
                    </ul>
                    
                    <div class="d-flex gap-2 contact-wrap">
                        <button class="btn theme-btn theme-outline-btn" type="button">
                            Contact
                          </button>
                          <form class="d-flex position-relative border-set" role="search">
                            <select class="form-select search" aria-label="Default select example">
                              <option selected>English</option>
                              <option value="1">Chinese</option>
                            </select>
                          </form>
                    </div>
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


</style>
