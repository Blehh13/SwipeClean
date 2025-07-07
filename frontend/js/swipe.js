const swipeState = {
  currentFileIndex: 0,
  files: [
    { 
      path: 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=400', 
      type: 'image',
      name: 'Beautiful Landscape',
      size: '2.3 MB'
    },
    { 
      path: 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=400', 
      type: 'image',
      name: 'City View',
      size: '1.8 MB'
    },
    { 
      path: 'https://images.pexels.com/photos/326055/pexels-photo-326055.jpeg?auto=compress&cs=tinysrgb&w=400', 
      type: 'image',
      name: 'Nature Photo',
      size: '3.1 MB'
    }
  ],
  isSwiping: false
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const cardStack = document.getElementById('card-stack');
  const deleteButton = document.getElementById('delete-button');
  const keepButton = document.getElementById('keep-button');
  const skipButton = document.getElementById('skip-button');
  const previewButton = document.getElementById('preview-button');
  const progressIndicator = document.getElementById('progress-indicator');
  const deleteLabel = document.querySelector('.swipe-label.delete');
  const keepLabel = document.querySelector('.swipe-label.keep');

  // Render current card
  function renderCard() {
    cardStack.innerHTML = '';
    const currentFile = swipeState.files[swipeState.currentFileIndex];
    
    if (currentFile) {
      const card = document.createElement('div');
      card.classList.add('card');
      
      const media = currentFile.type === 'image'
        ? `<img src="${currentFile.path}" alt="File" loading="lazy">`
        : `<video src="${currentFile.path}" autoplay muted loop></video>`;
      
      card.innerHTML = `
        ${media}
        <div class="file-info">
          <p><strong>${currentFile.name}</strong></p>
          <p>Size: ${currentFile.size}</p>
          <p>Type: ${currentFile.type}</p>
        </div>
      `;
      
      cardStack.appendChild(card);
      progressIndicator.textContent = `${swipeState.currentFileIndex + 1} / ${swipeState.files.length} files`;
      
      // Add touch events
      addTouchEvents(card);
    } else {
      progressIndicator.textContent = 'All files processed!';
      cardStack.innerHTML = '<div class="no-files">🎉 All files processed!</div>';
    }
  }

  // Add touch events for swipe gestures
  function addTouchEvents(card) {
    let startX = 0;
    let currentX = 0;
    let isDragging = false;

    card.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      isDragging = true;
    });

    card.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      
      currentX = e.touches[0].clientX;
      const deltaX = currentX - startX;
      const rotation = deltaX * 0.1;
      
      card.style.transform = `translateX(${deltaX}px) rotate(${rotation}deg)`;
      
      // Show labels based on swipe direction
      if (deltaX < -50) {
        deleteLabel.classList.add('visible');
        keepLabel.classList.remove('visible');
      } else if (deltaX > 50) {
        keepLabel.classList.add('visible');
        deleteLabel.classList.remove('visible');
      } else {
        deleteLabel.classList.remove('visible');
        keepLabel.classList.remove('visible');
      }
    });

    card.addEventListener('touchend', (e) => {
      if (!isDragging) return;
      isDragging = false;
      
      const deltaX = currentX - startX;
      
      if (Math.abs(deltaX) > 100) {
        // Swipe threshold reached
        swipe(deltaX < 0 ? 'left' : 'right');
      } else {
        // Snap back
        card.style.transform = '';
        deleteLabel.classList.remove('visible');
        keepLabel.classList.remove('visible');
      }
    });

    // Mouse events for desktop testing
    card.addEventListener('mousedown', (e) => {
      startX = e.clientX;
      isDragging = true;
    });

    card.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      
      currentX = e.clientX;
      const deltaX = currentX - startX;
      const rotation = deltaX * 0.1;
      
      card.style.transform = `translateX(${deltaX}px) rotate(${rotation}deg)`;
      
      if (deltaX < -50) {
        deleteLabel.classList.add('visible');
        keepLabel.classList.remove('visible');
      } else if (deltaX > 50) {
        keepLabel.classList.add('visible');
        deleteLabel.classList.remove('visible');
      } else {
        deleteLabel.classList.remove('visible');
        keepLabel.classList.remove('visible');
      }
    });

    card.addEventListener('mouseup', (e) => {
      if (!isDragging) return;
      isDragging = false;
      
      const deltaX = currentX - startX;
      
      if (Math.abs(deltaX) > 100) {
        swipe(deltaX < 0 ? 'left' : 'right');
      } else {
        card.style.transform = '';
        deleteLabel.classList.remove('visible');
        keepLabel.classList.remove('visible');
      }
    });
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
        const action = direction === 'left' ? 'Deleted' : 'Kept';
        console.log(`${action}: ${swipeState.files[swipeState.currentFileIndex].name}`);
        
        swipeState.currentFileIndex++;
        renderCard();
        label.classList.remove('visible');
        swipeState.isSwiping = false;
      }, 300);
    }
  }

  // Button actions
  deleteButton.addEventListener('click', () => swipe('left'));
  keepButton.addEventListener('click', () => swipe('right'));
  
  skipButton.addEventListener('click', () => {
    if (swipeState.files[swipeState.currentFileIndex]) {
      console.log(`Skipped: ${swipeState.files[swipeState.currentFileIndex].name}`);
      swipeState.currentFileIndex++;
      renderCard();
    }
  });

  previewButton.addEventListener('click', () => {
    const currentFile = swipeState.files[swipeState.currentFileIndex];
    if (currentFile) {
      window.open(currentFile.path, '_blank');
    }
  });

  // Initial render
  renderCard();
  document.querySelector('.swipe-container').classList.add('active');
});