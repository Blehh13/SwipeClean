import pytest
import json
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_cloud_status(client):
    """Test cloud connection status endpoint"""
    response = client.get('/api/cloud/status')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'google_drive' in data
    assert 'onedrive' in data
    assert 'dropbox' in data

def test_connect_google_drive(client):
    """Test connecting to Google Drive"""
    credentials = {
        'client_id': 'test_client_id',
        'client_secret': 'test_client_secret',
        'redirect_uri': 'http://localhost:5000/callback'
    }
    
    response = client.post('/api/cloud/connect/google_drive', json=credentials)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['connected'] == True
    assert data['provider'] == 'google_drive'

def test_connect_onedrive(client):
    """Test connecting to OneDrive"""
    credentials = {
        'client_id': 'test_client_id',
        'client_secret': 'test_client_secret'
    }
    
    response = client.post('/api/cloud/connect/onedrive', json=credentials)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['connected'] == True
    assert data['provider'] == 'onedrive'

def test_connect_dropbox(client):
    """Test connecting to Dropbox"""
    credentials = {
        'app_key': 'test_app_key',
        'app_secret': 'test_app_secret'
    }
    
    response = client.post('/api/cloud/connect/dropbox', json=credentials)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['connected'] == True
    assert data['provider'] == 'dropbox'

def test_sync_files(client):
    """Test file synchronization"""
    sync_request = {
        'provider': 'google_drive',
        'files': ['/test/photo1.jpg', '/test/video1.mp4']
    }
    
    response = client.post('/api/cloud/sync', json=sync_request)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'synced_files' in data
    assert data['success'] == True
    assert len(data['synced_files']) == 2

def test_sync_without_connection(client):
    """Test syncing files without connection"""
    sync_request = {
        'provider': 'unconnected_provider',
        'files': ['/test/photo1.jpg']
    }
    
    response = client.post('/api/cloud/sync', json=sync_request)
    # Should handle gracefully
    assert response.status_code in [200, 400]

def test_connect_invalid_provider(client):
    """Test connecting to invalid provider"""
    response = client.post('/api/cloud/connect/invalid_provider', 
                          json={'key': 'value'})
    assert response.status_code == 404

def test_sync_empty_file_list(client):
    """Test syncing empty file list"""
    sync_request = {
        'provider': 'google_drive',
        'files': []
    }
    
    response = client.post('/api/cloud/sync', json=sync_request)
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert len(data['synced_files']) == 0

def test_connect_missing_credentials(client):
    """Test connecting without proper credentials"""
    response = client.post('/api/cloud/connect/google_drive', json={})
    # Should handle missing credentials
    assert response.status_code in [200, 400, 500]