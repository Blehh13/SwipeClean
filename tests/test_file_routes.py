import pytest
import json
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_scan_files(client):
    """Test file scanning endpoint"""
    response = client.get('/api/files/scan')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'files' in data
    assert 'count' in data
    assert isinstance(data['files'], list)
    assert data['count'] == len(data['files'])

def test_file_info(client):
    """Test file information endpoint"""
    response = client.get('/api/files/info/test/photo.jpg')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'path' in data
    assert 'size' in data
    assert 'type' in data
    assert 'hash' in data

def test_find_duplicates(client):
    """Test duplicate file detection"""
    response = client.get('/api/files/duplicates')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'duplicates' in data
    assert 'count' in data
    assert isinstance(data['duplicates'], list)

def test_delete_files(client):
    """Test file deletion endpoint"""
    files_to_delete = ['/test/photo1.jpg', '/test/video1.mp4']
    
    response = client.post('/api/files/delete', 
                          json={'files': files_to_delete})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'results' in data
    assert 'success' in data
    assert len(data['results']) == len(files_to_delete)

def test_delete_empty_list(client):
    """Test deleting empty file list"""
    response = client.post('/api/files/delete', json={'files': []})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['results'] == []

def test_delete_invalid_request(client):
    """Test delete with invalid request format"""
    response = client.post('/api/files/delete', json={})
    # Should handle missing 'files' key gracefully
    assert response.status_code in [200, 400]

def test_file_info_nonexistent(client):
    """Test getting info for non-existent file"""
    response = client.get('/api/files/info/nonexistent/file.jpg')
    # Should return mock data or handle gracefully
    assert response.status_code in [200, 404]

def test_scan_with_parameters(client):
    """Test file scanning with query parameters"""
    response = client.get('/api/files/scan?types=image,video')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'files' in data

def test_file_deletion_results(client):
    """Test file deletion results format"""
    files_to_delete = ['/test/photo1.jpg']
    
    response = client.post('/api/files/delete', 
                          json={'files': files_to_delete})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    for result in data['results']:
        assert 'path' in result
        assert 'deleted' in result
        assert isinstance(result['deleted'], bool)

def test_duplicate_detection_format(client):
    """Test duplicate detection response format"""
    response = client.get('/api/files/duplicates')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    for duplicate_group in data['duplicates']:
        assert 'hash' in duplicate_group
        assert 'files' in duplicate_group
        assert isinstance(duplicate_group['files'], list)