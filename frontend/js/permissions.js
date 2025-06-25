const permissionsState = {
  isPermissionGranted: false
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const permissionsContent = document.querySelector('.permissions-content');
  const allowButton = document.getElementById('allow-button');
  const denyButton = document.getElementById('deny-button');
  const denyMessage = document.getElementById('deny-message');

  // Apply fade-in animation
  permissionsContent.classList.add('active');

  // Allow button
  allowButton.addEventListener('click', () => {
    permissionsState.isPermissionGranted = true;
    // Mock permission grant
    localStorage.setItem('hasStoragePermission', true);
    window.location.href = 'index.html'; // Redirect to Home in index.html
  });

  // Deny button
  denyButton.addEventListener('click', () => {
    permissionsState.isPermissionGranted = false;
    denyMessage.classList.remove('hidden');
    denyMessage.classList.add('visible');
  });
});

function checkPermission() {
  const hasStoragePermission = localStorage.getItem('hasStoragePermission');
  if (hasStoragePermission) {
    window.location.href = '/index.html';
  }
}

window.addEventListener('load', checkPermission);