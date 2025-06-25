const browserState = {
  files: [
    { path: 'assets/files/photo1.jpg', type: 'image', name: 'photo1.jpg', size: 6.2 },
    { path: 'assets/files/photo2.jpg', type: 'image', name: 'photo2.jpg', size: 3.5 },
    { path: 'assets/files/video1.mp4', type: 'video', name: 'video1.mp4', size: 15.8 },
    { path: 'assets/files/screenshot1.png', type: 'image', name: 'screenshot1.png', size: 0.8 }
  ],
  selectedFiles: [],
  viewMode: 'list'
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const fileList = document.getElementById('file-list');
  const listViewButton = document.getElementById('list-view-button');
  const gridViewButton = document.getElementById('grid-view-button');
  const deleteSelectedButton = document.getElementById('delete-selected-button');
  const swipeSelectedButton = document.getElementById('swipe-selected-button');

  // Render files
  function renderFiles() {
    fileList.classList.remove('list-view', 'grid-view');
    fileList.classList.add(`${browserState.viewMode}-view`);
    fileList.innerHTML = '';

    browserState.files.forEach((file, index) => {
      const item = document.createElement('div');
      item.classList.add('file-item', `${browserState.viewMode}-view`);
      item.innerHTML = `
        ${file.type === 'image' ? `<img src="${file.path}" alt="${file.name}">` : `<video src="${file.path}" muted></video>`}
        <div class="file-info">
          <p>${file.name}</p>
          <p class="file-size">${file.size} MB</p>
        </div>
        <input type="checkbox" class="file-checkbox" data-index="${index}">
      `;
      fileList.appendChild(item);
    });

    // Bind checkbox events
    document.querySelectorAll('.file-checkbox').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        const index = parseInt(e.target.dataset.index);
        if (e.target.checked) {
          browserState.selectedFiles.push(browserState.files[index]);
        } else {
          browserState.selectedFiles = browserState.selectedFiles.filter(f => f !== browserState.files[index]);
        }
      });
    });
  }

  // View toggle
  listViewButton.addEventListener('click', () => {
    browserState.viewMode = 'list';
    listViewButton.classList.add('active');
    gridViewButton.classList.remove('active');
    renderFiles();
  });

  gridViewButton.addEventListener('click', () => {
    browserState.viewMode = 'grid';
    gridViewButton.classList.add('active');
    listViewButton.classList.remove('active');
    renderFiles();
  });

  // Delete Selected
  deleteSelectedButton.addEventListener('click', () => {
    if (browserState.selectedFiles.length > 0 && localStorage.getItem('hasStoragePermission') === 'true') {
      console.log(`Deleted: ${browserState.selectedFiles.map(f => f.path).join(', ')}`);
      browserState.files = browserState.files.filter(f => !browserState.selectedFiles.includes(f));
      browserState.selectedFiles = [];
      renderFiles();
    } else if (browserState.selectedFiles.length === 0) {
      console.log('No files selected');
    } else {
      console.log('No storage permission');
    }
  });

  // Swipe Selected
  swipeSelectedButton.addEventListener('click', () => {
    if (browserState.selectedFiles.length > 0) {
      // In a real app, pass selected files to swipe.html
      console.log(`Swipe: ${browserState.selectedFiles.map(f => f.path).join(', ')}`);
      window.location.href = 'swipe.html';
    } else {
      console.log('No files selected');
    }
  });

  // Initial render
  renderFiles();
  document.querySelector('.browser-container').classList.add('active');
});