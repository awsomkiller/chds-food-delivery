import { defineStore } from 'pinia';
import axios from '../../axios';

export const useMenuStore = defineStore('menu', {
  state: () => ({
    items: [],
    cart: [],
    loading: false,
    error: null,
    nextPageUrl: '/menu/items/',
    searchQuery: '',
    selectedItem: {},
    categories: [],
    categoriesLoading: false,
    categoriesError: null,
    selectedCategory: "",
  }),
  getters: {
    isAllItemsLoaded: (state) => !state.nextPageUrl,
  },
  actions: {
    async loadItems() {
      if (this.loading || !this.nextPageUrl) return;

      this.loading = true;
      try {
        const params = { search: this.searchQuery };
        if (this.selectedCategory) {
          params.category = this.selectedCategory;
        }

        const response = await axios.get(this.nextPageUrl, { params });
        const data = response.data;

        this.items.push(...data.results);
        this.nextPageUrl = data.next;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async searchItems(query) {
      this.searchQuery = query;
      this.items = [];
      this.nextPageUrl = '/menu/items/';
      await this.loadItems();
    },
    async loadCategories() {
      if (this.categoriesLoading) return;

      this.categoriesLoading = true;
      try {
        const response = await axios.get('/menu/category/');
        this.categories = response.data.results;
      } catch (error) {
        this.categoriesError = error;
      } finally {
        this.categoriesLoading = false;
      }
    },
    selectCategory(category) {
      this.selectedCategory = category;
      this.items = [];
      this.nextPageUrl = '/menu/items/';
      this.loadItems();
    },
    updateSelectedItem(item) {
      this.selectedItem = item;
    },
    resetItems() {
      this.items = [];
      this.nextPageUrl = '/menu/items/';
    },
  },
});
