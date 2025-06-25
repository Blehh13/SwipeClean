import pytest
import os
from backend.api.hashing_utils import HashingUtils
from backend.api.image_utils import ImageUtils
from backend.api.storage_utils import StorageUtils
from backend.models.file_model import FileModel
from backend.models.session_model import CleaningSession

class TestHashingUtils:
    def test_calculate_hash(self):
        """Test hash calculation"""
        hash_result = HashingUtils.calculate_hash('/test/file.jpg')
        assert hash_result is not None
        assert isinstance(hash_result, str)
        assert len(hash_result) > 0

    def test_compare_hashes(self):
        """Test hash comparison"""
        hash1 = "abc123"
        hash2 = "abc123"
        hash3 = "def456"
        
        assert HashingUtils.compare_hashes(hash1, hash2) == True
        assert HashingUtils.compare_hashes(hash1, hash3) == False

    def test_perceptual_hash(self):
        """Test perceptual hash calculation"""
        phash = HashingUtils.calculate_perceptual_hash('/test/image.jpg')
        assert phash is not None
        assert isinstance(phash, str)

class TestImageUtils:
    def test_get_image_dimensions(self):
        """Test getting image dimensions"""
        dimensions = ImageUtils.get_image_dimensions('/test/image.jpg')
        assert dimensions is not None
        assert 'width' in dimensions
        assert 'height' in dimensions

    def test_blur_detection(self):
        """Test blur detection"""
        is_blurry = ImageUtils.is_blurry('/test/image.jpg')
        assert isinstance(is_blurry, bool)

    def test_image_metadata(self):
        """Test image metadata extraction"""
        metadata = ImageUtils.get_image_metadata('/test/image.jpg')
        assert metadata is not None
        assert 'format' in metadata
        assert 'size' in metadata

    def test_resize_image(self):
        """Test image resizing"""
        success = ImageUtils.resize_image('/test/input.jpg', '/test/output.jpg', (800, 600))
        assert isinstance(success, bool)

class TestStorageUtils:
    def test_get_storage_info(self):
        """Test storage information retrieval"""
        storage_info = StorageUtils.get_storage_info()
        assert 'total' in storage_info
        assert 'used' in storage_info
        assert 'available' in storage_info
        assert 'percentage_used' in storage_info

    def test_directory_size(self):
        """Test directory size calculation"""
        size = StorageUtils.get_directory_size('/test/directory')
        assert isinstance(size, int)
        assert size >= 0

    def test_move_to_trash(self):
        """Test moving file to trash"""
        success = StorageUtils.move_to_trash('/test/file.jpg')
        assert isinstance(success, bool)

    def test_empty_trash(self):
        """Test emptying trash"""
        success = StorageUtils.empty_trash()
        assert isinstance(success, bool)

class TestFileModel:
    def test_file_model_creation(self):
        """Test creating file model"""
        file_model = FileModel('/test/photo.jpg', size=1024000)
        assert file_model.path == '/test/photo.jpg'
        assert file_model.name == 'photo.jpg'
        assert file_model.size == 1024000
        assert file_model.type == 'image'

    def test_file_type_detection(self):
        """Test file type detection"""
        image_file = FileModel('/test/photo.jpg')
        video_file = FileModel('/test/video.mp4')
        document_file = FileModel('/test/document.pdf')
        
        assert image_file.type == 'image'
        assert video_file.type == 'video'
        assert document_file.type == 'document'

    def test_file_model_to_dict(self):
        """Test converting file model to dictionary"""
        file_model = FileModel('/test/photo.jpg', size=1024000)
        file_dict = file_model.to_dict()
        
        assert isinstance(file_dict, dict)
        assert file_dict['path'] == '/test/photo.jpg'
        assert file_dict['size'] == 1024000

    def test_file_model_from_dict(self):
        """Test creating file model from dictionary"""
        file_data = {
            'path': '/test/photo.jpg',
            'name': 'photo.jpg',
            'size': 1024000,
            'type': 'image'
        }
        
        file_model = FileModel.from_dict(file_data)
        assert file_model.path == '/test/photo.jpg'
        assert file_model.size == 1024000

    def test_size_conversion(self):
        """Test size conversion to MB"""
        file_model = FileModel('/test/photo.jpg', size=1048576)  # 1MB
        assert file_model.get_size_mb() == 1.0

    def test_file_type_checks(self):
        """Test file type checking methods"""
        image_file = FileModel('/test/photo.jpg')
        video_file = FileModel('/test/video.mp4')
        
        assert image_file.is_image() == True
        assert image_file.is_video() == False
        assert video_file.is_image() == False
        assert video_file.is_video() == True

class TestCleaningSession:
    def test_session_creation(self):
        """Test creating cleaning session"""
        session = CleaningSession(user_id=1)
        assert session.user_id == 1
        assert session.files_processed == 0
        assert session.files_deleted == 0
        assert session.is_active == True

    def test_add_processed_file(self):
        """Test adding processed file to session"""
        session = CleaningSession()
        session.add_processed_file(1024000, deleted=True)
        
        assert session.files_processed == 1
        assert session.files_deleted == 1
        assert session.space_freed == 1024000

    def test_session_statistics(self):
        """Test session statistics calculation"""
        session = CleaningSession()
        session.add_processed_file(1048576, deleted=True)  # 1MB
        session.add_processed_file(2097152, deleted=False)  # 2MB
        
        assert session.get_space_freed_mb() == 1.0
        assert session.get_deletion_rate() == 50.0

    def test_session_to_dict(self):
        """Test converting session to dictionary"""
        session = CleaningSession(user_id=1)
        session.add_processed_file(1048576, deleted=True)
        
        session_dict = session.to_dict()
        assert isinstance(session_dict, dict)
        assert session_dict['user_id'] == 1
        assert session_dict['files_processed'] == 1

    def test_session_from_dict(self):
        """Test creating session from dictionary"""
        session_data = {
            'user_id': 1,
            'files_processed': 5,
            'files_deleted': 3,
            'space_freed': 5242880
        }
        
        session = CleaningSession.from_dict(session_data)
        assert session.user_id == 1
        assert session.files_processed == 5
        assert session.files_deleted == 3

    def test_end_session(self):
        """Test ending cleaning session"""
        session = CleaningSession()
        assert session.is_active == True
        
        session.end_session()
        assert session.is_active == False
        assert session.ended_at is not None