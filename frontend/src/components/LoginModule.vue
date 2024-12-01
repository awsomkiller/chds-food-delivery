<script>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth'; 
import { useRouter } from 'vue-router';
import { Modal } from 'bootstrap';

export default {
  name: 'LoginModule',
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    const closeModalRef = ref(null);

    // Form fields
    const identifier = ref('');
    const password = ref('');

    // UI State
    const showPassword = ref(false);
    const loading = ref(false);

    // Error handling
    const errors = ref({});
    const loginError = ref('');

    // Toggle password visibility
    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    // Clear specific field error
    const clearIdentifierError = () => {
      if (errors.value.identifier) {
        errors.value.identifier = '';
      }
    };

    // Validate form inputs
    const validate = () => {
      const tempErrors = {};

      if (!identifier.value.trim()) {
        tempErrors.identifier = 'Email address is required.';
      } else {
        // Simple regex for email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        // const phoneRegex = /^0?\d{9}$/;

        if (
          !emailRegex.test(identifier.value.trim())
          // !phoneRegex.test(identifier.value.trim())
        ) {
          tempErrors.identifier = 'Please enter a valid email address ';
        }
      }

      if (!password.value) {
        tempErrors.password = 'Password is required.';
      }

      errors.value = tempErrors;

      return Object.keys(tempErrors).length === 0;
    };

    const handleLogin = async () => {
      if (!validate()) {
        return;
      }

      loading.value = true;
      loginError.value = '';

      try {
        const credentials = {
          email: identifier.value.trim(),
          password: password.value,
        };

        await authStore.login(credentials);

        router.push({ name: 'Ordernow' });

        const modalElement = document.getElementById('loginModal');
        if (modalElement) {
            const modalInstance = Modal.getInstance(modalElement);
            if (modalInstance) {
                modalInstance.hide();
            }
        }
      } catch (error) {
        loginError.value = error;
      } finally {
        loading.value = false;
      }
    };

    // Placeholder functions for social logins
    const handleGoogleLogin = () => {
      alert('Google login is not implemented yet.');
    };

    const handleFacebookLogin = () => {
      alert('Facebook login is not implemented yet.');
    };

    const closeModal = () => {
      const modalElement = document.getElementById('loginModal');
      const modalInstance = bootstrap.Modal.getInstance(modalElement) || new bootstrap.Modal(modalElement);
      modalInstance.hide();
    };

    // Import Bootstrap's Modal class
    let bootstrap;
    onMounted(() => {
      bootstrap = require('bootstrap/dist/js/bootstrap.bundle.min.js');
    });

    return {
      identifier,
      closeModal,
      password,
      showPassword,
      togglePasswordVisibility,
      handleLogin,
      handleGoogleLogin,
      handleFacebookLogin,
      errors,
      loginError,
      loading,
      clearIdentifierError,
      closeModalRef,
    };
  },
};
</script>


<template>
  <!-- Login Modal -->
  <div
    class="modal modal-search-dish fade"
    id="loginModal"
    tabindex="-1"
    aria-labelledby="loginModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
      <div class="modal-content">

        <!-- Modal Body -->
        <div class="modal-body text-center">
          <div class="login-content">
            <!-- Logo -->
            <div class="logo-wrap">
              <img src="@/assets/CHDS logo Blk transparent.png" alt="CHDS Logo" />
            </div>

            <!-- Login Text -->
            <div class="login-text-wrap">
              <h4>Login</h4>
              <p>Hi 👋 there! Log in and let’s make today’s meals memorable</p>
            </div>

            <!-- Social Login Options
            <div class="other-option-login d-flex gap-2 align-items-center">
              <button
                type="button"
                class="login-by-facebook facebook-btn google-btn btn d-flex gap-1 align-items-center"
                @click="handleFacebookLogin"
                disabled
              > -->
                <!-- Facebook SVG Icon -->
                <!-- <svg
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
                <p class="mb-0">Continue with Facebook</p>
              </button>
              <button
                type="button"
                class="login-by-google google-btn btn d-flex gap-1 align-items-center"
                @click="handleGoogleLogin"
                disabled
              > -->
                <!-- Google SVG Icon -->
                <!-- <svg
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
                <p class="mb-0">Continue with Google</p>
              </button>
            </div> -->

            <!-- Divider -->
            <div class="or-div">
              <p>OR</p>
            </div>

            <!-- Login Form -->
            <form @submit.prevent="handleLogin">
              <div class="form-wrap">
                <!-- Email/Phone Input -->
                <div class="mb-3 form-wrap-content">
                  <label for="identifier" class="form-label">Email Address or Phone Number</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-envelope"></i>
                    </div>
                    <input
                      type="text"
                      id="identifier"
                      v-model="identifier"
                      class="form-control"
                      placeholder="Enter Email Address or Phone Number"
                      :class="{ 'is-invalid': errors.identifier }"
                    />
                    <div class="info-icon" @click="clearIdentifierError" v-if="errors.identifier">
                      <i class="fa-solid fa-circle-exclamation"></i>
                    </div>
                  </div>
                  <div class="invalid-feedback" v-if="errors.identifier">
                    {{ errors.identifier }}
                  </div>
                </div>

                <!-- Password Input -->
                <div class="mb-3 form-wrap-content">
                  <label for="password" class="form-label">Password</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-lock"></i>
                    </div>
                    <input
                      :type="showPassword ? 'text' : 'password'"
                      id="password"
                      v-model="password"
                      class="form-control"
                      placeholder="Enter Password"
                      :class="{ 'is-invalid': errors.password }"
                    />
                    <div class="info-icon" @click="togglePasswordVisibility">
                      <i :class="showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"></i>
                    </div>
                  </div>
                  <div class="invalid-feedback" v-if="errors.password">
                    {{ errors.password }}
                  </div>
                </div>

                <!-- Login Button -->
                <div class="button-wrap mb-3">
                  <button class="btn btn-primary w-100" type="submit" :disabled="loading">
                    <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                    <span v-else>Login</span>
                  </button>
                </div>

                <!-- Error Message -->
                <div v-if="loginError" class="alert alert-danger" role="alert">
                  {{ loginError }}
                </div>
              </div>

              <!-- Signup Prompt -->
              <div class="bottom-text">
                <p>
                  Don't have an account?
                  <a data-bs-toggle="modal" data-bs-target="#registerModal" @click.prevent="closeModal">
                    <span>Sign Up Now!</span>
                  </a>
                </p>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  </div>
  <button type="button" ref="closeModal" class="d-none" data-bs-dismiss="modal" aria-label="Close"></button>
</template>


<style scoped>
/* Add any component-specific styles here */

.invalid-feedback {
  display: block;
}

.info-icon {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #dc3545; /* Bootstrap's danger color */
}

.form-control.is-invalid {
  border-color: #dc3545;
}

.bottom-text p {
  margin-top: 1rem;
}

.bottom-text a {
  color: #0d6efd; /* Bootstrap's primary color */
  text-decoration: none;
}

.bottom-text a:hover {
  text-decoration: underline;
}
</style>
