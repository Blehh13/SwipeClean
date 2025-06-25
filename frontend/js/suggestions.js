const suggestionsState = {
  suggestions: [
    { path: 'assets/files/photo1.jpg', type: 'image', reason: 'Duplicate', size: 6.2 },
    { path: 'assets/files/photo2.jpg', type: 'image', reason: 'Blurry', size: 3.5 },
    { path: 'assets/files/screenshot1.png', type: 'image', reason: 'Old Screenshot', size: 0.8 }
  ],
  filteredSuggestions: [],
  filters: { type: 'all', size: 'all' }
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  const suggestionsList = document.getElementById('suggestions-list');
  const filterType = document.getElementById('filter-type');
  const filterSize = document.getElementById('filter-size');
  const deleteAllButton = document.getElementById('delete-all-button');
  const reviewButton = document.getElementById('review-button');

  // Render suggestions
  function renderSuggestions() {
    suggestionsList.innerHTML = '';
    suggestionsState.filteredSuggestions = suggestionsState.suggestions.filter(suggestion => {
      const typeMatch = suggestionsState.filters.type === 'all' || suggestion.reason.toLowerCase().includes(suggestionsState.filters.type);
      const sizeMatch = suggestionsState.filters.size === 'all' ||
        (suggestionsState.filters.size === 'large' && suggestion.size > 5) ||
        (suggestionsState.filters.size === 'small' && suggestion.size < 1);
      return typeMatch && sizeMatch;
    });

    suggestionsState.filteredSuggestions.forEach(suggestion => {
      const card = document.createElement('div');
      card.classList.add('suggestion-card');
      card.innerHTML = `
        <img src="${suggestion.path}" alt="${suggestion.reason}">
        <p>${suggestion.reason} (${suggestion.size} MB)</p>
      `;
      suggestionsList.appendChild(card);
    });
  }

  // Filter change handlers
  filterType.addEventListener('change', (e) => {
    suggestionsState.filters.type = e.target.value;
    renderSuggestions();
  });

  filterSize.addEventListener('change', (e) => {
    suggestionsState.filters.size = e.target.value;
    renderSuggestions();
  });

  // Delete All button
  deleteAllButton.addEventListener('click', () => {
    if (document.hasStoragePermission === true)
    {
      console.log(`Deleted: ${suggestionsState.filteredSuggestions.map(s => s.path).join(', ')}`);
      suggestionsState.suggestions = suggestionsState.suggestions.filter(
        s => !suggestionsState.filteredSuggestions.includes(s)
      );
      renderSuggestions();
    } else {
      console.log(`No Storage Permission`);
    }
  });

  // Review button
  reviewButton.addEventListener('click', () => {
    window.location.href = 'swipe.html';
  });

  // Initial render
  renderSuggestions();
  document.querySelector('.suggestions-container').classList.add('active');
});