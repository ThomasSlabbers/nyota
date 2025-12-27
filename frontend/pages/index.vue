<template>
  <div class="home">
    <h1>Welcome to Rapid Django Nuxt</h1>
    <p>A modern boilerplate for building web applications</p>
    
    <div class="api-test">
      <button @click="testApiConnection" class="btn-test" :disabled="testing">
        {{ testing ? 'Testing...' : 'Test API Connection' }}
      </button>
      
      <div v-if="apiStatus" class="api-status" :class="apiStatus.success ? 'success' : 'error'">
        <span class="status-icon">{{ apiStatus.success ? '✓' : '✗' }}</span>
        <span>{{ apiStatus.message }}</span>
      </div>
    </div>
    
    <div class="features">
      <h2>Features:</h2>
      <ul>
        <li>✓ Django REST Framework backend</li>
        <li>✓ Nuxt 3 frontend</li>
        <li>✓ JWT Authentication</li>
        <li>✓ Pinia State Management</li>
        <li>✓ Docker support</li>
        <li>✓ TypeScript ready</li>
      </ul>
    </div>
    
    <div v-if="!authStore.isAuthenticated" class="cta">
      <NuxtLink to="/register" class="btn">Get Started</NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const config = useRuntimeConfig()

const testing = ref(false)
const apiStatus = ref<{success: boolean, message: string} | null>(null)

const testApiConnection = async () => {
  testing.value = true
  apiStatus.value = null
  
  try {
    const response: any = await $fetch(`${config.public.apiBase}/auth/health/`)
    apiStatus.value = {
      success: true,
      message: response.message || 'API connection successful!'
    }
  } catch (error) {
    apiStatus.value = {
      success: false,
      message: 'Failed to connect to API. Make sure the backend is running.'
    }
  } finally {
    testing.value = false
  }
}

definePageMeta({
  layout: 'default'
})
</script>

<style scoped>
.home {
  text-align: center;
  padding: 3rem 1rem;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 1rem;
  color: #2c3e50;
}

p {
  font-size: 1.2em;
  color: #666;
  margin-bottom: 2rem;
}

.api-test {
  margin: 2rem auto;
  max-width: 600px;
}

.btn-test {
  padding: 0.75rem 1.5rem;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1em;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-test:hover:not(:disabled) {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.btn-test:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.api-status {
  margin-top: 1rem;
  padding: 1rem;
  border-radius: 5px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.api-status.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.api-status.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.status-icon {
  font-size: 1.2em;
  font-weight: bold;
}

.features {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  margin: 2rem auto;
  max-width: 600px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.features h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.features ul {
  list-style: none;
  padding: 0;
  text-align: left;
}

.features li {
  font-size: 1.1em;
  margin: 0.8rem 0;
  color: #42b983;
  padding-left: 1.5rem;
}

.cta {
  margin-top: 3rem;
}

.btn {
  display: inline-block;
  padding: 1rem 2rem;
  background-color: #42b983;
  color: white;
  border-radius: 5px;
  font-size: 1.1em;
  font-weight: 500;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #35a372;
}
</style>

