<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { storeToRefs } from 'pinia';
import NavbarMenu from './NavbarMenu.vue';
import { useAuthStore } from '@/stores/auth';
import { useTranslationStore } from '../stores/translation';
import { useRouter } from 'vue-router';


export default {
  name: 'UserDropdown',
  components: {
    NavbarMenu,
  },
  setup() {
    // Initialize the authentication store
    const authStore = useAuthStore();
    const translationStore = useTranslationStore();
    const router = useRouter();
    
    // Destructure the 'user' from the store's reactive references
    const { user, delivery, profileImage } = storeToRefs(authStore);
    
    // Reactive state to manage dropdown visibility
    const isDropdownOpen = ref(false);
    
    // Reference to the dropdown element for detecting outside clicks
    const dropdown = ref(null);
    
    const t = (label, modules) => {
            return translationStore.translate(label, modules);
        };
    /**
     * Toggles the dropdown's visibility.
     */
    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value;
    };
    
    /**
     * Handles logout functionality.
     */
    const handleLogout = () => {
      authStore.logout();
      // Optionally, navigate the user after logout
       router.push('/');
    };
    
    /**
     * Closes the dropdown if a click is detected outside of it.
     * @param {Event} event - The click event
     */
    const handleClickOutside = (event) => {
      if (dropdown.value && !dropdown.value.contains(event.target)) {
        isDropdownOpen.value = false;
      }
    };
    
    const getProfileImage = () => {
      if (user.value && user.value.profile && user.value.profile.user_image) {
        const baseURL = process.env.VUE_APP_back_URL;
        return baseURL + user.value.profile.user_image;
      } else {
        return "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png";
      }
    };
    // Add event listener for detecting outside clicks when component is mounted
    onMounted(() => {
      document.addEventListener('click', handleClickOutside);
    });
    
    // Remove event listener when component is about to unmount
    onBeforeUnmount(() => {
      document.removeEventListener('click', handleClickOutside);
    });
    
    // Return all reactive properties and methods to the template
    return {
      user,
      profileImage,
      delivery,
      isDropdownOpen,
      toggleDropdown,
      getProfileImage,
      handleLogout,
      dropdown,
      t,
    };
  },
};
</script>


<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid p-0 m-0">
              <a class="navbar-brand w-15 m-0" href="/">
                <img src="@/assets/chi-hun-da-su-logo-vertical-white.svg" alt="">
              </a>
             
              <div class="d-flex flex-column w-100 home-wrap-nav">
                  <div class="top-address">
                    <!-- <div class="wlcm-text-wrap">
                        <p class="mb-0">Welcome To Chi Hun Da Su </p>
                    </div> -->
                    <div class="loctn-wrap d-flex align-items-center gap-3">
                        <div class="icon-location">
                            <i class="fa-solid fa-location-dot"></i>
                        </div>
                        <p class="mb-0">{{ t('4648_rocky_road_philadelphia', ['footer'])}}</p>
                    </div>
                    <div class="login-register d-flex align-items-center gap-3 login-hidden" v-if="!user">
                        
                        <a class="mb-0" type="button" data-bs-toggle="modal" data-bs-target="#loginModal"> Login 
                        </a>

                        <a> | </a>

                        <a class="mb-0" type="button" data-bs-toggle="modal" data-bs-target="#registerModal"> Register 
                        </a>
                    </div>

                    <div class="dropdown" v-if="user" ref="dropdown">
                      <button
                        class="profile-header d-flex align-items-center gap-2 btn p-0 dropdown-toggle"
                        type="button"
                        id="dropdownMenuLink"
                        @click.stop="toggleDropdown"
                        :aria-haspopup="true"
                        :aria-expanded="isDropdownOpen"
                      >
                        <div>
                          <img
                            class="profile-image"
                            :src="getProfileImage()"
                            alt="Profile Image"
                          />
                        </div>
                        <div class="text-mania mobilehide">
                          <h6 class="mb-0">{{ user.full_name }}</h6>
                          <small v-if="delivery">{{ t('delivery_available', ['navbar']) }}</small>
                        </div>
                      </button>
                      <div
                        class="dropdown-menu py-3"
                        :class="{ show: isDropdownOpen }"
                        aria-labelledby="dropdownMenuLink"
                      > 
                        <div class="text-mania desktophide p-3">
                            <h6 class="mb-0">{{ user.full_name }}</h6>
                            <small v-if="delivery">{{ t('delivery_available', ['navbar']) }}</small>
                        </div>
                        <router-link class="dropdown-item" to="/profile">{{ t('my_profile', ['navbar']) }}</router-link>
                        <hr class="dropdown-divider" />
                        <a class="dropdown-item text-danger" @click="handleLogout">{{ t('logout', ['navbar']) }}</a>
                      </div>
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

  .desktophide{
    display: none;
  }

  .mobilehide{
    display:block;
  }

@media screen and (min-width:991.91px) {
  .desktop-menu{
    display: block;
  }
 
}
/* Ensure the dropdown-menu is positioned correctly when shown */
.dropdown-menu {
  transition: opacity 0.3s ease;
}
.dropdown-menu.show {
  display: block;
  opacity: 1;
}



@media screen and (max-width:575px) {
  .mobilehide{
    display:none;
  }
  .desktophide{
    display: block;
  }   
  .profile-header{
    margin-right: 50px;
  }
}

</style>