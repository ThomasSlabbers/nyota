<template>
  <div class="login-page">
    <div class="form-container">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Username or Email:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            required
            placeholder="Enter your username or email"
          />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder="Enter your password"
          />
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
        <div v-if="error" class="error">{{ error }}</div>
      </form>
      <p class="signup-link">
        Don't have an account? <NuxtLink to="/register">Register here</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

definePageMeta({
  layout: 'default',
  middleware: (to, from) => {
    const authStore = useAuthStore()
    if (authStore.isAuthenticated) {
      return navigateTo('/dashboard')
    }
  }
})

const handleLogin = async () => {
  error.value = ''
  loading.value = true

  const result = await authStore.login(username.value, password.value)

  if (result.success) {
    await navigateTo('/dashboard')
  } else {
    error.value = result.error || 'Login failed. Please check your credentials.'
  }

  loading.value = false
}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.form-container {
  background-color: white;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

h1 {
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1em;
}

input:focus {
  outline: none;
  border-color: #42b983;
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1em;
  font-weight: 500;
  transition: background-color 0.3s;
}

button:hover:not(:disabled) {
  background-color: #35a372;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error {
  margin-top: 1rem;
  padding: 0.75rem;
  background-color: #fee;
  color: #c33;
  border-radius: 4px;
  font-size: 0.9em;
}

.signup-link {
  margin-top: 1.5rem;
  text-align: center;
  color: #666;
}

.signup-link a {
  color: #42b983;
  text-decoration: none;
}

.signup-link a:hover {
  text-decoration: underline;
}
</style>

