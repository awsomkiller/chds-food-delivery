<script setup >

const orderNumber = '#' + Math.floor(Math.random() * 1000000).toString().padStart(6, '0')
</script>

<template>
  <div class="order-success">
    <Header />
    
    <main class="main-content">
      <div class="success-container">
        <div class="success-content">
          <div class="icon-wrapper">
            <svg class="check-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 13l4 4L19 7" />
            </svg>
          </div>
          
          <h1 class="title">Order Placed Successfully!</h1>
          
          <p class="order-number">
            Thank you for your order. Your order number is {{ orderNumber }}
          </p>
          
          <div class="card">
            <div class="card-content">
              <div class="image-container">
                <img src="https://cdn-icons-png.flaticon.com/512/4108/4108921.png" 
                     alt="Order Success" />
              </div>
              
              <div class="info-section">
                <p class="confirmation-text">
                  We'll send you a confirmation email with your order details and tracking information.
                </p>
                
                <div class="button-container">
                  <router-link to="/" class="continue-button">
                    Continue Shopping
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    
    <Footer />
  </div>
</template>

<style scoped>
.order-success {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex-grow: 1;
  padding: 2rem 1rem;
}

.success-container {
  max-width: 600px;
  margin: 0 auto;
  padding-top: 2rem;
}

.success-content {
  text-align: center;
}

.icon-wrapper {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 3rem;
  height: 3rem;
  background-color: #ecfdf5;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  box-shadow: 0 0 15px rgba(52, 211, 153, 0.3);
  animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.check-icon {
  width: 1.5rem;
  height: 1.5rem;
  stroke: #059669;
  stroke-width: 2;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.title {
  font-size: 2rem;
  font-weight: 800;
  margin: 1rem 0;
  background: linear-gradient(120deg, #4f46e5, #34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: slide-up 0.6s ease-out;
}

.order-number {
  font-size: 1.125rem;
  color: #4b5563;
  margin-bottom: 2rem;
  animation: fade-in 0.8s ease-out;
}

.card {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: scale-in 0.7s ease-out;
}

.card-content {
  padding: 1.5rem;
}

.image-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.image-container img {
  width: 120px;
  height: 120px;
  object-fit: contain;
  animation: float 3s ease-in-out infinite;
}

.info-section {
  border-top: 1px solid #e5e7eb;
  padding-top: 1.5rem;
}

.confirmation-text {
  color: #6b7280;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.button-container {
  display: flex;
  justify-content: center;
}

.continue-button {
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background-color: #4f46e5;
  color: white;
  font-weight: 500;
  border-radius: 0.375rem;
  transition: all 0.3s ease;
  text-decoration: none;
}

.continue-button:hover {
  background-color: #4338ca;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

.continue-button:active {
  transform: translateY(0);
}

@media (min-width: 640px) {
  .main-content {
    padding: 3rem 2rem;
  }

  .title {
    font-size: 2.5rem;
  }

  .image-container img {
    width: 150px;
    height: 150px;
  }
}

@keyframes bounce-in {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); opacity: 1; }
}

@keyframes slide-up {
  0% { transform: translateY(20px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes fade-in {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes scale-in {
  0% { transform: scaleY(0.95); opacity: 0; }
  100% { transform: scaleY(1); opacity: 1; }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
</style>