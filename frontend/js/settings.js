const settingsState = {
  notifications: true,
  theme: 'light'
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const manageStorageButton = document.getElementById('manage-storage-button');
  const notificationsToggle = document.getElementById('notifications-toggle');
  const themeSelect = document.getElementById('theme-select');

  // Load settings
  notificationsToggle.checked = settingsState.notifications;
  themeSelect.value = settingsState.theme;

  // Manage Storage Permission
  manageStorageButton.addEventListener('click', () => {
    // Mock permission management
    if (confirm('Redirect to permissions page to manage storage access?')) {
      window.location.href = 'permissions.html';
    }
  });

  // Notifications Toggle
  notificationsToggle.addEventListener('change', (e) => {
    settingsState.notifications = e.target.checked;
    console.log(`Notifications: ${settingsState.notifications}`);
  });

  // Theme Select
  themeSelect.addEventListener('change', (e) => {
    settingsState.theme = e.target.value;
    console.log(`Theme: ${settingsState.theme}`);
    // In a real app, apply theme (e.g., toggle CSS classes)
  });

  // Initial render
  document.querySelector('.settings-container').classList.add('active');
});