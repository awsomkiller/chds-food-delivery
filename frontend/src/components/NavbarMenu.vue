<script>


export default {
    name: 'NavbarMenu',
}
</script>

<template>
    <div class="navbar-collapse" id="navbarSupportedContent">
        <div class="d-flex idendity-logo hidden-collapse align-items-start justify-content-between">
            <a class="navbar-brand w-15 p-0 m-0" href="#">
                <img src="@/assets/CHDS logo Blk on White.png" alt="">
            </a>
            <div class="cross-icon">
                <i class="fa-solid fa-xmark"></i>
            </div>

        </div>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/" active-class="active" >Home</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to="/ordernow" active-class="active" >Order Now</router-link>
        </li>   
        <li class="nav-item">
            <router-link class="nav-link" to="/ourstory" active-class="active">Our Story</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to="/contact-us" active-class="active">Contact Us</router-link>
        </li>

    
       
        <div class="login-register d-flex align-items-center gap-3 show-login ">
            <!-- <div class="icon-location">
                <i class="fa-solid fa-user"></i>
            </div> -->
            <a class="mb-0 nav-link" type="button" data-bs-toggle="modal" data-bs-target="#registerModal" data-bs-dismiss="offcanvas" > Register
            </a>

            <a class="mb-0 nav-link" type="button" data-bs-toggle="modal" data-bs-target="#loginModal" data-bs-dismiss="offcanvas" > Login
            </a>
        </div>
        </ul>
        
        <div class="d-flex gap-2 contact-wrap">
            <form class="d-flex position-relative border-set" role="search">
                <select class="form-select search" aria-label="Default select example">
                <option selected>English</option>
                <option value="1">Chinese</option>
                </select>
            </form>
        </div>
    </div>
    
</template>

<style>

@media screen and (max-width:991.91px) {
    .idendity-logo{
        display: none !important;
        padding: 0;
    }

    .navbar-collapse.idendity-logo{
        padding: 0;
    }

    .contact-wrap{
        padding: 2rem 0;
    }

}

 

</style>