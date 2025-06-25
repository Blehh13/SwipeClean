class CloudUtils:
    def __init__(self):
        self.connections = {}
    
    def connect(self, provider, credentials):
        """Connect to cloud storage provider"""
        try:
            # Mock connection
            self.connections[provider] = {
                'connected': True,
                'credentials': credentials
            }
            print(f"Mock connected to {provider}")
            return True
        except Exception as e:
            print(f"Error connecting to {provider}: {e}")
            return False
    
    def sync_files(self, provider, files):
        """Sync files with cloud storage"""
        if provider not in self.connections:
            return {'error': 'Not connected to provider'}
        
        results = []
        for file_path in files:
            results.append({
                'file': file_path,
                'synced': True,
                'cloud_path': f"{provider}://{file_path}"
            })
        
        return {
            'synced_files': results,
            'total': len(files),
            'success': True
        }
    
    def get_cloud_storage_info(self, provider):
        """Get cloud storage information"""
        return {
            'total': 15.0,  # GB
            'used': 8.2,    # GB
            'available': 6.8  # GB
        }