<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="footer-logo">Nyota Catalyst</div>
          <p class="footer-tagline">Empowering Silicon Savannah founders</p>
        </div>
        <div class="footer-links">
          <div class="footer-column">
            <h4>Program</h4>
            <a href="#program">Benefits</a>
            <a href="#process">How it works</a>
            <NuxtLink to="/founders">Founders</NuxtLink>
            <NuxtLink to="/register">Apply</NuxtLink>
          </div>
          <div class="footer-column">
            <h4>Company</h4>
            <a href="#">About</a>
            <a href="#">Contact</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 Nyota Catalyst. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Footer */
.footer {
  background: #fafafa;
  border-top: 1px solid #e5e5e5;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 2rem 2rem;
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 4rem;
  margin-bottom: 3rem;
}

.footer-logo {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.footer-tagline {
  color: #525252;
  font-size: 0.9375rem;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.footer-column h4 {
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.footer-column a {
  display: block;
  color: #525252;
  text-decoration: none;
  font-size: 0.9375rem;
  margin-bottom: 0.75rem;
  transition: color 0.2s;
}

.footer-column a:hover {
  color: #0a0a0a;
}

.footer-bottom {
  padding-top: 2rem;
  border-top: 1px solid #e5e5e5;
  text-align: center;
}

.footer-bottom p {
  color: #737373;
  font-size: 0.875rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
</style>

