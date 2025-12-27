<template>
  <div class="dashboard-page">
    <div class="dashboard-container">
      <!-- Header Section -->
      <div class="dashboard-header">
    <h1>Dashboard</h1>
        <p v-if="authStore.user">Welcome back, {{ authStore.user.username }}</p>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="dashboard-loading">
        <div class="loading-spinner"></div>
        <p>Loading your dashboard...</p>
      </div>

      <!-- User Info Section -->
      <div v-else-if="authStore.user" class="dashboard-content">
        <!-- Profile Card -->
        <div class="card">
          <div class="card-header">
            <h2>Profile Information</h2>
            <button 
              v-if="!editingBasicInfo" 
              @click="startEditBasicInfo" 
              class="btn-edit"
            >
              Edit
            </button>
          </div>
          <div class="card-body">
            <div v-if="!editingBasicInfo" class="profile-view">
              <div v-if="authStore.user.profile" class="profile-picture-section">
                <img 
                  v-if="authStore.user.profile.profile_picture_url" 
                  :src="authStore.user.profile.profile_picture_url" 
                  alt="Profile"
                  class="profile-picture"
                />
                <div v-else class="profile-picture-placeholder">
                  {{ authStore.user.username.charAt(0).toUpperCase() }}
                </div>
              </div>
              
              <div class="info-grid">
                <div class="info-item">
                  <span class="info-label">Username</span>
                  <span class="info-value">{{ authStore.user.username }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Email</span>
                  <span class="info-value">{{ authStore.user.email }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">First Name</span>
                  <span class="info-value">{{ authStore.user.first_name || 'Not set' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Last Name</span>
                  <span class="info-value">{{ authStore.user.last_name || 'Not set' }}</span>
                </div>
              </div>
            </div>
            
            <form v-else @submit.prevent="saveBasicInfo" class="edit-form">
              <div class="form-field">
                <label>Profile Picture</label>
                <div class="profile-picture-edit">
                  <img 
                    v-if="profilePicturePreview || authStore.user.profile?.profile_picture_url" 
                    :src="profilePicturePreview || authStore.user.profile.profile_picture_url" 
                    alt="Profile"
                    class="profile-picture-preview"
                  />
                  <div v-else class="profile-picture-placeholder-large">
                    {{ authStore.user.username.charAt(0).toUpperCase() }}
                  </div>
                  <div class="picture-upload-controls">
                    <input
                      type="file"
                      @change="handlePictureChange"
                      accept="image/*"
                      ref="pictureInput"
                      style="display: none"
                    />
                    <button type="button" @click="$refs.pictureInput.click()" class="btn-upload-picture">
                      {{ profilePictureFile ? 'Change Picture' : 'Upload Picture' }}
                    </button>
                    <button 
                      v-if="profilePictureFile || authStore.user.profile?.profile_picture_url" 
                      type="button" 
                      @click="clearPicture" 
                      class="btn-remove-picture"
                    >
                      Remove
                    </button>
                  </div>
                  <p class="file-hint">JPG, PNG or GIF. Max 5MB.</p>
                </div>
              </div>
              
              <div class="form-row">
                <div class="form-field">
                  <label>First Name</label>
                  <input v-model="editForm.first_name" type="text" placeholder="First name" />
                </div>
                <div class="form-field">
                  <label>Last Name</label>
                  <input v-model="editForm.last_name" type="text" placeholder="Last name" />
                </div>
              </div>
              
              <div class="form-actions">
                <button type="submit" class="btn-save" :disabled="savingBasicInfo">
                  {{ savingBasicInfo ? 'Saving...' : 'Save Changes' }}
                </button>
                <button type="button" @click="cancelEditBasicInfo" class="btn-cancel">
                  Cancel
                </button>
              </div>
              
              <div v-if="basicInfoError" class="alert alert-error">{{ basicInfoError }}</div>
              <div v-if="basicInfoSuccess" class="alert alert-success">{{ basicInfoSuccess }}</div>
            </form>
          </div>
        </div>

        <!-- Program Status Card -->
        <div class="card">
          <div class="card-header">
            <h2>Program Status</h2>
          </div>
          <div class="card-body">
            <div v-if="authStore.user.profile" class="status-container">
              <div v-if="authStore.user.profile.status === 'pending'" class="status-badge status-pending">
                <span class="status-dot status-dot-pending"></span>
                <span>Applied - Pending Approval</span>
              </div>
              <div v-else-if="authStore.user.profile.status === 'enrolled'" class="status-badge status-enrolled">
                <span class="status-dot"></span>
                <span>Enrolled</span>
              </div>
              
              <p v-if="authStore.user.profile.status === 'pending'" class="status-description">
                Your application is under review. We'll notify you once a decision has been made. Thank you for your patience!
              </p>
              <p v-else-if="authStore.user.profile.status === 'enrolled'" class="status-description">
                You're enrolled in the Nyota Catalyst program since {{ formatDate(authStore.user.profile.enrollment_date) }}. 
                Make sure to maintain regular GitHub activity and respond to coaching sessions.
              </p>
            </div>
            <div v-else class="status-badge">
              <span>No Status Available</span>
            </div>
          </div>
        </div>

        <!-- Application Details Card -->
        <div v-if="authStore.user.profile" class="card">
          <div class="card-header">
            <h2>Your Application</h2>
            <button 
              v-if="!editingApplication" 
              @click="startEditApplication" 
              class="btn-edit"
            >
              Edit
            </button>
          </div>
          <div class="card-body">
            <div v-if="!editingApplication">
              <div class="application-section">
                <h3>Background</h3>
                <p v-if="authStore.user.profile.background" class="application-text">{{ authStore.user.profile.background }}</p>
                <p v-else class="application-empty">Not provided</p>
              </div>
              
              <div class="application-section">
                <h3>Project Description</h3>
                <p v-if="authStore.user.profile.project_description" class="application-text">{{ authStore.user.profile.project_description }}</p>
                <p v-else class="application-empty">Not provided</p>
              </div>
            </div>
            
            <form v-else @submit.prevent="saveApplication" class="edit-form">
              <div class="form-field">
                <div class="label-with-count">
                  <label for="edit-background">Background</label>
                  <span class="char-count" :class="{ 'char-limit-reached': editForm.background.length >= 2000 }">
                    {{ editForm.background.length }}/2000
                  </span>
                </div>
                <textarea
                  id="edit-background"
                  v-model="editForm.background"
                  rows="6"
                  maxlength="2000"
                  placeholder="Tell us about your background, experience, and what drives you as an entrepreneur..."
                ></textarea>
              </div>
              
              <div class="form-field">
                <div class="label-with-count">
                  <label for="edit-project">Project Description</label>
                  <span class="char-count" :class="{ 'char-limit-reached': editForm.project_description.length >= 3000 }">
                    {{ editForm.project_description.length }}/3000
                  </span>
                </div>
                <textarea
                  id="edit-project"
                  v-model="editForm.project_description"
                  rows="6"
                  maxlength="3000"
                  placeholder="Describe your project, the problem it solves, and your vision..."
                ></textarea>
              </div>
              
              <div class="form-actions">
                <button type="submit" class="btn-save" :disabled="savingApplication">
                  {{ savingApplication ? 'Saving...' : 'Save Changes' }}
                </button>
                <button type="button" @click="cancelEditApplication" class="btn-cancel">
                  Cancel
                </button>
              </div>
              
              <div v-if="applicationError" class="alert alert-error">{{ applicationError }}</div>
              <div v-if="applicationSuccess" class="alert alert-success">{{ applicationSuccess }}</div>
            </form>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="card">
          <div class="card-header">
            <h2>Quick Actions</h2>
          </div>
          <div class="card-body">
            <div class="actions-grid">
              <button class="action-button">
                <span class="action-icon">📊</span>
                <span>View Progress</span>
              </button>
              <button class="action-button">
                <span class="action-icon">💬</span>
                <span>Schedule Session</span>
              </button>
              <button class="action-button">
                <span class="action-icon">📝</span>
                <span>Submit Update</span>
              </button>
              <button class="action-button">
                <span class="action-icon">🔗</span>
                <span>Connect GitHub</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="alert alert-error">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const config = useRuntimeConfig()
const loading = ref(true)
const error = ref('')

// Edit states
const editingBasicInfo = ref(false)
const editingApplication = ref(false)
const savingBasicInfo = ref(false)
const savingApplication = ref(false)
const basicInfoError = ref('')
const basicInfoSuccess = ref('')
const applicationError = ref('')
const applicationSuccess = ref('')

// Edit form data
const editForm = ref({
  first_name: '',
  last_name: '',
  background: '',
  project_description: ''
})

const profilePictureFile = ref<File | null>(null)
const profilePicturePreview = ref<string | null>(null)
const pictureInput = ref<HTMLInputElement | null>(null)

definePageMeta({
  layout: 'default',
  middleware: (to, from) => {
    const authStore = useAuthStore()
    if (!authStore.isAuthenticated) {
      return navigateTo('/login')
    }
  }
})

const formatDate = (dateString: string | null) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}

const handlePictureChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    const file = target.files[0]
    
    // Validate file size (5MB max)
    if (file.size > 5 * 1024 * 1024) {
      basicInfoError.value = 'File size must be less than 5MB'
      return
    }
    
    // Validate file type
    if (!file.type.startsWith('image/')) {
      basicInfoError.value = 'Please upload an image file'
      return
    }
    
    profilePictureFile.value = file
    
    // Create preview
    const reader = new FileReader()
    reader.onload = (e) => {
      profilePicturePreview.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
    
    basicInfoError.value = ''
  }
}

const clearPicture = () => {
  profilePictureFile.value = null
  profilePicturePreview.value = null
  if (pictureInput.value) {
    pictureInput.value.value = ''
  }
}

const startEditBasicInfo = () => {
  editForm.value.first_name = authStore.user?.first_name || ''
  editForm.value.last_name = authStore.user?.last_name || ''
  editingBasicInfo.value = true
  basicInfoError.value = ''
  basicInfoSuccess.value = ''
}

const cancelEditBasicInfo = () => {
  editingBasicInfo.value = false
  basicInfoError.value = ''
  basicInfoSuccess.value = ''
}

const saveBasicInfo = async () => {
  savingBasicInfo.value = true
  basicInfoError.value = ''
  basicInfoSuccess.value = ''
  
  try {
    const formData = new FormData()
    formData.append('first_name', editForm.value.first_name)
    formData.append('last_name', editForm.value.last_name)
    
    if (profilePictureFile.value) {
      formData.append('profile_picture', profilePictureFile.value)
    }
    
    const response = await fetch(`${config.public.apiBase}/auth/user/`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (!response.ok) {
      throw new Error('Failed to update profile')
    }
    
    await authStore.fetchUser()
    profilePictureFile.value = null
    profilePicturePreview.value = null
    basicInfoSuccess.value = 'Profile updated successfully!'
    setTimeout(() => {
      editingBasicInfo.value = false
      basicInfoSuccess.value = ''
    }, 2000)
  } catch (e: any) {
    basicInfoError.value = e.message || 'Failed to update profile'
  } finally {
    savingBasicInfo.value = false
  }
}

const startEditApplication = () => {
  editForm.value.background = authStore.user?.profile?.background || ''
  editForm.value.project_description = authStore.user?.profile?.project_description || ''
  editingApplication.value = true
  applicationError.value = ''
  applicationSuccess.value = ''
}

const cancelEditApplication = () => {
  editingApplication.value = false
  applicationError.value = ''
  applicationSuccess.value = ''
}

const saveApplication = async () => {
  savingApplication.value = true
  applicationError.value = ''
  applicationSuccess.value = ''
  
  try {
    const response = await fetch(`${config.public.apiBase}/auth/user/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        background: editForm.value.background,
        project_description: editForm.value.project_description
      })
    })
    
    if (!response.ok) {
      throw new Error('Failed to update application')
    }
    
    await authStore.fetchUser()
    applicationSuccess.value = 'Application updated successfully!'
    setTimeout(() => {
      editingApplication.value = false
      applicationSuccess.value = ''
    }, 2000)
  } catch (e: any) {
    applicationError.value = e.message || 'Failed to update application'
  } finally {
    savingApplication.value = false
  }
}

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
* {
  box-sizing: border-box;
}

.dashboard-page {
  min-height: calc(100vh - 80px);
  background: #fafafa;
  padding: 2rem 1rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
}

.dashboard-container {
  max-width: 1000px;
  margin: 0 auto;
}

/* Header */
.dashboard-header {
  margin-bottom: 3rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #0a0a0a;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.dashboard-header p {
  font-size: 1.125rem;
  color: #525252;
}

/* Loading State */
.dashboard-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  gap: 1rem;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e5e5e5;
  border-top-color: #0a0a0a;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.dashboard-loading p {
  font-size: 0.9375rem;
  color: #525252;
}

/* Content */
.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* Card Styles */
.card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
  overflow: hidden;
  transition: all 0.2s;
}

.card:hover {
  border-color: #d4d4d4;
}

.card-header {
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #e5e5e5;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #0a0a0a;
  margin: 0;
}

.btn-edit {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #0a0a0a;
  background: transparent;
  border: 1px solid #d4d4d4;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-edit:hover {
  background: #fafafa;
  border-color: #0a0a0a;
}

.card-body {
  padding: 2rem;
}

/* Profile View */
.profile-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.profile-picture-section {
  display: flex;
  justify-content: center;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e5e5;
}

.profile-picture {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #e5e5e5;
}

.profile-picture-placeholder {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: #0a0a0a;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 600;
  border: 3px solid #e5e5e5;
}

.profile-picture-placeholder-large {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: #0a0a0a;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  font-weight: 600;
  border: 3px solid #e5e5e5;
}

.profile-picture-edit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.profile-picture-preview {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #e5e5e5;
}

.picture-upload-controls {
  display: flex;
  gap: 0.75rem;
}

.btn-upload-picture {
  padding: 0.625rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #ffffff;
  background: #0a0a0a;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-upload-picture:hover {
  background: #262626;
}

.btn-remove-picture {
  padding: 0.625rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #991b1b;
  background: transparent;
  border: 1px solid #fecaca;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-remove-picture:hover {
  background: #fef2f2;
  border-color: #991b1b;
}

/* Info Grid */
.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #737373;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.info-value {
  font-size: 1rem;
  font-weight: 500;
  color: #0a0a0a;
}

/* Status Badge */
.status-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  width: fit-content;
}

.status-badge.status-enrolled {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  color: #166534;
}

.status-badge.status-pending {
  background: #fef3c7;
  border: 1px solid #fde68a;
  color: #92400e;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

.status-dot-pending {
  background: #f59e0b;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.status-description {
  font-size: 0.9375rem;
  color: #525252;
  line-height: 1.6;
  margin: 0;
}

/* Application Details */
.application-section {
  margin-bottom: 2rem;
}

.application-section:last-child {
  margin-bottom: 0;
}

.application-section h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #0a0a0a;
  margin-bottom: 0.75rem;
}

.application-text {
  font-size: 0.9375rem;
  color: #525252;
  line-height: 1.7;
  white-space: pre-wrap;
  margin: 0;
}

.application-empty {
  font-size: 0.9375rem;
  color: #a3a3a3;
  font-style: italic;
  margin: 0;
}

/* Edit Forms */
.edit-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
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

.form-field input,
.form-field textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 0.9375rem;
  color: #0a0a0a;
  background: #ffffff;
  border: 1px solid #d4d4d4;
  border-radius: 0.5rem;
  transition: all 0.2s;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
}

.form-field textarea {
  resize: vertical;
  min-height: 120px;
}

.form-field input:focus,
.form-field textarea:focus {
  outline: none;
  border-color: #0a0a0a;
}

.label-with-count {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.char-count {
  font-size: 0.75rem;
  color: #737373;
  font-weight: 400;
}

.char-count.char-limit-reached {
  color: #f59e0b;
  font-weight: 500;
}

.form-actions {
  display: flex;
  gap: 0.75rem;
  margin-top: 0.5rem;
}

.btn-save {
  padding: 0.75rem 1.5rem;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #ffffff;
  background: #0a0a0a;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-save:hover:not(:disabled) {
  background: #262626;
}

.btn-save:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  font-size: 0.9375rem;
  font-weight: 500;
  color: #0a0a0a;
  background: transparent;
  border: 1px solid #d4d4d4;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cancel:hover {
  background: #fafafa;
  border-color: #0a0a0a;
}

.alert-success {
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
}

/* Actions Grid */
.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.action-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  padding: 1.5rem 1rem;
  background: #fafafa;
  border: 1px solid #e5e5e5;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #0a0a0a;
  cursor: pointer;
  transition: all 0.2s;
}

.action-button:hover {
  background: #ffffff;
  border-color: #0a0a0a;
  transform: translateY(-2px);
}

.action-icon {
  font-size: 1.5rem;
}

/* Alert */
.alert {
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  font-size: 0.9375rem;
  line-height: 1.5;
}

.alert-error {
  background: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

/* Responsive */
@media (max-width: 768px) {
  .dashboard-header h1 {
    font-size: 2rem;
  }

  .dashboard-header p {
    font-size: 1rem;
  }

  .card-header,
  .card-body {
    padding: 1.25rem 1.5rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .actions-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .btn-save,
  .btn-cancel {
    width: 100%;
  }
}
</style>

