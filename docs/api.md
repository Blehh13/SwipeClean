# SwipeClean API Documentation

## Overview

The SwipeClean API provides endpoints for file management, AI-powered suggestions, cloud integration, and user authentication.

Base URL: `http://localhost:5000/api`

## Authentication

### Request Storage Permission

Request permission to access device storage.

**Endpoint:** `POST /auth/request-storage`

**Response:**
```json
{
  "success": true,
  "message": "Storage permission granted"
}
```

### Check Permissions

Check current permission status.

**Endpoint:** `GET /auth/check-permissions`

**Response:**
```json
{
  "storage": true,
  "camera": false,
  "notifications": true
}
```

## File Management

### Scan Files

Scan device directories for files.

**Endpoint:** `GET /files/scan`

**Query Parameters:**
- `directory` (optional): Specific directory to scan
- `types` (optional): File types to include (image,video,document)

**Response:**
```json
{
  "files": [
    {
      "path": "/storage/photo1.jpg",
      "name": "photo1.jpg",
      "size": 6291456,
      "type": "image",
      "modified": "2024-01-15T10:30:00Z"
    }
  ],
  "count": 1
}
```

### Delete Files

Delete selected files from device.

**Endpoint:** `POST /files/delete`

**Request Body:**
```json
{
  "files": ["/storage/photo1.jpg", "/storage/video1.mp4"]
}
```

**Response:**
```json
{
  "results": [
    {
      "path": "/storage/photo1.jpg",
      "deleted": true
    }
  ],
  "success": true
}
```

### Get File Information

Get detailed information about a specific file.

**Endpoint:** `GET /files/info/<path>`

**Response:**
```json
{
  "path": "/storage/photo1.jpg",
  "size": 6291456,
  "type": "image",
  "created": "2024-01-15T10:30:00Z",
  "modified": "2024-01-15T10:30:00Z",
  "hash": "abc123def456"
}
```

### Find Duplicates

Find duplicate files based on hash comparison.

**Endpoint:** `GET /files/duplicates`

**Response:**
```json
{
  "duplicates": [
    {
      "hash": "abc123",
      "files": [
        {"path": "/storage/photo1.jpg", "size": 6291456},
        {"path": "/storage/photo1_copy.jpg", "size": 6291456}
      ]
    }
  ],
  "count": 1
}
```

## AI-Powered Features

### Get AI Suggestions

Get AI-powered file cleaning suggestions.

**Endpoint:** `GET /ai/suggestions`

**Query Parameters:**
- `types` (optional): Suggestion types to include
- `confidence` (optional): Minimum confidence threshold (0.0-1.0)

**Response:**
```json
{
  "suggestions": [
    {
      "path": "/storage/photo1.jpg",
      "reason": "Duplicate detected",
      "confidence": 0.95,
      "size": 6291456,
      "type": "image"
    }
  ],
  "confidence": 0.92,
  "total_size": 6291456
}
```

### Analyze Image Quality

Analyze image quality using AI.

**Endpoint:** `POST /ai/analyze-image`

**Request Body:**
```json
{
  "path": "/storage/photo1.jpg"
}
```

**Response:**
```json
{
  "blur_score": 0.15,
  "brightness": 0.7,
  "quality_score": 0.85,
  "is_blurry": false,
  "recommendations": ["Good quality image"]
}
```

### AI Duplicate Detection

Advanced duplicate detection using perceptual hashing.

**Endpoint:** `POST /ai/detect-duplicates`

**Request Body:**
```json
{
  "files": ["/storage/photo1.jpg", "/storage/photo2.jpg"]
}
```

**Response:**
```json
{
  "duplicates": [
    {
      "group_id": 1,
      "files": ["/storage/photo1.jpg", "/storage/photo2.jpg"],
      "similarity": 0.98,
      "method": "perceptual_hash"
    }
  ],
  "method": "perceptual_hash"
}
```

## Cloud Integration

### Connect to Cloud Provider

Connect to a cloud storage provider.

**Endpoint:** `POST /cloud/connect/<provider>`

**Supported Providers:** `google_drive`, `onedrive`, `dropbox`

**Request Body:**
```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "redirect_uri": "your_redirect_uri"
}
```

**Response:**
```json
{
  "connected": true,
  "provider": "google_drive"
}
```

### Sync Files

Sync files with cloud storage.

**Endpoint:** `POST /cloud/sync`

**Request Body:**
```json
{
  "provider": "google_drive",
  "files": ["/storage/photo1.jpg", "/storage/video1.mp4"]
}
```

**Response:**
```json
{
  "synced_files": [
    {
      "file": "/storage/photo1.jpg",
      "synced": true,
      "cloud_path": "google_drive:///storage/photo1.jpg"
    }
  ],
  "total": 1,
  "success": true
}
```

### Cloud Status

Get cloud connection status.

**Endpoint:** `GET /cloud/status`

**Response:**
```json
{
  "google_drive": false,
  "onedrive": false,
  "dropbox": false
}
```

## Storage Information

### Get Storage Info

Get device storage information.

**Endpoint:** `GET /storage/info`

**Response:**
```json
{
  "used": 12.4,
  "total": 64.0,
  "available": 51.6
}
```

### Get Insights

Get storage insights and analytics.

**Endpoint:** `GET /insights`

**Response:**
```json
{
  "storageByCategory": {
    "photos": 8.2,
    "videos": 3.1,
    "screenshots": 0.8,
    "others": 0.3
  },
  "cleanedThisWeek": {
    "size": 2.1,
    "count": 47
  },
  "recommendedSize": 1.8,
  "aiConfidence": 92
}
```

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

Error responses include a descriptive message:

```json
{
  "error": "File not found",
  "code": 404
}
```

## Rate Limiting

API requests are limited to 100 requests per minute per client.

## Authentication

Some endpoints require storage permissions. Include the permission status in your requests or check permissions first using the `/auth/check-permissions` endpoint.