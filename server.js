import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Set up view engine for HTML templates
app.set('views', path.join(__dirname, 'templates'));
app.set('view engine', 'html');
app.engine('html', (filePath, options, callback) => {
  import('fs').then(fs => {
    fs.readFile(filePath, (err, content) => {
      if (err) return callback(err);
      return callback(null, content.toString());
    });
  });
});

// Mock data for demo
const MOCK_FILES = [
    {
        id: 1,
        path: 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=400',
        name: 'Beautiful Landscape',
        size: '2.3 MB',
        type: 'image'
    },
    {
        id: 2,
        path: 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=400',
        name: 'City View',
        size: '1.8 MB',
        type: 'image'
    },
    {
        id: 3,
        path: 'https://images.pexels.com/photos/326055/pexels-photo-326055.jpeg?auto=compress&cs=tinysrgb&w=400',
        name: 'Nature Photo',
        size: '3.1 MB',
        type: 'image'
    },
    {
        id: 4,
        path: 'https://images.pexels.com/photos/1366919/pexels-photo-1366919.jpeg?auto=compress&cs=tinysrgb&w=400',
        name: 'Mountain View',
        size: '2.7 MB',
        type: 'image'
    }
];

const AI_SUGGESTIONS = [
    {
        id: 1,
        path: 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=400',
        reason: 'Duplicate detected',
        confidence: 0.95,
        size: '2.3 MB'
    },
    {
        id: 2,
        path: 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=400',
        reason: 'Blurry image',
        confidence: 0.87,
        size: '1.8 MB'
    }
];

// Routes
app.get('/', (req, res) => {
    res.render('index');
});

app.get('/swipe', (req, res) => {
    res.render('swipe');
});

app.get('/suggestions', (req, res) => {
    res.render('suggestions');
});

app.get('/browser', (req, res) => {
    res.render('browser');
});

app.get('/settings', (req, res) => {
    res.render('settings');
});

app.get('/permissions', (req, res) => {
    res.render('permissions');
});

// API Routes
app.get('/api/files', (req, res) => {
    res.json({ files: MOCK_FILES });
});

app.get('/api/suggestions', (req, res) => {
    res.json({ suggestions: AI_SUGGESTIONS });
});

app.get('/api/storage', (req, res) => {
    res.json({
        used: 12.4,
        total: 64.0,
        available: 51.6
    });
});

app.post('/api/delete', (req, res) => {
    const fileId = req.body.id;
    // Mock deletion
    res.json({ success: true, message: `File ${fileId} deleted` });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on http://localhost:${PORT}`);
});