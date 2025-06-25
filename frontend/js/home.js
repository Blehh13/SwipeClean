const dashboardState = {
  storageInfo: { used: 0, total: 0 },
  isLoading: true,
  activeNav: 'home'
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const storageInfoElement = document.getElementById('storage-info');
  const startCleaningButton = document.getElementById('start-cleaning-button');
  const smartScanButton = document.getElementById('smart-scan-button');
  const browseFilesButton = document.getElementById('browse-files-button');
  const settingsButton = document.getElementById('settings-button');
  const navItems = document.querySelectorAll('.nav-item');

  // Mock storage info fetch
  setTimeout(() => {
    dashboardState.storageInfo = { used: 12.4, total: 64 };
    dashboardState.isLoading = false;
    storageInfoElement.textContent = `${dashboardState.storageInfo.used} GB of ${dashboardState.storageInfo.total} GB used`;
  }, 1000);

  // Button navigation
  startCleaningButton.addEventListener('click', () => {
    window.location.href = 'swipe.html';
  });

  smartScanButton.addEventListener('click', () => {
    window.location.href = 'suggestions.html';
  });

  browseFilesButton.addEventListener('click', () => {
    window.location.href = 'browser.html';
  });

  settingsButton.addEventListener('click', () => {
    window.location.href = 'settings.html';
  });

  // Bottom navigation
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      const navTarget = item.dataset.nav;
      dashboardState.activeNav = navTarget;
      navItems.forEach(nav => nav.classList.remove('active'));
      item.classList.add('active');

      switch (navTarget) {
        case 'home':
          window.location.href = 'index.html';
          break;
        case 'gallery':
          window.location.href = 'swipe.html';
          break;
        case 'suggestions':
          window.location.href = 'suggestions.html';
          break;
        case 'files':
          window.location.href = 'browser.html';
          break;
        case 'settings':
          window.location.href = 'settings.html';
          break;
      }
    });
  });
});