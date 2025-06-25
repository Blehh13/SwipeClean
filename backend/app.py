from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from api.auth_routes import auth_bp
from api.file_routes import file_bp
from api.ai_routes import ai_bp
from api.cloud_routes import cloud_bp

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(file_bp, url_prefix='/api/files')
app.register_blueprint(ai_bp, url_prefix='/api/ai')
app.register_blueprint(cloud_bp, url_prefix='/api/cloud')

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

@app.route('/api/storage/info')
def storage_info():
    return jsonify({
        'used': 12.4,
        'total': 64.0,
        'available': 51.6
    })

@app.route('/api/insights')
def insights():
    return jsonify({
        'storageByCategory': {
            'photos': 8.2,
            'videos': 3.1,
            'screenshots': 0.8,
            'others': 0.3
        },
        'cleanedThisWeek': {
            'size': 2.1,
            'count': 47
        },
        'recommendedSize': 1.8,
        'aiConfidence': 92
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)