import { defineStore } from 'pinia';
import axios from 'axios';

export const useWalletStore = defineStore('wallet', {
  state: () => ({
    balance: 0.00,
    currency: 'AUD',
    transactions: [],
    loading: false,
    error: null,
  }),
  
  getters: {
    getBalance: (state) => state.balance,
    getCurrency: (state) => state.currency,
    getTransactions: (state) => state.transactions,
    isLoading: (state) => state.loading,
    getError: (state) => state.error,
  },
  
  actions: {
    /**
     * Fetch the wallet details from the backend.
     */
    async fetchWallet() {
      this.loading = true;
      this.error = null;
      
      try {
        const response = await axios.get('/api/wallet/'); // Adjust the endpoint as needed
        this.balance = parseFloat(response.data.balance);
        this.currency = response.data.currency;
      } catch (err) {
        this.error = err.response?.data?.message || 'Failed to fetch wallet.';
        console.error('Error fetching wallet:', err);
      } finally {
        this.loading = false;
      }
    },
    
    /**
     * Fetch the transaction history.
     */
    async fetchTransactions() {
      this.loading = true;
      this.error = null;
      
      try {
        const response = await axios.get('/api/wallet/transactions/'); // Adjust the endpoint
        this.transactions = response.data.transactions.map(tx => ({
          id: tx.transaction_id,
          amount: parseFloat(tx.amount),
          currency: tx.currency,
          type: tx.operation_type, // 'CREDIT' or 'DEBIT'
          orderType: tx.order_type,
          status: tx.status,
          createdAt: tx.created_at,
          description: tx.description,
        }));
      } catch (err) {
        this.error = err.response?.data?.message || 'Failed to fetch transactions.';
        console.error('Error fetching transactions:', err);
      } finally {
        this.loading = false;
      }
    },
    
    /**
     * Recharge the wallet.
     * @param {Number} amount - The amount to recharge.
     */
    async rechargeWallet(amount) {
      this.loading = true;
      this.error = null;
      
      try {
        const payload = {
          amount: amount,
        };
        
        const response = await axios.post('/transactions/wallet/recharge/', payload);
        
        // Update the wallet balance and add the new transaction
        if (response.data.status === 'succeeded') {
          this.balance += amount;
          this.transactions.unshift({
            id: response.data.transaction_id,
            amount: amount,
            currency: this.currency,
            type: 'CREDIT',
            orderType: 'WALLET_RECHARGE',
            status: response.data.status,
            createdAt: new Date(),
            description: 'Wallet Recharge',
            receiptUrl: response.data.receipt_url,
          });
        }
        
        return response.data; // Return response for further handling if needed
      } catch (err) {
        this.error = err.response?.data?.message || 'Failed to recharge wallet.';
        console.error('Error recharging wallet:', err);
        throw err; // Re-throw for component-level handling
      } finally {
        this.loading = false;
      }
    },
    
    /**
     * Make a payment using the wallet.
     * @param {Number} amount - The amount to debit.
     * @param {String} orderId - The order ID for the transaction.
     */
    async makePayment(amount, orderId) {
      this.loading = true;
      this.error = null;
      
      try {
        const payload = {
          amount: amount,
          order_id: orderId, // Adjust based on your API requirements
        };
        
        const response = await axios.post('/api/orders/create/', payload);
        
        // Update the wallet balance and add the new transaction
        if (response.data.status === 'ORDER_PLACED') {
          this.balance -= amount;
          this.transactions.unshift({
            id: response.data.transaction_id,
            amount: amount,
            currency: this.currency,
            type: 'DEBIT',
            orderType: 'FOOD_ORDER',
            status: 'ORDER_PLACED',
            createdAt: new Date(),
            description: `Order #${orderId}`,
          });
        }
        
        return response.data;
      } catch (err) {
        this.error = err.response?.data?.message || 'Failed to make payment.';
        console.error('Error making payment:', err);
        throw err;
      } finally {
        this.loading = false;
      }
    },
  },
});
