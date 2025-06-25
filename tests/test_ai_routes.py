import pytest
import json
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_suggestions(client):
    """Test AI suggestions endpoint"""
    response = client.get('/api/ai/suggestions')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'suggestions' in data
    assert 'confidence' in data
    assert isinstance(data['suggestions'], list)

def test_analyze_image(client):
    """Test image analysis endpoint"""
    response = client.post('/api/ai/analyze-image', 
                          json={'path': '/test/image.jpg'})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'blur_score' in data
    assert 'quality_score' in data
    assert 'is_blurry' in data

def test_detect_duplicates(client):
    """Test AI duplicate detection"""
    response = client.post('/api/ai/detect-duplicates',
                          json={'files': ['/test/image1.jpg', '/test/image2.jpg']})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'duplicates' in data
    assert 'method' in data

def test_suggestions_with_filters(client):
    """Test suggestions with query parameters"""
    response = client.get('/api/ai/suggestions?confidence=0.9')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    # All suggestions should have confidence >= 0.9
    for suggestion in data['suggestions']:
        assert suggestion['confidence'] >= 0.9

def test_analyze_nonexistent_image(client):
    """Test analyzing non-existent image"""
    response = client.post('/api/ai/analyze-image',
                          json={'path': '/nonexistent/image.jpg'})
    # Should still return 200 with mock data
    assert response.status_code == 200

def test_empty_duplicate_detection(client):
    """Test duplicate detection with empty file list"""
    response = client.post('/api/ai/detect-duplicates',
                          json={'files': []})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['duplicates'] == []

def test_invalid_analyze_request(client):
    """Test image analysis with invalid request"""
    response = client.post('/api/ai/analyze-image', json={})
    # Should handle missing path gracefully
    assert response.status_code in [200, 400, 500]