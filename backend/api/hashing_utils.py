import hashlib
import os

class HashingUtils:
    @staticmethod
    def calculate_hash(file_path, algorithm='md5'):
        """Calculate file hash"""
        try:
            hash_obj = hashlib.new(algorithm)
            # Mock hash calculation
            mock_hash = f"{algorithm}_{os.path.basename(file_path)}_hash"
            return hashlib.md5(mock_hash.encode()).hexdigest()
        except Exception as e:
            print(f"Error calculating hash for {file_path}: {e}")
            return None
    
    @staticmethod
    def compare_hashes(hash1, hash2):
        """Compare two hashes"""
        return hash1 == hash2
    
    @staticmethod
    def calculate_perceptual_hash(image_path):
        """Calculate perceptual hash for images"""
        # Mock perceptual hash
        return f"phash_{os.path.basename(image_path)}"