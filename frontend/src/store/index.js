import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state() {
    return {
      goLinks: [],
      isOpen: true,
      currentGoLink: null,
      teamMembers: [],
      userDetail: {
        picture: '/static/img/dummy_profile.jpg',
        first_name: '-',
        last_name: '-',
        date_joined: '-',
        organization: '-',
        categories: [],
        apps: [],
        selectedApp: null,
        app_links: [],
        appDetails: null,
      },
      goLinkShortpath: '',
    };
  },
  getters: {
    getLinks: (state) => state.goLinks,
    getLink: (state) => state.currentGoLink,
    getMembers: (state) => state.teamMembers,
    getFavoriteGoLinks: (state) => state.favouriteGoLinks,
    getUserDetails: (state) => state.userDetail,
    getGoLinkShortpath: (state) => state.goLinkShortpath,
    getCategories: (state) => state.categories,
    getApps: (state) => state.apps,
    getSelectedApp: (state) => state.selectedApp,
    getAppLinks: (state) => state.app_links,
    getAppDetails: (state) => state.appDetails,
  },

  mutations: {
    setLinks(state, links) {
      state.goLinks = links;
    },
    setUserDetail(state, user) {
      state.userDetail = user;
    },
    setIsOpen(state, isOpen) {
      state.isOpen = isOpen;
    },
    setCurrentGoLink(state, link) {
      state.currentGoLink = link;
    },
    addLink(state, link) {
      state.goLinks.push(link);
    },
    updateLink(state, updatedLink) {
      const index = state.goLinks.findIndex(
        (link) => link.id === updatedLink.id,
      );
      if (index !== -1) {
        state.goLinks.splice(index, 1, updatedLink);
      }
    },
    addFavourite(state, id) {
      const item = state.goLinks.find(() => item.id === id);
      if (item) {
        item.favourite = true; // Assuming there is an 'isFavourite' property
      }
    },

    deleteFavourite(state, id) {
      const item = state.goLinks.find(() => item.id === id);
      if (item) {
        item.favourite = false; // Assuming there is an 'isFavourite' property
      }
    },
    setMembers(state, members) {
      state.teamMembers = members;
    },
    setGoLinkShortpath(state, shortpath) {
      state.goLinkShortpath = shortpath;
    },
    setApps(state, apps) {
      state.apps = apps;
    },
    setCategories(state, categories) {
      state.categories = categories;
    },
    setSelectedApps(state, selectedApp) {
      state.selectedApp = selectedApp;
    },
    setAppLinks(state, appLinks) {
      state.app_links = appLinks;
    },
    setAppDetails(state, appDetails) {
      state.appDetails = appDetails;
    },
  },
  actions: {
    async getLinks(context) {
      try {
        const response = await axios.get('/link/');
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setLinks', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    // eslint-disable-next-line consistent-return
    async createLink(context, newLinkData) {
      try {
        const payload = JSON.stringify(newLinkData);
        const response = await axios.post('/link/', payload);
        if (response.status === 201) {
          context.dispatch('getLinks');
          return { success: true };
        }
      } catch (error) {
        return { success: false, errors: error.response.data };
      }
    },

    // eslint-disable-next-line consistent-return
    async updateLink(context, updatedLinkData) {
      try {
        const { id, ...payload } = updatedLinkData;
        const response = await axios.patch(`/link/${id}/`, payload);
        if (response.status === 206) {
          context.dispatch('getLinks');
          context.commit('setCurrentGoLink', response.data);
          return { success: true };
        }
      } catch (error) {
        return { success: false, errors: error.response.data };
      }
    },

    async getTeamMember(context) {
      try {
        const response = await axios.get('/team/list/');
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setMembers', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async FetchFavouriteGoLinks(context) {
      try {
        const response = await axios.get('/favourite/list/');
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setMembers', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async searchLinks(context, searchTerm) {
      try {
        const response = await axios.get(
          `/link/shortlinks/?search=${searchTerm}`,
        );
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setLinks', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async deleteLink(context, id) {
      try {
        const response = await axios.delete(`/link/${id}/`);
        if (response.status === 204) {
          context.dispatch('getLinks');
        } else {
          throw new Error('Failed to update link');
        }
      } catch (error) {
        console.error('Error Deleting link:', error);
      }
    },
    async userdetails(context) {
      try {
        const response = await axios.get('/user/details/');
        if (response.status === 200) {
          context.commit('setUserDetail', response.data);
        }
      } catch (errors) {
        console.log(errors);
      }
    },
    // eslint-disable-next-line consistent-return
    async updateDetails(context, newUserDetails) {
      try {
        const payload = JSON.stringify(newUserDetails);
        const response = await axios.patch('/user/details/update/', payload);
        if (response.status === 206) {
          return { success: true };
        }
      } catch (error) {
        return { success: false, errors: error.response.data };
      }
    },

    async getCategories(context) {
      try {
        const response = await axios.get('/store/categories/');
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setCategories', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async getApps(context, slug = '') {
      try {
        const response = await axios.get(`/store/apps/${slug}`);
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setApps', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async getAppLinks(context, id) {
      try {
        const response = await axios.get(`/store/app/${id}/links/`);
        if (response.status < 200 || response.status >= 300) {
          context.commit('setAppLinks', []);
        }
        const { data } = response;
        context.commit('setAppLinks', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async getAppDetails(context, id) {
      try {
        const response = await axios.get(`/store/app/${id}/details/`);
        if (response.status < 200 || response.status >= 300) {
          throw new Error('Failed to fetch data');
        }
        const { data } = response;
        context.commit('setAppDetails', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

  },
  modules: {},
});
