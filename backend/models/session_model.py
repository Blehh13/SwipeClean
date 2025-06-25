from datetime import datetime

class CleaningSession:
    def __init__(self, user_id=None):
        self.id = None
        self.user_id = user_id
        self.started_at = datetime.now()
        self.ended_at = None
        self.files_processed = 0
        self.files_deleted = 0
        self.space_freed = 0  # in bytes
        self.is_active = True
    
    def add_processed_file(self, file_size, deleted=False):
        """Add a processed file to the session"""
        self.files_processed += 1
        if deleted:
            self.files_deleted += 1
            self.space_freed += file_size
    
    def end_session(self):
        """End the cleaning session"""
        self.ended_at = datetime.now()
        self.is_active = False
    
    def get_duration_minutes(self):
        """Get session duration in minutes"""
        if not self.ended_at:
            end_time = datetime.now()
        else:
            end_time = self.ended_at
        
        duration = end_time - self.started_at
        return round(duration.total_seconds() / 60, 2)
    
    def get_space_freed_mb(self):
        """Get space freed in MB"""
        return round(self.space_freed / (1024 * 1024), 2)
    
    def get_deletion_rate(self):
        """Get deletion rate as percentage"""
        if self.files_processed == 0:
            return 0
        return round((self.files_deleted / self.files_processed) * 100, 1)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'started_at': self.started_at.isoformat(),
            'ended_at': self.ended_at.isoformat() if self.ended_at else None,
            'files_processed': self.files_processed,
            'files_deleted': self.files_deleted,
            'space_freed': self.space_freed,
            'space_freed_mb': self.get_space_freed_mb(),
            'duration_minutes': self.get_duration_minutes(),
            'deletion_rate': self.get_deletion_rate(),
            'is_active': self.is_active
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create instance from dictionary"""
        instance = cls(user_id=data.get('user_id'))
        instance.id = data.get('id')
        instance.files_processed = data.get('files_processed', 0)
        instance.files_deleted = data.get('files_deleted', 0)
        instance.space_freed = data.get('space_freed', 0)
        instance.is_active = data.get('is_active', True)
        
        if data.get('started_at'):
            instance.started_at = datetime.fromisoformat(data['started_at'])
        if data.get('ended_at'):
            instance.ended_at = datetime.fromisoformat(data['ended_at'])
        
        return instance