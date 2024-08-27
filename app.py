from flask import Flask, request, jsonify, render_template_string
import subprocess
from flask_cors import CORS
from tonconsole import get_posts
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


@app.route('/get_list', methods=['GET'])
def api_interact():
    otvet = get_posts()
    html_content = f"""
            <html>
                <head><title>Script Output</title></head>
                <body>
                    <div style="background-color: red; color: white; padding: 20px;">
                    <h1>Пост №1:</h1>
                    <h2>Отправитель:</h2>
                    <pre>{otvet[0]['post_source']}</pre>
                    <h2>Дата:</h2>
                    <pre>{otvet[0]['post_timestamp']}</pre>
                    <h2>Текст:</h2>
                    <pre>{otvet[0]['post_text']}</pre>
                    </div>
                    <div style="background-color: green; color: white; padding: 20px;">
                    <h1>Пост №2:</h1>
                    <h2>Отправитель:</h2>
                    <pre>{otvet[1]['post_source']}</pre>
                    <h2>Дата:</h2>
                    <pre>{otvet[1]['post_timestamp']}</pre>
                    <h2>Текст:</h2>
                    <pre>{otvet[1]['post_text']}</pre>
                    </div>
                    
                    
                </body>
            </html>
            """

    print(otvet)
    return html_content



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
