# SwipeClean

A mobile-first web application for AI-powered file cleaning and storage management.

## Features

- **Swipe Interface**: Intuitive swipe gestures to keep or delete files
- **AI Suggestions**: Smart detection of duplicates, blurry photos, and old screenshots
- **File Browser**: Grid and list view for browsing files
- **Storage Insights**: Visual analytics of storage usage
- **Cloud Integration**: Sync with Google Drive, OneDrive, and Dropbox
- **Mobile Optimized**: Responsive design for mobile devices

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **Database**: SQLite/PostgreSQL with Supabase support
- **AI/ML**: OpenCV, scikit-image, imagehash
- **Cloud**: Google Drive API, Microsoft Graph API, Dropbox API

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+ (for development tools)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd swipeclean
```

2. Install Python dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
python backend/db/init_db.py
```

5. Start the development server:
```bash
python backend/app.py
```

The app will be available at `http://localhost:5000`

### Docker Setup

```bash
docker-compose up -d
```

## Project Structure

```
swipeclean/
├── frontend/           # Frontend assets
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   ├── assets/        # Images, icons, animations
│   └── *.html         # HTML pages
├── backend/           # Python backend
│   ├── api/           # API routes and handlers
│   ├── models/        # Data models
│   ├── db/            # Database schema and client
│   └── cloud/         # Cloud integration
├── config/            # Configuration files
├── tests/             # Test files
└── docs/              # Documentation
```

## API Endpoints

### Authentication
- `POST /api/auth/request-storage` - Request storage permission
- `GET /api/auth/check-permissions` - Check permission status

### Files
- `GET /api/files/scan` - Scan device for files
- `POST /api/files/delete` - Delete selected files
- `GET /api/files/info/<path>` - Get file information
- `GET /api/files/duplicates` - Find duplicate files

### AI
- `GET /api/ai/suggestions` - Get AI-powered suggestions
- `POST /api/ai/analyze-image` - Analyze image quality
- `POST /api/ai/detect-duplicates` - AI duplicate detection

### Cloud
- `POST /api/cloud/connect/<provider>` - Connect to cloud provider
- `POST /api/cloud/sync` - Sync files with cloud
- `GET /api/cloud/status` - Get cloud connection status

## Configuration

Edit `config/settings.json` to customize:

- AI detection thresholds
- Storage scan directories
- UI preferences
- Cloud provider settings
- Privacy and security options

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

The project follows PEP 8 for Python and standard JavaScript conventions.

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Mobile Deployment

### Android (Cordova/PhoneGap)
1. Install Cordova CLI
2. Add Android platform
3. Build and deploy

### iOS (Cordova/PhoneGap)
1. Install Cordova CLI
2. Add iOS platform
3. Build with Xcode

### Progressive Web App (PWA)
The app includes service worker support for PWA functionality.

## Privacy & Security

- Files are processed locally on device
- No data is sent to external servers without explicit consent
- Cloud sync is optional and user-controlled
- Secure deletion options available

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- Create an issue on GitHub
- Check the documentation in `/docs`
- Review the FAQ

## Roadmap

- [ ] Advanced AI models for better detection
- [ ] Batch operations for large file sets
- [ ] Integration with more cloud providers
- [ ] Desktop application version
- [ ] Advanced analytics and reporting