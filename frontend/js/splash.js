const splashState = {
  isAnimating: true,
  redirectTarget: ''
};

// Variables
const isFirstTimeUser = !localStorage.getItem('hasOnboarded');
const animationDuration = 2000; // 2 seconds

// Particle effect
function initParticles() {
  const canvas = document.getElementById('particle-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const particles = [];
  const particleCount = 50;

  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 3 + 1;
      this.speedX = Math.random() * 0.5 - 0.25;
      this.speedY = Math.random() * 0.5 - 0.25;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
      if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
      ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(particle => {
      particle.update();
      particle.draw();
    });
    requestAnimationFrame(animate);
  }
  animate();
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const splashScreen = document.getElementById('splash-screen');
  const splashContent = document.getElementById('splash-content');
  const logo = document.querySelector('.logo');

  // Start particle effect
  initParticles();

  // Apply fade-in animation
  splashContent.classList.add('animate-fade-in');

  // Apply logo pulse animation
  setTimeout(() => {
    logo.classList.add('animate-logo-pulse');
  }, 700);

  // Transition to next screen
  setTimeout(() => {
    splashState.isAnimating = false;
    splashState.redirectTarget = isFirstTimeUser ? 'onboarding' : 'home';
    splashContent.classList.add('animate-fade-out');

    // Wait for fade-out to complete
    setTimeout(() => {
      splashScreen.classList.add('hidden');
      document.getElementById(`${splashState.redirectTarget}-screen`).classList.remove('hidden');
      document.getElementById(`${splashState.redirectTarget}-screen`).classList.add('active');
    }, 500);
  }, animationDuration);
});