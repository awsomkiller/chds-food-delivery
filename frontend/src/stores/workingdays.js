import { defineStore } from 'pinia'
import axios from '../../axios'

export const useWorkingDaysStore = defineStore('workingDays', {
  state: () => ({
    offDays: ['2024-12-01'],
    pickup_time_slots: [],
    delivery_time_slots: [],
    schedule_date: "",
    schedule_time: "",
    isLoading: false,
    error: null
  }),
  
  actions: {
    /**
     * Fetches working days from the API using Axios and categorizes them.
     */
    async fetchTimeSlots() {
      this.isLoading = true
      this.error = null
      
      try {
        const response = await axios.get('/menu/timeslots/', {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        })
        
        const data = response.data
        
        this.workingdays = data;
        this.pickup_time_slots = data.filter(slot => slot.type === 'PICKUP ONLY' || slot.type === 'ALL');
        this.delivery_time_slots = data.filter(slot => slot.type === 'DELIVERY ONLY' || slot.type === 'ALL');
        
      } catch (error) {
        console.error('Error fetching working days:', error)
        this.error = error.message || 'An error occurred while fetching working days.'
      } finally {
        this.isLoading = false
      }
    },
     
    setScheduleDate(date){
      this.schedule_date = date;
    },

    setScheduleTime(timeslot) {
      this.schedule_time = timeslot;
    },
    
    async fetchOffDays() {
      try {
        const response = await axios.get("https://your-api-endpoint.com/offdays");
        this.offDays = response.data.offDays || [];
      } catch (error) {
        console.error("Error fetching OFF days:", error);
      }
    },
  }
})
