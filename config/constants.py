# SwipeClean Configuration Constants

# File type constants
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff']
SUPPORTED_VIDEO_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
SUPPORTED_AUDIO_FORMATS = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a']
SUPPORTED_DOCUMENT_FORMATS = ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx']

# AI processing constants
AI_CONFIDENCE_THRESHOLD = 0.8
BLUR_DETECTION_THRESHOLD = 100
DUPLICATE_SIMILARITY_THRESHOLD = 0.95
OLD_FILE_DAYS_THRESHOLD = 30

# Storage constants
MAX_FILE_SIZE_MB = 100
MIN_FREE_SPACE_MB = 500
CACHE_SIZE_LIMIT_MB = 50

# Cloud sync constants
CLOUD_PROVIDERS = ['google_drive', 'onedrive', 'dropbox']
SYNC_BATCH_SIZE = 10
MAX_RETRY_ATTEMPTS = 3

# UI constants
SWIPE_THRESHOLD_PX = 100
ANIMATION_DURATION_MS = 300
CARDS_PRELOAD_COUNT = 3

# API constants
API_TIMEOUT_SECONDS = 30
MAX_CONCURRENT_REQUESTS = 5
RATE_LIMIT_REQUESTS_PER_MINUTE = 100

# Database constants
DB_CONNECTION_TIMEOUT = 10
MAX_DB_CONNECTIONS = 20
QUERY_TIMEOUT_SECONDS = 30

# Logging constants
LOG_LEVEL = 'INFO'
LOG_FILE_MAX_SIZE_MB = 10
LOG_RETENTION_DAYS = 7

# Security constants
SESSION_TIMEOUT_MINUTES = 60
MAX_LOGIN_ATTEMPTS = 5
PASSWORD_MIN_LENGTH = 8

# Performance constants
THUMBNAIL_SIZE = (150, 150)
IMAGE_PREVIEW_SIZE = (800, 600)
VIDEO_THUMBNAIL_TIME_SECONDS = 1