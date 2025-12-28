<template>
  <div class="founders-page">
    <!-- Filter Tabs -->
    <div class="filters-section">
      <div class="filters-container">
        <div class="tabs">
          <button
            v-for="tab in tabs"
            :key="tab.value"
            @click="activeTab = tab.value"
            :class="['tab', { 'tab-active': activeTab === tab.value }]"
          >
            {{ tab.label }}
          </button>
        </div>
      </div>
    </div>

    <!-- Founders Grid -->
    <section class="founders-section">
      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading founders...</p>
      </div>

      <div v-else-if="error" class="error-state">
        <div class="error-card">
          <p class="error-message">{{ error }}</p>
          <button @click="fetchFounders" class="btn-retry">
            Try Again
          </button>
        </div>
      </div>

      <div v-else-if="founders.length === 0" class="empty-state">
        <div class="empty-icon">🔍</div>
        <p class="empty-message">No founders found in this category</p>
      </div>

      <div v-else class="founders-grid">
        <div
          v-for="founder in founders"
          :key="founder.username"
          class="founder-card"
        >
          <!-- Profile Picture -->
          <div class="founder-image">
            <img
              v-if="founder.profile_picture_url"
              :src="founder.profile_picture_url"
              :alt="`${founder.first_name} ${founder.last_name}`"
            />
            <div v-else class="founder-initials">
              <span>{{ getInitials(founder.first_name, founder.last_name) }}</span>
            </div>
            
            <!-- Status Badge -->
            <div class="status-badge-container">
              <span :class="['status-badge', `status-${founder.status}`]">
                {{ founder.status_display }}
              </span>
            </div>
          </div>

          <!-- Founder Info -->
          <div class="founder-info">
            <h3 class="founder-name">
              {{ founder.first_name }} {{ founder.last_name }}
            </h3>
            <p class="founder-username">@{{ founder.username }}</p>

            <!-- Background -->
            <div v-if="founder.background" class="info-section">
              <h4>Background</h4>
              <p class="info-text">{{ founder.background }}</p>
            </div>

            <!-- Project Description -->
            <div v-if="founder.project_description" class="info-section">
              <h4>Project</h4>
              <p class="info-text">{{ founder.project_description }}</p>
            </div>

            <!-- Enrollment Date -->
            <div v-if="founder.enrollment_date" class="enrollment-date">
              Enrolled: {{ formatDate(founder.enrollment_date) }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from 'vue'

interface Founder {
  username: string
  first_name: string
  last_name: string
  profile_picture_url: string | null
  background: string
  project_description: string
  status: string
  status_display: string
  enrollment_date: string | null
}

const tabs = [
  { label: 'All Founders', value: 'all' },
  { label: 'Seeking Support', value: 'seeking_support' },
  { label: 'Enrolled', value: 'enrolled' }
]

const activeTab = ref('all')
const founders = ref<Founder[]>([])
const loading = ref(false)
const error = ref<string | null>(null)

const fetchFounders = async () => {
  loading.value = true
  error.value = null
  
  try {
    const config = useRuntimeConfig()
    
    // Fetch based on active tab - always send status parameter
    const endpoint = `${config.public.apiBase}/auth/founders/?status=${activeTab.value}`
    
    const response = await fetch(endpoint, {
      method: 'GET',
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    founders.value = await response.json()
  } catch (err: any) {
    console.error('Error fetching founders:', err)
    error.value = err.message || 'Failed to load founders. Please try again.'
  } finally {
    loading.value = false
  }
}

const getInitials = (firstName: string, lastName: string): string => {
  const first = firstName?.charAt(0) || ''
  const last = lastName?.charAt(0) || ''
  return (first + last).toUpperCase() || '?'
}

const formatDate = (dateString: string | null): string => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

// Watch for tab changes and refetch data
watch(activeTab, () => {
  fetchFounders()
})

// Fetch founders on mount
onMounted(() => {
  fetchFounders()
})
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.founders-page {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
  color: #0a0a0a;
  background: #ffffff;
  min-height: 100vh;
}

/* Hero Section */
.hero {
  padding: 8rem 2rem 4rem;
  background: #0a0a0a;
  color: #ffffff;
  text-align: center;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.hero-description {
  font-size: 1.25rem;
  color: #a3a3a3;
  line-height: 1.6;
  max-width: 700px;
  margin: 0 auto;
}

/* Filters Section */
.filters-section {
  background: #ffffff;
  border-bottom: 1px solid #e5e5e5;
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.95);
  padding-top: 1rem;
}

.filters-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem 2rem;
}

.tabs {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.tab {
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: #525252;
  border: 1px solid #e5e5e5;
  border-radius: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.tab:hover {
  border-color: #0a0a0a;
  color: #0a0a0a;
}

.tab-active {
  background: #0a0a0a;
  color: #ffffff;
  border-color: #0a0a0a;
}

/* Founders Section */
.founders-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
  min-height: 400px;
}

/* Loading State */
.loading-state {
  text-align: center;
  padding: 6rem 2rem;
}

.spinner {
  width: 48px;
  height: 48px;
  border: 3px solid #e5e5e5;
  border-top-color: #0a0a0a;
  border-radius: 50%;
  margin: 0 auto 1.5rem;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-state p {
  color: #525252;
  font-size: 1rem;
}

/* Error State */
.error-state {
  padding: 6rem 2rem;
  text-align: center;
}

.error-card {
  max-width: 500px;
  margin: 0 auto;
  padding: 2.5rem;
  background: #fafafa;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
}

.error-message {
  color: #dc2626;
  margin-bottom: 1.5rem;
  font-size: 1rem;
}

.btn-retry {
  padding: 0.75rem 1.5rem;
  background: #dc2626;
  color: #ffffff;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.btn-retry:hover {
  background: #b91c1c;
  transform: translateY(-1px);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 6rem 2rem;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.empty-message {
  color: #525252;
  font-size: 1.125rem;
}

/* Founders Grid */
.founders-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
}

/* Founder Card */
.founder-card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
  overflow: hidden;
  transition: all 0.3s;
}

.founder-card:hover {
  border-color: #0a0a0a;
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

/* Founder Image */
.founder-image {
  position: relative;
  height: 240px;
  background: #fafafa;
  overflow: hidden;
}

.founder-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.founder-initials {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0a0a0a 0%, #262626 100%);
}

.founder-initials span {
  font-size: 4rem;
  font-weight: 700;
  color: #ffffff;
}

/* Status Badge */
.status-badge-container {
  position: absolute;
  top: 1rem;
  right: 1rem;
}

.status-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-enrolled {
  background: #22c55e;
  color: #ffffff;
}

.status-seeking_support {
  background: #eab308;
  color: #ffffff;
}

.status-pending {
  background: #94a3b8;
  color: #ffffff;
}

/* Founder Info */
.founder-info {
  padding: 2rem;
}

.founder-name {
  font-size: 1.375rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: #0a0a0a;
}

.founder-username {
  font-size: 0.875rem;
  color: #737373;
  margin-bottom: 1.5rem;
}

/* Info Section */
.info-section {
  margin-bottom: 1.5rem;
}

.info-section h4 {
  font-size: 0.875rem;
  font-weight: 600;
  color: #0a0a0a;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.info-text {
  font-size: 0.9375rem;
  color: #525252;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Enrollment Date */
.enrollment-date {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e5e5e5;
  font-size: 0.8125rem;
  color: #737373;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero {
    padding: 6rem 1.5rem 3rem;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-description {
    font-size: 1.125rem;
  }

  .filters-container {
    padding: 1rem 1.5rem;
  }

  .founders-section {
    padding: 3rem 1.5rem;
  }

  .founders-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .founder-image {
    height: 200px;
  }

  .founder-initials span {
    font-size: 3rem;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .founders-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

