<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="auth-header">
        <h1>Join Nyota Catalyst</h1>
        <p>Start your application to access resources and mentorship</p>
      </div>
      
      <form @submit.prevent="handleRegister" class="auth-form">
        <div class="form-field">
          <label for="username">Username</label>
          <input
            type="text"
            id="username"
            v-model="formData.username"
            required
            placeholder="Choose a username"
          />
        </div>
        
        <div class="form-field">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="formData.email"
            required
            placeholder="your.email@example.com"
          />
        </div>
        
        <div class="form-row">
          <div class="form-field">
            <label for="first_name">First Name</label>
            <input
              type="text"
              id="first_name"
              v-model="formData.first_name"
              placeholder="First name"
            />
          </div>
          
          <div class="form-field">
            <label for="last_name">Last Name</label>
            <input
              type="text"
              id="last_name"
              v-model="formData.last_name"
              placeholder="Last name"
            />
          </div>
        </div>
        
        <div class="form-field">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="formData.password"
            required
            placeholder="Create a strong password"
          />
        </div>
        
        <div class="form-field">
          <label for="password2">Confirm Password</label>
          <input
            type="password"
            id="password2"
            v-model="formData.password2"
            required
            placeholder="Confirm your password"
          />
        </div>
        
        <div class="form-field">
          <label for="profile_picture">Profile Picture (Optional)</label>
          <div class="file-upload-container">
            <input
              type="file"
              id="profile_picture"
              @change="handleFileChange"
              accept="image/*"
              ref="fileInput"
              style="display: none"
            />
            <button type="button" @click="$refs.fileInput.click()" class="btn-file-upload">
              {{ profilePictureFile ? profilePictureFile.name : 'Choose a file' }}
            </button>
            <button 
              v-if="profilePictureFile" 
              type="button" 
              @click="clearFile" 
              class="btn-clear-file"
            >
              ✕
            </button>
          </div>
          <p class="file-hint">JPG, PNG or GIF. Max 5MB.</p>
        </div>
        
        <div class="form-field">
          <div class="label-with-count">
            <label for="background">About You / Background</label>
            <span class="char-count" :class="{ 'char-limit-reached': formData.background.length >= 2000 }">
              {{ formData.background.length }}/2000
            </span>
          </div>
          <textarea
            id="background"
            v-model="formData.background"
            rows="4"
            maxlength="2000"
            placeholder="Tell us about your background, experience, and what drives you as an entrepreneur..."
          ></textarea>
        </div>
        
        <div class="form-field">
          <div class="label-with-count">
            <label for="project_description">Describe Your Project</label>
            <span class="char-count" :class="{ 'char-limit-reached': formData.project_description.length >= 3000 }">
              {{ formData.project_description.length }}/3000
            </span>
          </div>
          <textarea
            id="project_description"
            v-model="formData.project_description"
            rows="4"
            maxlength="3000"
            placeholder="Describe your project, the problem it solves, and your vision..."
          ></textarea>
        </div>
        
        <button type="submit" class="btn-submit" :disabled="loading">
          {{ loading ? 'Submitting application...' : 'Submit Application' }}
        </button>
        
        <div v-if="error" class="alert alert-error">{{ error }}</div>
        <div v-if="success" class="alert alert-success">{{ success }}</div>
      </form>
      
      <div class="auth-footer">
        <p>Already have an account? <NuxtLink to="/login">Sign in</NuxtLink></p>
      </div>
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
  password2: '',
  background: '',
  project_description: ''
})

const profilePictureFile = ref<File | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)
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

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    const file = target.files[0]
    
    // Validate file size (5MB max)
    if (file.size > 5 * 1024 * 1024) {
      error.value = 'File size must be less than 5MB'
      return
    }
    
    // Validate file type
    if (!file.type.startsWith('image/')) {
      error.value = 'Please upload an image file'
      return
    }
    
    profilePictureFile.value = file
    error.value = ''
  }
}

const clearFile = () => {
  profilePictureFile.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const handleRegister = async () => {
  error.value = ''
  success.value = ''
  loading.value = true

  const formDataToSend = new FormData()
  Object.entries(formData.value).forEach(([key, value]) => {
    formDataToSend.append(key, value)
  })
  
  if (profilePictureFile.value) {
    formDataToSend.append('profile_picture', profilePictureFile.value)
  }

  const result = await authStore.register(formDataToSend)

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
  max-width: 520px;
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

.file-upload-container {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.btn-file-upload {
  flex: 1;
  padding: 0.75rem 1rem;
  font-size: 0.9375rem;
  color: #525252;
  background: #fafafa;
  border: 1px solid #d4d4d4;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.btn-file-upload:hover {
  border-color: #0a0a0a;
  background: #ffffff;
}

.btn-clear-file {
  padding: 0.75rem;
  font-size: 1rem;
  color: #737373;
  background: transparent;
  border: 1px solid #d4d4d4;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-clear-file:hover {
  color: #991b1b;
  border-color: #fecaca;
  background: #fef2f2;
}

.file-hint {
  font-size: 0.75rem;
  color: #737373;
  margin: 0;
}

.form-field input,
.form-field textarea {
  width: 100%;
  padding: 0.875rem 1rem;
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
  min-height: 100px;
}

.form-field input::placeholder,
.form-field textarea::placeholder {
  color: #a3a3a3;
}

.form-field input:focus,
.form-field textarea:focus {
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

.alert-success {
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
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

  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>

