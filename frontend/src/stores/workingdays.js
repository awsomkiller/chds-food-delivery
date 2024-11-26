// stores/workingdays.js
import { defineStore } from 'pinia'
import axios from '../../axios'

export const useWorkingDaysStore = defineStore('workingDays', {
  state: () => ({
    workingdays: [],
    pickupdays: [],
    deliverydays: [],
    activePickUpDay: {},
    activeDeliveryDay: {},
    activeDeliveryTimeSlot: {},
    activePickupTimeSlot: {},
    isLoading: false,
    error: null
  }),
  
  actions: {
    /**
     * Fetches working days from the API using Axios and categorizes them.
     */
    async fetchWorkingDays() {
      this.isLoading = true
      this.error = null
      
      try {
        const response = await axios.get('/menu/working-days/', {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        })
        
        const data = response.data
        
        this.workingdays = data
        this.pickupdays = data.filter(day => 
          day.time_slot.some(slot => slot.type === 'PICKUP ONLY' || slot.type === 'ALL')
        )
        this.deliverydays = data.filter(day => 
          day.time_slot.some(slot => slot.type === 'DELIVERY ONLY' || slot.type === 'ALL')
        )
        
      } catch (error) {
        console.error('Error fetching working days:', error)
        this.error = error.message || 'An error occurred while fetching working days.'
      } finally {
        this.isLoading = false
      }
    },
    
    /**
     * Sets the active delivery day based on selected date.
     * @param {Number} dayId - The ID of the selected delivery day.
     */
    setActiveDeliveryDay(dayId) {
      const selectedDay = this.deliverydays.find(day => day.id === parseInt(dayId))
      if (selectedDay) {
        this.activeDeliveryDay = selectedDay
        // Optionally, set a default time slot
        if (selectedDay.time_slot.length > 0) {
          this.setActiveDeliveryTimeSlot(selectedDay.time_slot[0].id)
        } else {
          this.activeDeliveryTimeSlot = {}
        }
      } else {
        this.activeDeliveryDay = {}
        this.activeDeliveryTimeSlot = {}
      }
    },
    
    /**
     * Sets the active delivery time slot based on selected time slot ID.
     * @param {Number} timeSlotId - The ID of the selected time slot.
     */
    setActiveDeliveryTimeSlot(timeSlotId) {
      if (this.activeDeliveryDay && this.activeDeliveryDay.time_slot) {
        const selectedSlot = this.activeDeliveryDay.time_slot.find(slot => slot.id === parseInt(timeSlotId))
        if (selectedSlot) {
          this.activeDeliveryTimeSlot = selectedSlot
        } else {
          this.activeDeliveryTimeSlot = {}
        }
      }
    },
    
    /**
     * Sets the active pickup day based on selected date.
     * @param {Number} dayId - The ID of the selected pickup day.
     */
    setActivePickupDay(dayId) {
      const selectedDay = this.pickupdays.find(day => day.id === parseInt(dayId))
      if (selectedDay) {
        this.activePickUpDay = selectedDay
        // Optionally, set a default time slot
        if (selectedDay.time_slot.length > 0) {
          this.setActivePickupTimeSlot(selectedDay.time_slot[0].id)
        } else {
          this.activePickupTimeSlot = {}
        }
      } else {
        this.activePickUpDay = {}
        this.activePickupTimeSlot = {}
      }
    },
    
    /**
     * Sets the active pickup time slot based on selected time slot ID.
     * @param {Number} timeSlotId - The ID of the selected time slot.
     */
    setActivePickupTimeSlot(timeSlotId) {
      if (this.activePickUpDay && this.activePickUpDay.time_slot) {
        const selectedSlot = this.activePickUpDay.time_slot.find(slot => slot.id === parseInt(timeSlotId))
        if (selectedSlot) {
          this.activePickupTimeSlot = selectedSlot
        } else {
          this.activePickupTimeSlot = {}
        }
      }
    },
  }
})
