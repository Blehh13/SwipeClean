-- SwipeClean Database Schema

-- Users table for storing user preferences
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settings TEXT DEFAULT '{}' -- JSON string for user settings
);

-- Files table for tracking scanned files
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    size INTEGER NOT NULL, -- Size in bytes
    type TEXT NOT NULL, -- image, video, document, etc.
    hash TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP,
    last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- AI suggestions table
CREATE TABLE IF NOT EXISTS ai_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    suggestion_type TEXT NOT NULL, -- duplicate, blurry, old_screenshot, etc.
    confidence REAL NOT NULL,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_processed BOOLEAN DEFAULT FALSE,
    user_action TEXT, -- keep, delete, ignore
    FOREIGN KEY (file_id) REFERENCES files (id)
);

-- Duplicate groups table
CREATE TABLE IF NOT EXISTS duplicate_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- File duplicates mapping
CREATE TABLE IF NOT EXISTS file_duplicates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER,
    file_id INTEGER,
    similarity_score REAL DEFAULT 1.0,
    FOREIGN KEY (group_id) REFERENCES duplicate_groups (id),
    FOREIGN KEY (file_id) REFERENCES files (id)
);

-- Cleaning sessions table
CREATE TABLE IF NOT EXISTS cleaning_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    files_processed INTEGER DEFAULT 0,
    files_deleted INTEGER DEFAULT 0,
    space_freed INTEGER DEFAULT 0, -- Bytes freed
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Cloud sync status
CREATE TABLE IF NOT EXISTS cloud_sync (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    provider TEXT NOT NULL, -- google_drive, onedrive, dropbox
    cloud_file_id TEXT,
    sync_status TEXT DEFAULT 'pending', -- pending, synced, failed
    last_sync TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES files (id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_files_path ON files(path);
CREATE INDEX IF NOT EXISTS idx_files_hash ON files(hash);
CREATE INDEX IF NOT EXISTS idx_files_type ON files(type);
CREATE INDEX IF NOT EXISTS idx_ai_suggestions_file_id ON ai_suggestions(file_id);
CREATE INDEX IF NOT EXISTS idx_ai_suggestions_type ON ai_suggestions(suggestion_type);
CREATE INDEX IF NOT EXISTS idx_file_duplicates_group_id ON file_duplicates(group_id);
CREATE INDEX IF NOT EXISTS idx_cloud_sync_file_id ON cloud_sync(file_id);