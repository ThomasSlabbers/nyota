<template>
  <div class="landing">
    <!-- Navigation -->
    <nav class="nav">
      <div class="nav-container">
        <div class="nav-logo">Nyota Catalyst</div>
        <div class="nav-links">
          <NuxtLink to="/login" class="nav-link">Sign in</NuxtLink>
          <NuxtLink to="/register" class="nav-button">Apply now</NuxtLink>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-container">
        <h1 class="hero-title">
          Fueling the next wave of<br>
          <span class="hero-highlight">Silicon Savannah</span> founders
        </h1>
        <p class="hero-description">
          Technical and financial infrastructure for ambitious entrepreneurs building the future from Nairobi, Kenya.
        </p>
        <div class="hero-cta">
          <NuxtLink to="/register" class="btn-primary">Start your application</NuxtLink>
          <a href="#program" class="btn-secondary">Learn more</a>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats">
      <div class="stats-container">
        <div class="stat">
          <div class="stat-value">$90</div>
          <div class="stat-label">Initial monthly support value</div>
        </div>
        <div class="stat">
          <div class="stat-value">1:1</div>
          <div class="stat-label">Monthly mentorship</div>
        </div>
        <div class="stat">
          <div class="stat-value">$</div>
          <div class="stat-label">Investment round opportunity</div>
        </div>
      </div>
    </section>

    <!-- Program Section -->
    <section id="program" class="program">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">What you'll receive</h2>
          <p class="section-subtitle">
            Everything you need to build, deploy, and scale your startup
          </p>
        </div>

        <div class="benefits">
          <div class="benefit">
            <div class="benefit-header">
              <h3>Cursor Pro</h3>
              <span class="benefit-value">~$30/mo</span>
            </div>
            <p class="benefit-description">
              Advanced AI-powered development environment. Ship faster with intelligent code completion and pair programming.
            </p>
          </div>

          <div class="benefit">
            <div class="benefit-header">
              <h3>Hetzner Cloud</h3>
              <span class="benefit-value">~$30/mo</span>
            </div>
            <p class="benefit-description">
              Production-grade hosting infrastructure. Deploy and scale your applications with reliability.
            </p>
          </div>

          <div class="benefit">
            <div class="benefit-header">
              <h3>Starlink Residential</h3>
              <span class="benefit-value">~$30/mo</span>
            </div>
            <p class="benefit-description">
              Optional: High-speed internet connectivity to ensure uninterrupted development and deployment workflows.
            </p>
          </div>

          <div class="benefit">
            <div class="benefit-header">
              <h3>Expert mentorship</h3>
              <span class="benefit-value">Monthly</span>
            </div>
            <p class="benefit-description">
              One-on-one coaching sessions with experienced founders and operators to help you navigate challenges and scale.
            </p>
          </div>

          <div class="benefit">
            <div class="benefit-header">
              <h3>Investment opportunity</h3>
              <span class="benefit-value">Optional</span>
            </div>
            <p class="benefit-description">
              Pitch your prototype to receive investment from Nyota and our network of investors to accelerate your growth.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Process Section -->
    <section class="process">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">How it works</h2>
          <p class="section-subtitle">
            A straightforward path from application to launch
          </p>
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-marker">01</div>
            <div class="timeline-content">
              <h3>Submit your application</h3>
              <p>Tell us about your project, your vision, and what you're building. We review applications on a rolling basis.</p>
      </div>
    </div>
    
          <div class="timeline-item">
            <div class="timeline-marker">02</div>
            <div class="timeline-content">
              <h3>Present your pitch</h3>
              <p>Selected founders receive an invitation to present their vision and demonstrate their technical capabilities.</p>
            </div>
    </div>
    
          <div class="timeline-item">
            <div class="timeline-marker">03</div>
            <div class="timeline-content">
              <h3>Join the program</h3>
              <p>Get immediate access to all resources and begin building with support from our team and community.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Program Details Section -->
    <section class="details">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">The partnership</h2>
          <p class="section-subtitle">
            Clear expectations and mutual commitments for long-term success
          </p>
        </div>

        <div class="details-grid">
          <div class="detail-card">
            <h3>Shared Success (7% Stake)</h3>
            <p>
              When you formalize your venture as a Private Limited Company, Nyota receives a 7% equity stake. 
              100% of returns from this stake are reinvested to support the next generation of entrepreneurs.
            </p>
          </div>

          <div class="detail-card">
            <h3>Your Commitments</h3>
            <p>
              Maintain an active GitHub repository with visible progress. Respond to coaching coordination within 48 hours. 
              Be transparent about blockers, pivots, or challenges—we're here to help you succeed.
            </p>
          </div>

          <div class="detail-card">
            <h3>Scaling Opportunities</h3>
            <p>
              As you gain traction, pitch for additional capital and support. Access industry experts across Africa, Europe, and the USA. 
              Receive warm introductions to clients, beta testers, and strategic partners.
            </p>
          </div>

          <div class="detail-card">
            <h3>Terms & Ownership</h3>
            <p>
              You retain 100% ownership of all code, IP, and business rights. Resources are for your project only. 
              When successful, contribute 2 hours/month mentoring students at local grassroots coding schools.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="cta-container">
        <h2 class="cta-title">Ready to build?</h2>
        <p class="cta-description">
          Join Nyota Catalyst and accelerate your journey from idea to impact
        </p>
        <NuxtLink to="/register" class="btn-primary-large">Start your application</NuxtLink>
      </div>
    </section>

    <!-- Footer -->
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
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false
})
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.landing {
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

.nav-link:hover {
  color: #0a0a0a;
}

.nav-button {
  padding: 0.625rem 1.25rem;
  background: #0a0a0a;
  color: #ffffff;
  text-decoration: none;
  border-radius: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.nav-button:hover {
  background: #262626;
}

/* Hero Section */
.hero {
  padding: 10rem 2rem 6rem;
  text-align: center;
}

.hero-container {
  max-width: 900px;
  margin: 0 auto;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  letter-spacing: -0.03em;
}

.hero-highlight {
  color: #0066ff;
}

.hero-description {
  font-size: 1.25rem;
  color: #525252;
  line-height: 1.6;
  margin-bottom: 3rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-primary {
  padding: 1rem 2rem;
  background: #0a0a0a;
  color: #ffffff;
  text-decoration: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.2s;
  display: inline-block;
}

.btn-primary:hover {
  background: #262626;
  transform: translateY(-1px);
}

.btn-secondary {
  padding: 1rem 2rem;
  background: transparent;
  color: #0a0a0a;
  text-decoration: none;
  border: 1px solid #e5e5e5;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.2s;
  display: inline-block;
}

.btn-secondary:hover {
  border-color: #0a0a0a;
}

/* Stats Section */
.stats {
  padding: 4rem 2rem;
  background: #fafafa;
  border-top: 1px solid #e5e5e5;
  border-bottom: 1px solid #e5e5e5;
}

.stats-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 3rem;
  text-align: center;
}

.stat-value {
  font-size: 3rem;
  font-weight: 700;
  color: #0a0a0a;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9375rem;
  color: #525252;
}

/* Section Styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 6rem 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #525252;
  max-width: 600px;
  margin: 0 auto;
}

/* Benefits */
.benefits {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.benefit {
  padding: 2rem;
  background: #fafafa;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
  transition: all 0.2s;
}

.benefit:hover {
  border-color: #0a0a0a;
  transform: translateY(-2px);
}

.benefit-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.benefit h3 {
  font-size: 1.25rem;
  font-weight: 600;
}

.benefit-value {
  font-size: 0.875rem;
  color: #525252;
  font-weight: 500;
}

.benefit-description {
  font-size: 0.9375rem;
  color: #525252;
  line-height: 1.6;
}

/* Process/Timeline */
.process {
  background: #fafafa;
}

.timeline {
  max-width: 800px;
  margin: 0 auto;
}

.timeline-item {
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-marker {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #0a0a0a;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
  flex-shrink: 0;
}

.timeline-content h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.timeline-content p {
  font-size: 1rem;
  color: #525252;
  line-height: 1.6;
}

/* Details Section */
.details {
  background: #ffffff;
  border-top: 1px solid #e5e5e5;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.detail-card {
  padding: 2.5rem;
  background: #fafafa;
  border: 1px solid #e5e5e5;
  border-radius: 0.75rem;
  transition: all 0.2s;
}

.detail-card:hover {
  border-color: #0a0a0a;
  transform: translateY(-2px);
}

.detail-card.full-width {
  grid-column: 1 / -1;
  background: #0a0a0a;
  color: #ffffff;
  border-color: #0a0a0a;
}

.detail-card.full-width h3 {
  color: #ffffff;
}

.detail-card.full-width p {
  color: #d4d4d4;
}

.detail-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #0a0a0a;
}

.detail-card p {
  font-size: 0.9375rem;
  color: #525252;
  line-height: 1.7;
}

/* CTA Section */
.cta-section {
  padding: 6rem 2rem;
  text-align: center;
  background: #0a0a0a;
  color: #ffffff;
}

.cta-container {
  max-width: 800px;
  margin: 0 auto;
}

.cta-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.cta-description {
  font-size: 1.25rem;
  color: #a3a3a3;
  margin-bottom: 2.5rem;
}

.btn-primary-large {
  padding: 1.25rem 2.5rem;
  background: #ffffff;
  color: #0a0a0a;
  text-decoration: none;
  border-radius: 0.5rem;
  font-size: 1.125rem;
  font-weight: 600;
  transition: all 0.2s;
  display: inline-block;
}

.btn-primary-large:hover {
  background: #f5f5f5;
  transform: translateY(-2px);
}

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
  .hero {
    padding: 8rem 1.5rem 4rem;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-description {
    font-size: 1.125rem;
  }

  .section-container {
    padding: 4rem 1.5rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .timeline-item {
    grid-template-columns: 60px 1fr;
    gap: 1.5rem;
  }

  .timeline-marker {
    width: 60px;
    height: 60px;
    font-size: 1.25rem;
  }

  .cta-title {
    font-size: 2rem;
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .nav-links {
    gap: 1rem;
  }

  .nav-link {
    display: none;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }

  .detail-card.full-width {
    grid-column: 1;
  }
}
</style>

