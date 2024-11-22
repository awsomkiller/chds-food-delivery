import { defineStore } from 'pinia'
import axios from '../../axios'

export const useMenuStore = defineStore('menu', {
  state: () => ({
    items: [],
    cart: [],
    loading: false,
    error: null,
    nextPageUrl: '/menu-items/',
    searchQuery: '',
    selectedItem:{},
  }),
  getters: {
    isAllItemsLoaded: (state) => !state.nextPageUrl,
    cartItemCount: (state) =>
      state.cart.reduce((total, item) => total + item.quantity, 0),
    cartTotalPrice: (state) =>
      state.cart.reduce((total, item) => total + item.price * item.quantity, 0),
  },
  actions: {
    async loadItems() {
      if (this.loading || !this.nextPageUrl) return

      this.loading = true
      try {
        const response = await axios.get(this.nextPageUrl, {
          params: { search: this.searchQuery },
        })
        const data = response.data

        this.items.push(...data.results)

        this.nextPageUrl = data.next
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },
    async searchItems(query) {
      this.searchQuery = query
      this.items = []
      this.nextPageUrl = '/menu-items/'
      await this.loadItems()
    },
    addToCart(item) {
      const cartItem = this.cart.find((ci) => ci.name === item.name)
      if (cartItem) {
        cartItem.quantity += 1
      } else {
        this.cart.push({ ...item, quantity: 1 })
      }
    },
    removeFromCart(item) {
      const index = this.cart.findIndex((ci) => ci.name === item.name)
      if (index !== -1) {
        this.cart.splice(index, 1)
      }
    },
    updateCartItemQuantity(item, quantity) {
      const cartItem = this.cart.find((ci) => ci.name === item.name)
      if (cartItem) {
        cartItem.quantity = quantity
        if (cartItem.quantity <= 0) {
          this.removeFromCart(item)
        }
      }
    },
    updateSelectedItem(item){
        this.selectedItem = item;
    }
  },
})
