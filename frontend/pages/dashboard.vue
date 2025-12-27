<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="authStore.user" class="user-info">
      <h2>Welcome, {{ authStore.user.username }}!</h2>
      <div class="info-card">
        <p><strong>Email:</strong> {{ authStore.user.email }}</p>
        <p><strong>First Name:</strong> {{ authStore.user.first_name || 'Not set' }}</p>
        <p><strong>Last Name:</strong> {{ authStore.user.last_name || 'Not set' }}</p>
        <p><strong>User ID:</strong> {{ authStore.user.id }}</p>
      </div>
    </div>
    <div v-else-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const loading = ref(true)
const error = ref('')

definePageMeta({
  layout: 'default',
  middleware: (to, from) => {
    const authStore = useAuthStore()
    if (!authStore.isAuthenticated) {
      return navigateTo('/login')
    }
  }
})

onMounted(async () => {
  try {
    if (!authStore.user) {
      await authStore.fetchUser()
    }
  } catch (e: any) {
    error.value = 'Failed to load user data.'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.dashboard {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

h1 {
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
}

h2 {
  color: #42b983;
  margin-bottom: 1.5rem;
}

.loading {
  text-align: center;
  font-size: 1.2em;
  color: #666;
}

.user-info {
  text-align: left;
}

.info-card {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.info-card p {
  margin: 1rem 0;
  font-size: 1.1em;
  color: #2c3e50;
}

.error {
  padding: 1rem;
  background-color: #fee;
  color: #c33;
  border-radius: 4px;
  text-align: center;
}
</style>

