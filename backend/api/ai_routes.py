from flask import Blueprint, request, jsonify
from .ai_processor import AIProcessor

ai_bp = Blueprint('ai', __name__)
ai_processor = AIProcessor()

@ai_bp.route('/suggestions')
def get_suggestions():
    """Get AI-powered file suggestions"""
    try:
        suggestions = ai_processor.analyze_files()
        return jsonify({
            'suggestions': suggestions,
            'confidence': 0.92,
            'total_size': sum(s.get('size', 0) for s in suggestions)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_bp.route('/analyze-image', methods=['POST'])
def analyze_image():
    """Analyze image quality"""
    try:
        file_path = request.json.get('path')
        analysis = ai_processor.analyze_image_quality(file_path)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_bp.route('/detect-duplicates', methods=['POST'])
def detect_duplicates():
    """AI-powered duplicate detection"""
    try:
        file_paths = request.json.get('files', [])
        duplicates = ai_processor.detect_duplicates(file_paths)
        return jsonify({
            'duplicates': duplicates,
            'method': 'perceptual_hash'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500