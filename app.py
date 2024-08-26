from flask import Flask, request, jsonify, render_template_string
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Flask server is running!"


@app.route('/run-script', methods=['POST'])
def run_script():
    script_name = request.json.get('script_name')

    try:
        # Запуск Python скрипта
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        # Создание HTML-кода
        html_content = 'fffff'

        return render_template_string(html_content)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
