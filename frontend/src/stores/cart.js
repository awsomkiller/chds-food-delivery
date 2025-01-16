import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => ({
    cart: [],
    totalQty: 0,
    TotalOrderPrice: 0,
    TotalDiscount: 0,
    active: {
      id: 1,
      meal_name: '',
      meal_id:null,
      selected_meal_portion_id: null,
      selected_meal_portion_name: '',
      selected_meal_portion_weight: 0,
      selected_meal_portion_price: 0,
      selected_meal_addon_price: 0,
      selected_meal_portion_protein: 0,
      selected_meal_portion_carbs: 0,
      selected_meal_portion_fat: 0,
      selected_meal_portion_calories: 0,
      isMealSet: false,
      addons: [],
      quantity: 1,
      total_price: 0,
      discount: 0,
    },
    appliedCoupon:null,
  }),
  actions: {
    addToCart(item) {
      this.active.meal_name = item.name;
      this.active.meal_id = item.id;
      const newItem = { ...this.active };
      this.cart.push(newItem);
      this.updateTotal();
      this.resetActive();
    },
    resetActive() {
      this.active = {
        id: this.generateId(),
        meal_name: '',
        selected_meal_portion_id: null,
        selected_meal_portion_name: '',
        selected_meal_portion_weight: 0,
        selected_meal_portion_price: 0,
        selected_meal_addon_price: 0,
        addons: [],
        quantity: 1,
        total_price: 0,
      };
    },
    generateId() {
      return this.cart.length > 0 ? this.cart[this.cart.length - 1].id + 1 : 1;
    },
    updateTotal() {
      this.totalQty = this.cart.reduce((sum, item) => sum + item.quantity, 0);
      this.TotalOrderPrice = this.cart.reduce((sum, item) => sum + item.total_price, 0);
    },
    removeFromCart(id) {
      this.cart = this.cart.filter(item => item.id !== id);
      this.cart.forEach((item, index) => {
        item.id = index + 1;
      });
      this.updateTotal();
    },
    updateActivePortion(portion) {
      this.active.selected_meal_portion_id = portion.id;
      this.active.selected_meal_portion_name = portion.portion_name;
      this.active.selected_meal_portion_weight = portion.portion_weight;
      this.active.selected_meal_portion_price = parseFloat(portion.price);
      this.active.selected_meal_portion_protein = portion.protein;
      this.active.selected_meal_portion_carbs = portion.carbs;
      this.active.selected_meal_portion_fat = portion.fats;
      this.active.selected_meal_portion_calories = portion.calories;
      this.active.isMealSet = portion.portion_code === "meal_set" ? true : false;
      this.active.addons = [];
      this.updateActiveTotalPrice();
    },
    updateActiveAddons() {
      const addonTotal = this.active.addons.reduce((sum, addon) => sum + parseFloat(addon.price), 0);
      this.active.selected_meal_addon_price = addonTotal;
      this.updateActiveTotalPrice();
    },
    updateActiveQuantity(quantity) {
      if (quantity < 1) {
        quantity = 1;
      }
      this.active.quantity = quantity;
      this.updateActiveTotalPrice();
    },
    updateActiveTotalPrice() {
      const itemPrice = parseFloat(this.active.selected_meal_portion_price);
      const addonPrice = parseFloat(this.active.selected_meal_addon_price)
      const totalPrice = (itemPrice + addonPrice) * this.active.quantity;
      this.active.total_price = totalPrice;
    },
    increaseItemQuantity(itemId) {
      const item = this.cart.find(item => item.id === itemId);
      if (item) {
        item.quantity += 1;
        item.total_price = item.quantity * item.selected_meal_portion_price;
        this.updateTotal();
      }
    },
    decreaseItemQuantity(itemId) {
      const item = this.cart.find(item => item.id === itemId);
      if (item) {
        item.quantity -= 1;
        if (item.quantity <= 0) {
          this.removeFromCart(itemId);
        } else {
          item.total_price = item.quantity * item.selected_meal_portion_price;
        }
        this.updateTotal();
      }
    },
    resetCart() {
      this.$reset();
    },

    applyCoupon(coupon) {
      if (!coupon || !coupon.is_active) {
        throw new Error('Invalid or inactive coupon.');
      }

      this.appliedCoupon = coupon;
      this.calculateDiscount();
    },

    unapplyCoupon() {
      this.appliedCoupon = null;
      this.TotalDiscount = 0;
    },

    calculateDiscount() {
      if (!this.appliedCoupon) {
        this.TotalDiscount = 0;
        return;
      }

      const discountType = this.appliedCoupon.discount_type;
      const discountValue = parseFloat(this.appliedCoupon.discount_upto);

      switch (discountType) {
        case 'PERCENTAGE':{
          this.TotalDiscount = (discountValue / 100) * this.TotalOrderPrice;
          break;
        }
        case 'FIXED_ORDER':{
          this.TotalDiscount = discountValue;
          // Ensure that discount does not exceed the total order price
          if (this.TotalDiscount > this.TotalOrderPrice) {
            this.TotalDiscount = this.TotalOrderPrice;
          }
          break;
        }
        case 'FIXED_ITEM':{
          // Apply fixed discount per item quantity
          const totalItems = this.cart.reduce((sum, item) => sum + item.quantity, 0);
          this.TotalDiscount = discountValue * totalItems;
          // Ensure that discount does not exceed the total order price
          if (this.TotalDiscount > this.TotalOrderPrice) {
            this.TotalDiscount = this.TotalOrderPrice;
          }
          break;
        }
        default:{
          this.TotalDiscount = 0;
          break;
        }
      }
    },
  },
});
