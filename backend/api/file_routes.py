from flask import Blueprint, request, jsonify
import os
from .file_handler import FileHandler
from .storage_utils import StorageUtils

file_bp = Blueprint('files', __name__)
file_handler = FileHandler()
storage_utils = StorageUtils()

@file_bp.route('/scan')
def scan_files():
    """Scan device for files"""
    try:
        files = file_handler.scan_directory('/mock/storage')
        return jsonify({
            'files': files,
            'count': len(files)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_bp.route('/delete', methods=['POST'])
def delete_files():
    """Delete selected files"""
    try:
        file_paths = request.json.get('files', [])
        results = []
        
        for path in file_paths:
            success = file_handler.delete_file(path)
            results.append({
                'path': path,
                'deleted': success
            })
        
        return jsonify({
            'results': results,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_bp.route('/info/<path:file_path>')
def file_info(file_path):
    """Get file information"""
    try:
        info = file_handler.get_file_info(file_path)
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_bp.route('/duplicates')
def find_duplicates():
    """Find duplicate files"""
    try:
        duplicates = file_handler.find_duplicates()
        return jsonify({
            'duplicates': duplicates,
            'count': len(duplicates)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500