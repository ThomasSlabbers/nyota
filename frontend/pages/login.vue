<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="auth-header">
        <h1>Welcome back</h1>
        <p>Sign in to continue to Nyota Catalyst</p>
      </div>
      
      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-field">
          <label for="username">Username or Email</label>
          <input
            type="text"
            id="username"
            v-model="username"
            required
            placeholder="Enter your username or email"
          />
        </div>
        
        <div class="form-field">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder="Enter your password"
          />
        </div>
        
        <button type="submit" class="btn-submit" :disabled="loading">
          {{ loading ? 'Signing in...' : 'Sign in' }}
        </button>
        
        <div v-if="error" class="alert alert-error">{{ error }}</div>
      </form>
      
      <div class="auth-footer">
        <p>Don't have an account? <NuxtLink to="/register">Apply now</NuxtLink></p>
      </div>
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
* {
  box-sizing: border-box;
}

.auth-page {
  min-height: calc(100vh - 80px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  background: #fafafa;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
}

.auth-container {
  width: 100%;
  max-width: 420px;
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
  padding: 3rem 2.5rem;
}

.auth-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.auth-header h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #0a0a0a;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.auth-header p {
  font-size: 0.9375rem;
  color: #525252;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-field label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #0a0a0a;
}

.form-field input {
  width: 100%;
  padding: 0.875rem 1rem;
  font-size: 0.9375rem;
  color: #0a0a0a;
  background: #ffffff;
  border: 1px solid #d4d4d4;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.form-field input::placeholder {
  color: #a3a3a3;
}

.form-field input:focus {
  outline: none;
  border-color: #0a0a0a;
}

.btn-submit {
  width: 100%;
  padding: 0.875rem 1rem;
  margin-top: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #ffffff;
  background: #0a0a0a;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-submit:hover:not(:disabled) {
  background: #262626;
  transform: translateY(-1px);
}

.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.alert {
  padding: 0.875rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
}

.alert-error {
  background: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

.auth-footer {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e5e5e5;
  text-align: center;
}

.auth-footer p {
  font-size: 0.9375rem;
  color: #525252;
}

.auth-footer a {
  color: #0a0a0a;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.2s;
}

.auth-footer a:hover {
  color: #0066ff;
}

@media (max-width: 768px) {
  .auth-container {
    padding: 2rem 1.5rem;
  }

  .auth-header h1 {
    font-size: 1.75rem;
  }
}
</style>

