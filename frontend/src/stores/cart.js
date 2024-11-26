import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => ({
    cart: [],
    totalQty: 0,
    TotalOrderPrice: 0,
    active: {
      id: 1,
      meal_name: '',
      selected_meal_portion_id: null,
      selected_meal_portion_name: '',
      selected_meal_portion_weight: 0,
      selected_meal_portion_price: 0,
      selected_meal_addon_price: 0,
      addons: [],
      quantity: 1,
      total_price: 0,
    },
  }),
  actions: {
    addToCart(item) {
      this.active.meal_name = item.name;
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
  },
});
