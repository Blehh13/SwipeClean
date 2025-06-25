class OneDriveIntegration:
    def __init__(self):
        self.authenticated = False
        self.access_token = None
    
    def authenticate(self, client_id, client_secret, redirect_uri):
        """Authenticate with OneDrive"""
        try:
            # Mock authentication
            self.authenticated = True
            self.access_token = "mock_onedrive_token"
            print("Mock OneDrive authentication successful")
            return True
        except Exception as e:
            print(f"OneDrive authentication error: {e}")
            return False
    
    def upload_file(self, file_path, remote_path=None):
        """Upload file to OneDrive"""
        if not self.authenticated:
            return {'error': 'Not authenticated'}
        
        return {
            'id': 'mock_onedrive_file_id',
            'name': file_path.split('/')[-1],
            'size': 1024000,
            'uploaded': True,
            'download_url': f"https://onedrive.com/mock/{file_path}"
        }
    
    def list_files(self, folder_path='/'):
        """List files in OneDrive"""
        if not self.authenticated:
            return {'error': 'Not authenticated'}
        
        return {
            'files': [
                {
                    'id': 'od_file1',
                    'name': 'document1.pdf',
                    'size': 2048000
                },
                {
                    'id': 'od_file2',
                    'name': 'photo2.jpg',
                    'size': 3072000
                }
            ]
        }
    
    def delete_file(self, file_id):
        """Delete file from OneDrive"""
        if not self.authenticated:
            return {'error': 'Not authenticated'}
        
        print(f"Mock deleting OneDrive file: {file_id}")
        return {'deleted': True}