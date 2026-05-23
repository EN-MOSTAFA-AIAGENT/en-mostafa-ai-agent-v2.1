from flask import Flask, jsonify, render_template
from src.routes import register_routes

app = Flask(__name__, template_folder='../templates')
register_routes(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/healthz')
def healthz():
    return jsonify({'status': 'ok', 'version': 'v2.1'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
