// stores/translation.js
import { defineStore } from 'pinia';
import axios from '../../axios';

export const useTranslationStore = defineStore('translation', {
  state: () => ({
    translations: [],            // All translations fetched from the backend
    modules: {},                 // Translations organized by module and language
    currentLanguage: 'en',       // Default language
    isLoaded: false,             // Flag to indicate if translations have been loaded
    isLoading: false,            // Flag to indicate if a fetch is in progress
    loadError: null,             // Store any error that occurs during fetch
  }),
  actions: {
    /**
     * Fetch translations from the backend.
     * If translations are already loaded, skip fetching.
     * Returns a promise that resolves when translations are ready.
     */
    async fetchTranslations() {
      if (this.isLoaded) {
        // Translations are already loaded; no need to fetch again
        return Promise.resolve();
      }

      if (this.isLoading) {
        // A fetch is already in progress; return the existing promise
        this.currentLanguage = this.getLanguageCode();
        return new Promise((resolve, reject) => {
          const checkLoaded = () => {
            if (this.isLoaded) {
              resolve();
            } else if (this.loadError) {
              reject(this.loadError);
            } else {
              setTimeout(checkLoaded, 100); // Polling every 100ms
            }
          };
          checkLoaded();
        });
      }

      this.isLoading = true;
      this.loadError = null;

      try {
        const response = await axios.get('/translations/all'); // Adjust the endpoint as needed
        this.translations = response.data;
        this.organizeTranslations();
        this.isLoaded = true;
      } catch (error) {
        console.error('Error fetching translations:', error);
        this.loadError = error;
        throw error; // Re-throw to allow handling in components
      } finally {
        this.isLoading = false;
      }
    },
    /**
     * Organize translations by module and language for efficient access.
     */
    organizeTranslations() {
      this.modules = {};

      this.translations.forEach((item) => {
        const { feature_code } = item.module;
        const { language, label, value } = item;

        if (!this.modules[feature_code]) {
          this.modules[feature_code] = {};
        }

        if (!this.modules[feature_code][language]) {
          this.modules[feature_code][language] = {};
        }

        this.modules[feature_code][language][label] = value;
      });
    },
    /**
     * Set the current language.
     * @param {string} lang - The language code to set (e.g., 'en', 'zh').
     */
    setLanguage(lang) {
      if (this.currentLanguage !== lang) {
        this.currentLanguage = lang;
      }
    },
    /**
     * Optional: Force reload translations, bypassing the cache.
     */
    async reloadTranslations() {
      this.isLoaded = false;
      await this.fetchTranslations();
    },
  },
  getters: {
    /**
     * Get all translations for the specified modules based on the current language.
     * @param {Array<string>} moduleCodes - Array of module feature codes.
     * @returns {Object} Combined translations from the specified modules.
     */
    getModuleTranslations: (state) => {
      return (moduleCodes) => {
        let combinedTranslations = {};

        moduleCodes.forEach((code) => {
          const moduleTranslations = state.modules[code]?.[state.currentLanguage];
          if (moduleTranslations) {
            combinedTranslations = { ...combinedTranslations, ...moduleTranslations };
          }
        });

        return combinedTranslations;
      };
    },
    /**
     * Retrieve a specific translation for a given label.
     * Accepts multiple module codes to handle labels present in multiple modules.
     * @param {string} label - The label key to translate.
     * @param {Array<string>} moduleCodes - Array of module feature codes.
     * @returns {string} The translated value or the label itself if not found.
     */
    translate: (state) => {
      return (label, moduleCodes = []) => {
        let translation = '';
        const code = moduleCodes[0];

        const moduleTranslations = state.modules[code]?.[state.currentLanguage];
        if (moduleTranslations && moduleTranslations[label]) {
          translation = moduleTranslations[label];
        }
        if (!translation) {
          // Fallback to English if current language translation is missing
          moduleCodes.forEach((code) => {
            const moduleTranslations = state.modules[code]?.['en'];
            if (moduleTranslations && moduleTranslations[label]) {
              translation = moduleTranslations[label];
            }
          });
        }

        if (!translation) {
          console.warn(`Missing translation for label: "${label}"`);
        }

        return translation || label;
      };
    },
    /**
     * Get sorted translations for specified modules.
     * @param {Array<string>} moduleCodes - Array of module feature codes.
     * @returns {Object} Sorted translations object.
     */
    getSortedModuleLabels: (state, getters) => {
      return (moduleCodes) => {
        const translations = getters.getModuleTranslations(moduleCodes);
        return Object.keys(translations)
          .sort()
          .reduce((acc, key) => {
            acc[key] = translations[key];
            return acc;
          }, {});
      };
    },
    getLanguageCode() {
      // Retrieve the browser's language setting
      const browserLanguage = navigator.language || navigator.userLanguage;
      console.log(browserLanguage);
      // Check if the language starts with 'zh' (covers all Chinese variants)
      if (browserLanguage.toLowerCase().startsWith('zh')) {
        return 'zh';
      } else {
        return 'en';
      }
    },
  },
});
