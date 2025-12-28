<template>
  <div id="app">
    <nav class="nav">
      <div class="nav-container">
        <NuxtLink to="/" class="nav-logo">Nyota Catalyst</NuxtLink>
        <div class="nav-links">
          <NuxtLink to="/founders" class="nav-link">Founders</NuxtLink>
          <template v-if="!authStore.isAuthenticated">
            <NuxtLink to="/login" class="nav-link">Sign in</NuxtLink>
            <NuxtLink to="/register" class="nav-button">Apply now</NuxtLink>
          </template>
          <template v-else>
            <NuxtLink to="/dashboard" class="nav-link">Dashboard</NuxtLink>
            <button @click="handleLogout" class="nav-button">Sign out</button>
          </template>
        </div>
      </div>
    </nav>
    <main>
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()

onMounted(() => {
  authStore.initFromStorage()
})

const handleLogout = () => {
  authStore.logout()
  navigateTo('/login')
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
  color: #0a0a0a;
  background: #ffffff;
}

/* Navigation */
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #e5e5e5;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.25rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo {
  font-size: 1.25rem;
  font-weight: 600;
  color: #0a0a0a;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-link {
  color: #525252;
  text-decoration: none;
  font-size: 0.9375rem;
  transition: color 0.2s;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #0a0a0a;
}

.nav-button {
  padding: 0.625rem 1.25rem;
  background: #0a0a0a;
  color: #ffffff;
  text-decoration: none;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
}

.nav-button:hover {
  background: #262626;
}

main {
  padding-top: 5rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-container {
    padding: 1rem 1.5rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link {
    display: none;
  }
}
</style>

