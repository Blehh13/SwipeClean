from datetime import datetime
import os

class FileModel:
    def __init__(self, path, name=None, size=None, file_type=None):
        self.path = path
        self.name = name or os.path.basename(path)
        self.size = size or 0
        self.type = file_type or self._detect_type()
        self.hash = None
        self.created_at = datetime.now()
        self.modified_at = None
        self.is_deleted = False
    
    def _detect_type(self):
        """Detect file type from extension"""
        ext = os.path.splitext(self.path)[1].lower()
        
        image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
        video_exts = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv']
        audio_exts = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
        document_exts = ['.pdf', '.doc', '.docx', '.txt', '.rtf']
        
        if ext in image_exts:
            return 'image'
        elif ext in video_exts:
            return 'video'
        elif ext in audio_exts:
            return 'audio'
        elif ext in document_exts:
            return 'document'
        else:
            return 'other'
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'path': self.path,
            'name': self.name,
            'size': self.size,
            'type': self.type,
            'hash': self.hash,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'modified_at': self.modified_at.isoformat() if self.modified_at else None,
            'is_deleted': self.is_deleted
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create instance from dictionary"""
        instance = cls(
            path=data['path'],
            name=data.get('name'),
            size=data.get('size'),
            file_type=data.get('type')
        )
        instance.hash = data.get('hash')
        instance.is_deleted = data.get('is_deleted', False)
        
        if data.get('created_at'):
            instance.created_at = datetime.fromisoformat(data['created_at'])
        if data.get('modified_at'):
            instance.modified_at = datetime.fromisoformat(data['modified_at'])
        
        return instance
    
    def get_size_mb(self):
        """Get size in MB"""
        return round(self.size / (1024 * 1024), 2) if self.size else 0
    
    def is_image(self):
        """Check if file is an image"""
        return self.type == 'image'
    
    def is_video(self):
        """Check if file is a video"""
        return self.type == 'video'