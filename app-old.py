from flask import Flask, request, jsonify
from flask_cors import CORS
from database.branch_info_iteraction import get_branches_list, get_posts_list
app = Flask(__name__)
CORS(app)






@app.route('/')
def index():
    return "Flask server is running!"




@app.route('/get_posts', methods=['POST'])
def get_posts():
    # Получаем id_нужной_ветки из JSON-данных запроса
    branch_id = request.json.get('branch')

    branches_list = get_branches_list()

    # Проверяем, существует ли такая ветка
    if branch_id in branches_list:
        # Возвращаем список постов для данной ветки
        posts_for_print = get_posts_list(branch_id)
        return jsonify(posts_for_print)
    else:
        # Если ветка не найдена, возвращаем пустой список с кодом 404
        return jsonify([]), 404


    # Предположим, что у вас есть функция для получения постов
    posts = fetch_posts(limit=limit, offset=offset)
    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25400)
