import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
FRONTEND_DIR = BASE_DIR / 'frontend'
BACKEND_DIR = BASE_DIR / 'backend'
TESTS_DIR = BASE_DIR / 'tests'

# Frontend paths
ASSETS_DIR = FRONTEND_DIR / 'assets'
CSS_DIR = FRONTEND_DIR / 'css'
JS_DIR = FRONTEND_DIR / 'js'
IMAGES_DIR = ASSETS_DIR / 'images'
ICONS_DIR = ASSETS_DIR / 'icons'
ANIMATIONS_DIR = ASSETS_DIR / 'animations'

# Backend paths
API_DIR = BACKEND_DIR / 'api'
MODELS_DIR = BACKEND_DIR / 'models'
DB_DIR = BACKEND_DIR / 'db'
CLOUD_DIR = BACKEND_DIR / 'cloud'

# Data paths
DATA_DIR = BASE_DIR / 'data'
CACHE_DIR = DATA_DIR / 'cache'
LOGS_DIR = DATA_DIR / 'logs'
TEMP_DIR = DATA_DIR / 'temp'
THUMBNAILS_DIR = CACHE_DIR / 'thumbnails'

# Database paths
DATABASE_FILE = DB_DIR / 'swipeclean.db'
SCHEMA_FILE = DB_DIR / 'schema.sql'

# Log file paths
APP_LOG_FILE = LOGS_DIR / 'app.log'
ERROR_LOG_FILE = LOGS_DIR / 'error.log'
ACCESS_LOG_FILE = LOGS_DIR / 'access.log'

# Configuration file paths
CONFIG_DIR = BASE_DIR / 'config'
SETTINGS_FILE = CONFIG_DIR / 'settings.json'

# Test data paths
TEST_DATA_DIR = TESTS_DIR / 'data'
MOCK_IMAGES_DIR = TEST_DATA_DIR / 'images'
MOCK_VIDEOS_DIR = TEST_DATA_DIR / 'videos'

# Device-specific paths (these would be different on actual mobile devices)
DEVICE_DCIM_PATH = '/storage/emulated/0/DCIM'
DEVICE_DOWNLOADS_PATH = '/storage/emulated/0/Download'
DEVICE_PICTURES_PATH = '/storage/emulated/0/Pictures'
DEVICE_MOVIES_PATH = '/storage/emulated/0/Movies'
DEVICE_SCREENSHOTS_PATH = '/storage/emulated/0/Pictures/Screenshots'

# Cloud storage paths
GOOGLE_DRIVE_FOLDER = 'SwipeClean'
ONEDRIVE_FOLDER = 'Apps/SwipeClean'
DROPBOX_FOLDER = '/SwipeClean'

def ensure_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        DATA_DIR, CACHE_DIR, LOGS_DIR, TEMP_DIR, 
        THUMBNAILS_DIR, MOCK_IMAGES_DIR, MOCK_VIDEOS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def get_user_data_dir():
    """Get user-specific data directory"""
    if os.name == 'nt':  # Windows
        return Path(os.environ.get('APPDATA', '')) / 'SwipeClean'
    else:  # Unix-like systems
        return Path.home() / '.swipeclean'

def get_cache_dir():
    """Get cache directory"""
    if os.name == 'nt':  # Windows
        return Path(os.environ.get('LOCALAPPDATA', '')) / 'SwipeClean' / 'Cache'
    else:  # Unix-like systems
        return Path.home() / '.cache' / 'swipeclean'