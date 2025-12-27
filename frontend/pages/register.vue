<template>
  <div class="register-page">
    <div class="form-container">
      <h1>Register</h1>
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            v-model="formData.username"
            required
            placeholder="Choose a username"
          />
        </div>
        <div class="form-group">
          <label for="email">Email: <span class="helper-text">(can be used to login)</span></label>
          <input
            type="email"
            id="email"
            v-model="formData.email"
            required
            placeholder="Enter your email"
          />
        </div>
        <div class="form-group">
          <label for="first_name">First Name:</label>
          <input
            type="text"
            id="first_name"
            v-model="formData.first_name"
            placeholder="Your first name"
          />
        </div>
        <div class="form-group">
          <label for="last_name">Last Name:</label>
          <input
            type="text"
            id="last_name"
            v-model="formData.last_name"
            placeholder="Your last name"
          />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            v-model="formData.password"
            required
            placeholder="Choose a strong password"
          />
        </div>
        <div class="form-group">
          <label for="password2">Confirm Password:</label>
          <input
            type="password"
            id="password2"
            v-model="formData.password2"
            required
            placeholder="Confirm your password"
          />
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Registering...' : 'Register' }}
        </button>
        <div v-if="error" class="error">{{ error }}</div>
        <div v-if="success" class="success">{{ success }}</div>
      </form>
      <p class="login-link">
        Already have an account? <NuxtLink to="/login">Login here</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()

const formData = ref({
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  password: '',
  password2: ''
})

const error = ref('')
const success = ref('')
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

const handleRegister = async () => {
  error.value = ''
  success.value = ''
  loading.value = true

  const result = await authStore.register(formData.value)

  if (result.success) {
    success.value = 'Registration successful! Redirecting to login...'
    setTimeout(() => {
      navigateTo('/login')
    }, 2000)
  } else {
    error.value = result.error || 'Registration failed. Please try again.'
  }

  loading.value = false
}
</script>

<style scoped>
.register-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
  padding: 2rem 1rem;
}

.form-container {
  background-color: white;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
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

.helper-text {
  font-weight: normal;
  font-size: 0.85em;
  color: #42b983;
  font-style: italic;
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
  margin-top: 1rem;
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

.success {
  margin-top: 1rem;
  padding: 0.75rem;
  background-color: #efe;
  color: #3c3;
  border-radius: 4px;
  font-size: 0.9em;
}

.login-link {
  margin-top: 1.5rem;
  text-align: center;
  color: #666;
}

.login-link a {
  color: #42b983;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>

