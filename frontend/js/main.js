function initApp() {
  const hasStoragePermission = localStorage.getItem('hasStoragePermission');
  if (!hasStoragePermission && window.location.pathname !== '/permissions.html') {
    window.location.href = '/permissions.html';
  }
}

window.addEventListener('load', initApp);