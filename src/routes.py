from flask import Blueprint, jsonify, request
from src.wp_manager import WPManager
from src.llm_bridge import LLMBridge

wp_bp = Blueprint('wp', __name__, url_prefix='/wp')

manager = WPManager()
llm = LLMBridge()

@wp_bp.route('/sites', methods=['GET'])
def list_sites():
    return jsonify({'sites': manager.list_sites()})

@wp_bp.route('/operator/run', methods=['POST'])
def run_task():
    payload = request.get_json(force=True) or {}
    task = payload.get('task', '')
    site = payload.get('site')
    if not task:
        return jsonify({'error': 'task required'}), 400
    return jsonify(llm.execute_task(task, site_name=site))

@wp_bp.route('/status', methods=['GET'])
def site_status():
    site = request.args.get('site')
    if not site:
        return jsonify({'error': 'site required'}), 400
    return jsonify(manager.get_site_status(site))

@wp_bp.route('/ai/chat', methods=['POST'])
def ai_chat():
    payload = request.get_json(force=True) or {}
    message = payload.get('message')
    if not message:
        return jsonify({'error': 'message required'}), 400
    return jsonify(llm.chat(message, payload.get('site')))


def register_routes(app):
    app.register_blueprint(wp_bp)
