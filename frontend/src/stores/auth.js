import { defineStore } from 'pinia';
import axios from '../../axios';
import { useAddressStore } from './address';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
    delivery: false,
    profileImage: null,
    fullName: '',
    email: '',
    phoneNumber: '',
    street1: '',
    street2: '',
    suburb: '',
    pincode: '',
    city: '',
  }),

  actions: {
    async login(credentials) {
      try {
        const response = await axios.post('/login/', credentials);
        const { access_token, refresh_token } = response.data;

        this.accessToken = access_token;
        this.refreshToken = refresh_token;

        localStorage.setItem('accessToken', access_token);
        localStorage.setItem('refreshToken', refresh_token);

        axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
        this.fetchUserDetails()
        return response.data;
      } catch (error) {
        let errorMessage = 'An unexpected error occurred. Please try again.';
    
        if (error.response && error.response.data) {
          const errors = error.response.data;
    
          const formattedErrors = Object.values(errors)
            .flat()
            .join(' ');
    
          if (formattedErrors) {
            errorMessage = formattedErrors;
          }
        } else if (error.message) {
          errorMessage = error.message;
        }
    
        console.error('Login failed:', errorMessage);
        throw new Error(errorMessage);
      }
    },

    async fetchUserDetails() {
      try {
        if(this.accessToken){
          const response = await axios.get('/details/');
          this.user = response.data;
          localStorage.setItem('user', JSON.stringify(this.user));
          this.initializeProfile();
          return;
        } else{
          console.log("User not logged in");
        }
        
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
      }
    },

    deliveryEligibilityCheck(){
      const addressStore = useAddressStore()
      if(this.user.primary_address){
        const postal_code = this.user.primary_address.postal_code;
        const eligible_postal_code = addressStore.fetchEligiblePostalCodes();
        console.log(eligible_postal_code)
        this.delivery = eligible_postal_code.includes(parseInt(postal_code));
      }
    },

    async handlePasswordChange(payload) {
      try {
        await axios.post('/change-password/', payload);
      } catch (error) {
        console.error('Password Change failed:', error.response?.data || error.message);
        throw error;
      }
    },
    async register(credentials) {
      try {
        const response = await axios.post('/register-user/', credentials);
        await this.login({
          email: credentials.email,
          password: credentials.password,
        });
        return response.data;
      } catch (error) {
        console.error('Registration failed:', error.response?.data || error.message);

        if (error.response && error.response.data && error.response.data.errors) {
          const apiErrors = error.response.data.errors;
          const formattedErrors = {};

          Object.entries(apiErrors).forEach(([key, messages]) => {
            if (key in formattedErrors) {
              formattedErrors[key] += ` ${messages.join(' ')}`;
            } else {
              formattedErrors[key] = messages.join(' ');
            }
          });

          throw formattedErrors;
        } else {
          throw { general: 'An unexpected error occurred. Please try again later.' };
        }
      }
    },

    logout() {
      this.user = null;
      this.accessToken = null;
      this.refreshToken = null;

      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('user');

      delete axios.defaults.headers.common['Authorization'];
    },

    initializeAuth() {
      const accessToken = localStorage.getItem('accessToken');
      const refreshToken = localStorage.getItem('refreshToken');
      const user = JSON.parse(localStorage.getItem('user'));

      if (accessToken && refreshToken && user) {
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
        this.user = user;

        axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;
      }
    },
    getBillingAddress(){
      return this.formatAddressSingleLine(this.user.billing_address)
    },

    formatAddressSingleLine({
      street_address1,
      street_address2,
      suburbs,
      city,
      postal_code,
    }) {
      return [
        [street_address1, street_address2].filter(Boolean).join(', '),
        suburbs?.trim(),
        [city, postal_code].filter(Boolean).join(', '),
      ].filter(Boolean).join(', ');
    },
    setProfileImage(imageUrl) {
      this.profileImage = imageUrl;
    },
    setFirstName(name) {
      this.firstName = name;
    },
    setLastName(name) {
      this.lastName = name;
    },
    setEmail(email) {
      this.email = email;
    },
    setPhoneNumber(phone) {
      this.phoneNumber = phone;
    },
    setStreet1(street) {
      this.street1 = street;
    },
    setStreet2(street) {
      this.street2 = street;
    },
    setSuburb(suburb) {
      this.suburb = suburb;
    },
    setPincode(pincode) {
      this.pincode = pincode;
    },
    setState(state) {
      this.state = state;
    },
    async saveProfile() {
        const payload = { 
          profile_picture: this.profileImage,
          full_name:this.fullName, 
        };
        try{
          await axios.post('/details/', payload);
          await this.fetchUserDetails();
          this.fetchUserDetails();
        }
        catch (error) {
        console.error('Error saving profile:', error);
        throw error;
      }
    },
    initializeProfile(){  
      if(this.user){
        this.fullName = this.user.full_name ? this.user.full_name : ""
        this.email = this.user.email;
        this.phoneNumber = this.user.mobile_number;
        if(this.user.billing_address){
          this.street1 = this.user.billing_address.street_address1;
          this.street2 = this.user.billing_address.street_address2;
          this.suburbs = this.user.billing_address.suburbs;
          this.pincode = this.user.billing_address.pincode;
          this.city = this.user.billing_address.city;
        }
      } else {
        console.warn('User not found')
      }
    }
  },
});
