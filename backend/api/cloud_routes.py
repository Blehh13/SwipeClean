from flask import Blueprint, request, jsonify
from cloud.cloud_utils import CloudUtils

cloud_bp = Blueprint('cloud', __name__)
cloud_utils = CloudUtils()

@cloud_bp.route('/connect/<provider>', methods=['POST'])
def connect_cloud(provider):
    """Connect to cloud storage provider"""
    try:
        credentials = request.json
        success = cloud_utils.connect(provider, credentials)
        return jsonify({
            'connected': success,
            'provider': provider
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cloud_bp.route('/sync', methods=['POST'])
def sync_files():
    """Sync files with cloud storage"""
    try:
        provider = request.json.get('provider')
        files = request.json.get('files', [])
        results = cloud_utils.sync_files(provider, files)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cloud_bp.route('/status')
def cloud_status():
    """Get cloud connection status"""
    return jsonify({
        'google_drive': False,
        'onedrive': False,
        'dropbox': False
    })