<!-- Vue registration component -->
<template>
  <!-- Registration Modal -->
  <div
    class="modal modal-search-dish fade"
    id="registerModal"
    tabindex="-1"
    aria-labelledby="registerModalLabel"
    aria-hidden="true"
    ref="registerModal"
  >
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body text-center">
          <div class="login-content">
            <div class="login-text-wrap">
              <h4>Sign Up</h4>
              <p>Hi 👋 there! Sign Up to have a memorable meal</p>
            </div>

            <!-- Registration Form -->
            <form @submit.prevent="handleRegister">
              <div class="form-wrap">

                <!-- General Error Message -->
                <div v-if="errors.general" class="alert alert-danger" role="alert">
                  {{ errors.general }}
                </div>

                <!-- Full Name Field -->
                <div class="mb-3 form-wrap-content">
                  <label for="fullName" class="form-label">Full Name</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-user"></i>
                    </div>
                    <input
                      type="text"
                      id="fullName"
                      v-model="form.full_name"
                      class="form-control"
                      placeholder="Enter Full Name"
                      required
                    />
                    <div class="info-icon" v-if="errors.full_name">
                      <i class="fa-solid fa-circle-exclamation"></i>
                    </div>
                  </div>
                  <div class="error-wrap" v-if="errors.full_name">
                    <p>{{ errors.full_name }}</p>
                  </div>
                </div>

                <!-- Email Address Field -->
                <div class="mb-3 form-wrap-content">
                  <label for="email" class="form-label">Email Address</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-envelope"></i>
                    </div>
                    <input
                      type="email"
                      id="email"
                      v-model="form.email"
                      class="form-control"
                      placeholder="Enter Email Address"
                      required
                    />
                    <div class="info-icon" v-if="errors.email">
                      <i class="fa-solid fa-circle-exclamation"></i>
                    </div>
                  </div>
                  <div class="error-wrap" v-if="errors.email">
                    <p>{{ errors.email }}</p>
                  </div>
                </div>

                <!-- Phone Number Field -->
                <div class="mb-3 form-wrap-content">
                  <label for="phoneNumber" class="form-label">Phone Number</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-phone"></i>
                    </div>
                    <input
                      type="tel"
                      id="phoneNumber"
                      v-model="form.mobile_number"
                      class="form-control"
                      placeholder="Enter Phone Number"
                      required
                    />
                    <div class="info-icon" v-if="errors.mobile_number">
                      <i class="fa-solid fa-circle-exclamation"></i>
                    </div>
                  </div>
                  <div class="error-wrap" v-if="errors.mobile_number">
                    <p>{{ errors.mobile_number }}</p>
                  </div>
                </div>

                <!-- Password Field -->
                <div class="mb-3 form-wrap-content">
                  <label for="password" class="form-label">Password</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-lock"></i>
                    </div>
                    <input
                      :type="showPassword ? 'text' : 'password'"
                      id="password"
                      v-model="form.password"
                      class="form-control"
                      placeholder="Enter Password"
                      required
                    />
                    <button
                      type="button"
                      class="info-icon btn btn-link"
                      @click="togglePasswordVisibility"
                      aria-label="Toggle Password Visibility"
                    >
                      <i :class="showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"></i>
                    </button>
                  </div>
                  <div class="error-wrap" v-if="errors.password">
                    <p>{{ errors.password }}</p>
                  </div>
                </div>

                <!-- Confirm Password Field -->
                <div class="mb-3 form-wrap-content">
                  <label for="confirmPassword" class="form-label">Confirm Password</label>
                  <div class="position-relative">
                    <div class="icon-email">
                      <i class="fa-solid fa-lock"></i>
                    </div>
                    <input
                      :type="showConfirmPassword ? 'text' : 'password'"
                      id="confirmPassword"
                      v-model="form.confirm_password"
                      class="form-control"
                      placeholder="Confirm Password"
                      required
                    />
                    <button
                      type="button"
                      class="info-icon btn btn-link"
                      @click="toggleConfirmPasswordVisibility"
                      aria-label="Toggle Confirm Password Visibility"
                    >
                      <i :class="showConfirmPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"></i>
                    </button>
                  </div>
                  <div class="error-wrap" v-if="errors.confirm_password">
                    <p>{{ errors.confirm_password }}</p>
                  </div>
                </div>

                <!-- Remember Me & Forgot Password -->
                <div class="d-flex justify-content-between align-items-center mb-3">
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      id="rememberMe"
                      v-model="form.remember_me"
                    />
                    <label class="form-check-label" for="rememberMe">
                      Remember me
                    </label>
                  </div>
                  <div class="forgot-password">
                    <a href="#" @click.prevent="forgotPassword">Forgot password?</a>
                  </div>
                </div>

                <!-- Submit Button -->
                <div class="button-wrap mb-3">
                  <button class="btn btn-primary w-100" type="submit" :disabled="isSubmitting">
                    <span
                      v-if="isSubmitting"
                      class="spinner-border spinner-border-sm"
                      role="status"
                      aria-hidden="true"
                    ></span>
                    Sign Up
                  </button>
                </div>
              </div>

              <!-- Hidden Close Button -->
              <button
                type="button"
                ref="hiddenCloseButton"
                class="d-none"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>

              <!-- Bottom Text -->
              <div class="bottom-text">
                <p>
                  Already have an account?
                  <a href="#" data-bs-toggle="modal" data-bs-target="#loginModal" @click.prevent="switchToLogin">Login Now!</a>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue';
import { useAuthStore } from '@/stores/auth';

export default {
  name: 'SignUp',
  setup() {
    const authStore = useAuthStore();

    const form = reactive({
      full_name: '',
      email: '',
      mobile_number: '',
      password: '',
      confirm_password: '',
      remember_me: false,
    });

    const errors = reactive({
      general: '',
      full_name: '',
      email: '',
      mobile_number: '',
      password: '',
      confirm_password: '',
    });

    const isSubmitting = ref(false);

    const showPassword = ref(false);
    const showConfirmPassword = ref(false);

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    const toggleConfirmPasswordVisibility = () => {
      showConfirmPassword.value = !showConfirmPassword.value;
    };

    const validateForm = () => {
      let isValid = true;

      // Reset errors
      Object.keys(errors).forEach((key) => (errors[key] = ''));

      // Full Name Validation
      if (!form.full_name.trim()) {
        errors.full_name = 'Full name is required.';
        isValid = false;
      }

      // Email Validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!form.email) {
        errors.email = 'Email is required.';
        isValid = false;
      } else if (!emailPattern.test(form.email)) {
        errors.email = 'Please enter a valid email address.';
        isValid = false;
      }

      const phonePattern = /^0?\d{9}$/;
      const sanitizedNumber = form.mobile_number ? form.mobile_number.replace(/\D/g, '') : '';

      if (!sanitizedNumber) {
        errors.mobile_number = 'Phone number is required.';
        isValid = false;
      } else if (!phonePattern.test(sanitizedNumber)) {
        errors.mobile_number = 'Please enter a 9-digit number or a 10-digit number starting with 0.';
        isValid = false;
      } else {
        form.mobile_number = sanitizedNumber;
      }

      // Password Validation
      if (!form.password) {
        errors.password = 'Password is required.';
        isValid = false;
      }

      // Confirm Password Validation
      if (!form.confirm_password) {
        errors.confirm_password = 'Please confirm your password.';
        isValid = false;
      } else if (form.password !== form.confirm_password) {
        errors.confirm_password = 'Passwords do not match.';
        isValid = false;
      }

      return isValid;
    };

    const hiddenCloseButton = ref(null);

    const handleRegister = async () => {
      if (!validateForm()) {
        return;
      }

      isSubmitting.value = true;
      errors.general = '';

      try {
        await authStore.register(form);
        hiddenCloseButton.value.click();
      } catch (apiErrors) {
        if (apiErrors) {
          Object.entries(apiErrors).forEach(([key, message]) => {
            if (key in errors) {
              errors[key] = message;
            } else {
              errors.general += message;
            }
          });
        } else {
          errors.general = 'An unexpected error occurred. Please try again later.';
        }
      } finally {
        isSubmitting.value = false;
        console.log
      }
    };

    const loginWithFacebook = () => {
      // Implement Facebook login logic
    };

    const loginWithGoogle = () => {
      // Implement Google login logic
    };

    const forgotPassword = () => {
      // Implement forgot password logic
    };

    // Function to switch to Login Modal
    const switchToLogin = () => {
      hiddenCloseButton.value.click();
    };

    return {
      form,
      errors,
      isSubmitting,
      showPassword,
      showConfirmPassword,
      togglePasswordVisibility,
      toggleConfirmPasswordVisibility,
      handleRegister,
      loginWithFacebook,
      loginWithGoogle,
      forgotPassword,
      switchToLogin,
      hiddenCloseButton,
    };
  },
};
</script>


<style scoped>
/* Add your styles here */

.icon-email {
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
  color: #6c757d;
}

.info-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: #dc3545;
  cursor: pointer;
}

.form-control {
  padding-left: 35px; /* Adjust based on icon size */
  padding-right: 35px; /* Adjust based on icon size */
}

.button-wrap .spinner-border {
  margin-right: 5px;
}

.btn-link {
  padding: 0;
}

.modal-search-dish .modal-dialog {
  max-width: 500px;
}

.bottom-text {
  margin-top: 10px;
}

.bottom-text a {
  color: #0d6efd;
  text-decoration: none;
}

.bottom-text a:hover {
  text-decoration: underline;
}

/* shubhams style */
.error-wrap {
  color: red;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.alert {
  margin-bottom: 1rem;
}

.alert-danger {
  color: #842029;
  background-color: #f8d7da;
  border-color: #f5c2c7;
  padding: 0.75rem 1.25rem;
  border: 1px solid transparent;
  border-radius: 0.25rem;
}

.position-relative {
  position: relative;
}

.icon-email {
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
  color: #6c757d;
}

.info-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: #dc3545;
  cursor: pointer;
}

.form-control {
  padding-left: 35px;
  padding-right: 35px;
}

.spinner-border {
  margin-right: 0.5rem;
}
</style>
