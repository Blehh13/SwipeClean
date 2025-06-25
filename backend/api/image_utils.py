from PIL import Image
import os

class ImageUtils:
    @staticmethod
    def get_image_dimensions(image_path):
        """Get image dimensions"""
        try:
            # Mock dimensions
            return {'width': 1920, 'height': 1080}
        except Exception as e:
            print(f"Error getting dimensions for {image_path}: {e}")
            return None
    
    @staticmethod
    def is_blurry(image_path, threshold=100):
        """Detect if image is blurry"""
        try:
            # Mock blur detection
            import random
            return random.choice([True, False])
        except Exception as e:
            print(f"Error analyzing blur for {image_path}: {e}")
            return False
    
    @staticmethod
    def get_image_metadata(image_path):
        """Extract image metadata"""
        return {
            'format': 'JPEG',
            'mode': 'RGB',
            'size': (1920, 1080),
            'has_exif': True,
            'created': '2024-01-15T10:30:00Z'
        }
    
    @staticmethod
    def resize_image(image_path, output_path, size):
        """Resize image"""
        try:
            print(f"Mock resizing {image_path} to {size}")
            return True
        except Exception as e:
            print(f"Error resizing image: {e}")
            return False