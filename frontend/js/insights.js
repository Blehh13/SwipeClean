const insightsState = {
  storageByCategory: { photos: 0, videos: 0, screenshots: 0, others: 0 },
  cleanedThisWeek: { size: 0, count: 0 },
  recommendedSize: 0,
  aiConfidence: 0,
  isLoading: false
};

async function loadInsights() {
  insightsState.isLoading = true;
  const response = await fetch('/api/insights');
  const data = await response.json();
  insightsState.storageByCategory = data.storageByCategory;
  insightsState.cleanedThisWeek = data.cleanedThisWeek;
  insightsState.recommendedSize = data.recommendedSize;
  insightsState.aiConfidence = data.aiConfidence;
  renderInsights();
  insightsState.isLoading = false;
}

function renderInsights() {
  document.getElementById('cleaned-size').textContent = `${insightsState.cleanedThisWeek.size} GB`;
  document.getElementById('cleaned-count').textContent = `Across ${insightsState.cleanedThisWeek.count} files`;
  document.getElementById('recommended-size').textContent = `${insightsState.recommendedSize} GB`;
  document.getElementById('ai-confidence-bar').style.width = `${insightsState.aiConfidence}%`;
  document.getElementById('ai-confidence-text').textContent = `${insightsState.aiConfidence}% accurate`;

  const ctx = document.getElementById('storage-chart').getContext('2d');
  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Photos', 'Videos', 'Screenshots', 'Others'],
      datasets: [{
        data: [
          insightsState.storageByCategory.photos,
          insightsState.storageByCategory.videos,
          insightsState.storageByCategory.screenshots,
          insightsState.storageByCategory.others
        ],
        backgroundColor: ['#8B5CF6', '#3B82F6', '#6B7280', '#D1D5DB']
      }]
    },
    options: { responsive: true }
  });
}

window.addEventListener('load', loadInsights);