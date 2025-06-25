const onboardingState = {
  currentSlide: 0,
  hasCompleted: false,
  isTransitioning: false,
  direction: 'right'
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const carouselInner = document.querySelector('.carousel-inner');
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.dot');
  const skipLink = document.getElementById('skip-link');
  const getStartedButton = document.getElementById('get-started-button');

  // Update carousel position
  function updateCarousel() {
    carouselInner.style.transform = `translateX(-${onboardingState.currentSlide * 33.33}%)`;
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === onboardingState.currentSlide);
    });
    slides.forEach((slide, index) => {
      slide.classList.toggle('active', index === onboardingState.currentSlide);
    });
  }

  // Navigate to specific slide
  function goToSlide(index) {
    if (index >= 0 && index < slides.length && !onboardingState.isTransitioning) {
      onboardingState.isTransitioning = true;
      onboardingState.direction = index > onboardingState.currentSlide ? 'right' : 'left';
      onboardingState.currentSlide = index;
      updateCarousel();
      setTimeout(() => {
        onboardingState.isTransitioning = false;
      }, 500); // Match CSS transition duration
    }
  }

  // Swipe gesture support
  let touchStartX = null;
  carouselInner.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
  });

  carouselInner.addEventListener('touchend', (e) => {
    if (touchStartX === null) return;
    const touchEndX = e.changedTouches[0].clientX;
    const deltaX = touchEndX - touchStartX;
    if (Math.abs(deltaX) > 50) {
      if (deltaX > 0 && onboardingState.currentSlide > 0) {
        goToSlide(onboardingState.currentSlide - 1);
      } else if (deltaX < 0 && onboardingState.currentSlide < slides.length - 1) {
        goToSlide(onboardingState.currentSlide + 1);
      }
    }
    touchStartX = null;
  });

  // Skip button
  skipLink.addEventListener('click', (e) => {
    e.preventDefault();
    localStorage.setItem('hasOnboarded', true);
    window.location.href = 'permissions.html';
  });

  // Get Started button
  getStartedButton.addEventListener('click', () => {
    localStorage.setItem('hasOnboarded', true);
    window.location.href = 'permissions.html';
  });

  // Initial setup
  updateCarousel();
});