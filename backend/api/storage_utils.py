import os
import shutil

class StorageUtils:
    @staticmethod
    def get_storage_info():
        """Get device storage information"""
        return {
            'total': 64.0,  # GB
            'used': 12.4,   # GB
            'available': 51.6,  # GB
            'percentage_used': 19.4
        }
    
    @staticmethod
    def get_directory_size(directory_path):
        """Calculate directory size"""
        # Mock directory size calculation
        return 1024 * 1024 * 100  # 100MB
    
    @staticmethod
    def move_to_trash(file_path):
        """Move file to trash/recycle bin"""
        try:
            print(f"Mock moving {file_path} to trash")
            return True
        except Exception as e:
            print(f"Error moving to trash: {e}")
            return False
    
    @staticmethod
    def empty_trash():
        """Empty trash/recycle bin"""
        try:
            print("Mock emptying trash")
            return True
        except Exception as e:
            print(f"Error emptying trash: {e}")
            return False