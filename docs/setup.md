# SwipeClean Setup Guide

## Development Environment Setup

### Prerequisites

Before setting up SwipeClean, ensure you have the following installed:

- **Python 3.8+** - Backend runtime
- **Node.js 16+** - For development tools (optional)
- **Git** - Version control
- **Code Editor** - VS Code, PyCharm, or similar

### 1. Clone the Repository

```bash
git clone <repository-url>
cd swipeclean
```

### 2. Python Environment Setup

Create a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r backend/requirements.txt
```

### 3. Environment Configuration

Create environment file:

```bash
cp .env.example .env
```

Edit `.env` file with your configuration:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here

# Database Configuration
DATABASE_URL=sqlite:///swipeclean.db
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key

# Cloud Provider Keys (Optional)
GOOGLE_DRIVE_CLIENT_ID=your-google-client-id
GOOGLE_DRIVE_CLIENT_SECRET=your-google-client-secret
ONEDRIVE_CLIENT_ID=your-onedrive-client-id
ONEDRIVE_CLIENT_SECRET=your-onedrive-client-secret
DROPBOX_APP_KEY=your-dropbox-app-key
DROPBOX_APP_SECRET=your-dropbox-app-secret

# AI/ML Configuration
OPENCV_ENABLED=true
AI_CONFIDENCE_THRESHOLD=0.8
```

### 4. Database Setup

Initialize the database:

```bash
# Create database tables
python -c "
from backend.db.supabase_client import SupabaseClient
import sqlite3

# For SQLite (development)
conn = sqlite3.connect('swipeclean.db')
with open('backend/db/schema.sql', 'r') as f:
    conn.executescript(f.read())
conn.close()
print('Database initialized successfully')
"
```

### 5. Start Development Server

```bash
python backend/app.py
```

The application will be available at `http://localhost:5000`

## Production Deployment

### Docker Deployment

1. **Build and run with Docker Compose:**

```bash
docker-compose up -d
```

2. **Check container status:**

```bash
docker-compose ps
```

3. **View logs:**

```bash
docker-compose logs -f swipeclean-app
```

### Manual Production Setup

1. **Install production dependencies:**

```bash
pip install gunicorn
```

2. **Set production environment:**

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
```

3. **Run with Gunicorn:**

```bash
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app
```

### Nginx Configuration

Create `/etc/nginx/sites-available/swipeclean`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/swipeclean/frontend;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/swipeclean /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Mobile App Setup

### Cordova/PhoneGap Setup

1. **Install Cordova CLI:**

```bash
npm install -g cordova
```

2. **Create Cordova project:**

```bash
cordova create swipeclean-mobile com.swipeclean.app SwipeClean
cd swipeclean-mobile
```

3. **Copy web assets:**

```bash
cp -r ../frontend/* www/
```

4. **Add platforms:**

```bash
cordova platform add android
cordova platform add ios
```

5. **Configure permissions in `config.xml`:**

```xml
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.CAMERA" />
```

6. **Build and run:**

```bash
# Android
cordova build android
cordova run android

# iOS
cordova build ios
cordova run ios
```

### Progressive Web App (PWA)

The app includes PWA support. To enable:

1. **Serve over HTTPS** (required for PWA features)
2. **Install service worker** (already included)
3. **Add to home screen** prompt will appear automatically

## Cloud Provider Setup

### Google Drive Integration

1. **Create Google Cloud Project:**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create new project
   - Enable Google Drive API

2. **Create OAuth 2.0 Credentials:**
   - Go to Credentials section
   - Create OAuth 2.0 Client ID
   - Add authorized redirect URIs

3. **Update environment variables:**

```env
GOOGLE_DRIVE_CLIENT_ID=your-client-id
GOOGLE_DRIVE_CLIENT_SECRET=your-client-secret
```

### OneDrive Integration

1. **Register app in Azure:**
   - Go to [Azure Portal](https://portal.azure.com)
   - Register new application
   - Configure Microsoft Graph permissions

2. **Update environment variables:**

```env
ONEDRIVE_CLIENT_ID=your-client-id
ONEDRIVE_CLIENT_SECRET=your-client-secret
```

### Dropbox Integration

1. **Create Dropbox App:**
   - Go to [Dropbox App Console](https://www.dropbox.com/developers/apps)
   - Create new app
   - Get app key and secret

2. **Update environment variables:**

```env
DROPBOX_APP_KEY=your-app-key
DROPBOX_APP_SECRET=your-app-secret
```

## Testing Setup

### Unit Tests

Run Python tests:

```bash
python -m pytest tests/ -v
```

### Frontend Tests

If using frontend testing framework:

```bash
npm test
```

### Integration Tests

Test API endpoints:

```bash
python -m pytest tests/test_api.py -v
```

## Troubleshooting

### Common Issues

1. **Permission Denied Errors:**
   - Check file permissions
   - Ensure proper user permissions for storage access

2. **Database Connection Issues:**
   - Verify database URL in environment variables
   - Check database server status

3. **Cloud API Errors:**
   - Verify API credentials
   - Check API quotas and limits

4. **Mobile App Issues:**
   - Check Cordova platform requirements
   - Verify device permissions

### Debug Mode

Enable debug logging:

```bash
export FLASK_DEBUG=1
export LOG_LEVEL=DEBUG
```

### Performance Monitoring

Monitor application performance:

```bash
# Check memory usage
ps aux | grep python

# Check disk usage
df -h

# Monitor logs
tail -f data/logs/app.log
```

## Security Considerations

1. **Environment Variables:**
   - Never commit `.env` files
   - Use secure secret keys
   - Rotate API keys regularly

2. **File Permissions:**
   - Limit file system access
   - Validate file paths
   - Sanitize user inputs

3. **HTTPS:**
   - Always use HTTPS in production
   - Configure SSL certificates
   - Enable HSTS headers

4. **Database Security:**
   - Use parameterized queries
   - Enable database encryption
   - Regular security updates

## Monitoring and Maintenance

1. **Log Monitoring:**
   - Set up log rotation
   - Monitor error rates
   - Alert on critical issues

2. **Performance Monitoring:**
   - Track response times
   - Monitor resource usage
   - Set up health checks

3. **Backup Strategy:**
   - Regular database backups
   - User data backup procedures
   - Disaster recovery plan

For additional help, check the [API Documentation](api.md) or create an issue on GitHub.