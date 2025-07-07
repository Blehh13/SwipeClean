from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Mock data for demo
MOCK_FILES = [
    {
        'id': 1,
        'path': 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=400',
        'name': 'Beautiful Landscape',
        'size': '2.3 MB',
        'type': 'image'
    },
    {
        'id': 2,
        'path': 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=400',
        'name': 'City View',
        'size': '1.8 MB',
        'type': 'image'
    },
    {
        'id': 3,
        'path': 'https://images.pexels.com/photos/326055/pexels-photo-326055.jpeg?auto=compress&cs=tinysrgb&w=400',
        'name': 'Nature Photo',
        'size': '3.1 MB',
        'type': 'image'
    },
    {
        'id': 4,
        'path': 'https://images.pexels.com/photos/1366919/pexels-photo-1366919.jpeg?auto=compress&cs=tinysrgb&w=400',
        'name': 'Mountain View',
        'size': '2.7 MB',
        'type': 'image'
    }
]

AI_SUGGESTIONS = [
    {
        'id': 1,
        'path': 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=400',
        'reason': 'Duplicate detected',
        'confidence': 0.95,
        'size': '2.3 MB'
    },
    {
        'id': 2,
        'path': 'https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=400',
        'reason': 'Blurry image',
        'confidence': 0.87,
        'size': '1.8 MB'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/swipe')
def swipe():
    return render_template('swipe.html')

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

@app.route('/browser')
def browser():
    return render_template('browser.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/permissions')
def permissions():
    return render_template('permissions.html')

# API Routes
@app.route('/api/files')
def get_files():
    return jsonify({'files': MOCK_FILES})

@app.route('/api/suggestions')
def get_suggestions():
    return jsonify({'suggestions': AI_SUGGESTIONS})

@app.route('/api/storage')
def get_storage():
    return jsonify({
        'used': 12.4,
        'total': 64.0,
        'available': 51.6
    })

@app.route('/api/delete', methods=['POST'])
def delete_file():
    file_id = request.json.get('id')
    # Mock deletion
    return jsonify({'success': True, 'message': f'File {file_id} deleted'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)