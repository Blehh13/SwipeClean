const swipeState = {
  currentFileIndex: 0,
  files: [
    { path: 'assets/files/photo1.jpg', type: 'image' },
    { path: 'assets/files/photo2.jpg', type: 'image' },
    { path: 'assets/files/video1.mp4', type: 'video' }
  ],
  isSwiping: false
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const cardStack = document.getElementById('card-stack');
  const deleteButton = document.getElementById('delete-button');
  const keepButton = document.getElementById('keep-button');
  const progressIndicator = document.getElementById('progress-indicator');
  const deleteLabel = document.querySelector('.swipe-label.delete');
  const keepLabel = document.querySelector('.swipe-label.keep');

  // Render cards
  function renderCards() {
    cardStack.innerHTML = '';
    const currentFile = swipeState.files[swipeState.currentFileIndex];
    if (currentFile) {
      const card = document.createElement('div');
      card.classList.add('card');
      const media = currentFile.type === 'image'
        ? `<img src="${currentFile.path}" alt="File">`
        : `<video src="${currentFile.path}" autoplay muted loop></video>`;
      card.innerHTML = media;
      cardStack.appendChild(card);
      progressIndicator.textContent = `${swipeState.currentFileIndex + 1} / ${swipeState.files.length} files`;
    } else {
      progressIndicator.textContent = 'No more files';
      cardStack.innerHTML = '<p class="no-files">All files processed!</p>';
    }
  }

  // Swipe action
  function swipe(direction) {
    if (swipeState.isSwiping || !swipeState.files[swipeState.currentFileIndex]) return;
    swipeState.isSwiping = true;
    const card = cardStack.querySelector('.card');
    if (card) {
      card.classList.add(direction === 'left' ? 'deleting' : 'keeping');
      const label = direction === 'left' ? deleteLabel : keepLabel;
      label.classList.add('visible');
      setTimeout(() => {
        // Mock file action
        if (document.hasStoragePermission === true)
        {
          if (direction === 'left') {
            console.log(`Deleted: ${swipeState.files[swipeState.currentFileIndex].path}`);
          } else {
            console.log(`Kept: ${swipeState.files[swipeState.currentFileIndex].path}`);
          }
        } else {
          console.log(`No Storage Permission`);
        }
        swipeState.currentFileIndex++;
        renderCards();
        card.classList.remove(direction === 'left' ? 'deleting' : 'keeping');
        label.classList.remove('visible');
        swipeState.isSwiping = false;
      }, 300); // Match CSS transition
    }
  }

  // Swipe gesture support
  let touchStartX = null;
  cardStack.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
  });

  cardStack.addEventListener('touchmove', (e) => {
    if (!touchStartX) return;
    const touchX = e.touches[0].clientX;
    const deltaX = touchX - touchStartX;
    const card = cardStack.querySelector('.card');
    if (card) {
      const translateX = Math.min(Math.max(deltaX, -200), 200);
      const rotate = translateX / 10;
      card.style.transform = `translateX(${translateX}px) rotate(${rotate}deg)`;
      if (translateX < -50) {
        deleteLabel.classList.add('visible');
        keepLabel.classList.remove('visible');
      } else if (translateX > 50) {
        keepLabel.classList.add('visible');
        deleteLabel.classList.remove('visible');
      } else {
        deleteLabel.classList.remove('visible');
        keepLabel.classList.remove('visible');
      }
    }
  });

  cardStack.addEventListener('touchend', (e) => {
    if (!touchStartX) return;
    const touchEndX = e.changedTouches[0].clientX;
    const deltaX = touchEndX - touchStartX;
    if (Math.abs(deltaX) > 100) {
      swipe(deltaX < 0 ? 'left' : 'right');
    } else {
      const card = cardStack.querySelector('.card');
      if (card) card.style.transform = '';
      deleteLabel.classList.remove('visible');
      keepLabel.classList.remove('visible');
    }
    touchStartX = null;
  });

  // Button actions
  deleteButton.addEventListener('click', () => swipe('left'));
  keepButton.addEventListener('click', () => swipe('right'));

  // Initial render
  renderCards();
  document.querySelector('.swipe-container').classList.add('active');
});