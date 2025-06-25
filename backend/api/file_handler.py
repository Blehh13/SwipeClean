import os
import hashlib
from datetime import datetime
from .hashing_utils import HashingUtils
from .image_utils import ImageUtils

class FileHandler:
    def __init__(self):
        self.hashing_utils = HashingUtils()
        self.image_utils = ImageUtils()
    
    def scan_directory(self, directory_path):
        """Scan directory for files"""
        files = []
        mock_files = [
            {
                'path': 'assets/files/photo1.jpg',
                'name': 'photo1.jpg',
                'size': 6.2,
                'type': 'image',
                'modified': '2024-01-15T10:30:00Z'
            },
            {
                'path': 'assets/files/photo2.jpg',
                'name': 'photo2.jpg',
                'size': 3.5,
                'type': 'image',
                'modified': '2024-01-14T15:20:00Z'
            },
            {
                'path': 'assets/files/video1.mp4',
                'name': 'video1.mp4',
                'size': 15.8,
                'type': 'video',
                'modified': '2024-01-13T09:45:00Z'
            }
        ]
        return mock_files
    
    def delete_file(self, file_path):
        """Delete a file"""
        try:
            # Mock deletion - in real app would use os.remove()
            print(f"Mock deleting file: {file_path}")
            return True
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
            return False
    
    def get_file_info(self, file_path):
        """Get detailed file information"""
        return {
            'path': file_path,
            'size': 5.2,
            'type': 'image',
            'created': '2024-01-15T10:30:00Z',
            'modified': '2024-01-15T10:30:00Z',
            'hash': self.hashing_utils.calculate_hash(file_path)
        }
    
    def find_duplicates(self):
        """Find duplicate files based on hash"""
        duplicates = [
            {
                'hash': 'abc123',
                'files': [
                    {'path': 'assets/files/photo1.jpg', 'size': 6.2},
                    {'path': 'assets/files/photo1_copy.jpg', 'size': 6.2}
                ]
            }
        ]
        return duplicates