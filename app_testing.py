from flask import Flask, request, jsonify
from flask_cors import CORS
from database.branch_info_iteraction import get_branches_list, get_posts_from_branch
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Flask server is running!"




# @app.route('/get_posts', methods=['POST'])
# def get_posts():
#     # Получаем id_нужной_ветки из JSON-данных запроса
#     branch_id = request.json.get('branch')
#     limit = int(request.json.get('limit', 20))
#     offset = int(request.json.get('offset', 0))
#     branches_list = get_branches_list()
#
#     # Проверяем, существует ли такая ветка
#     if branch_id in branches_list:
#         # Возвращаем список постов для данной ветки
#         posts_for_print = get_posts_from_branch(branch_id, limit=limit)
#         return jsonify(posts_for_print)
#     else:
#         # Если ветка не найдена, возвращаем пустой список с кодом 404
#         return jsonify([]), 404
#
#
#     # Предположим, что у вас есть функция для получения постов
#     posts = fetch_posts(limit=limit, offset=offset)
#     return jsonify(posts)
# ============================
# @app.route('/get_posts', methods=['POST'])
# def get_posts():
#     branch_id = request.json.get('branch')
#     last_id = request.json.get('last_id')  # Последний ID для пагинации
#     limit = int(request.json.get('limit', 20))  # Количество постов для получения
#
#     branches_list = get_branches_list()
#
#     if branch_id in branches_list:
#         posts_for_print = get_posts_from_branch(branch_id, last_id, limit)
#         return jsonify(posts_for_print)
#     else:
#         return jsonify([]), 404
# ============================

@app.route('/get_posts', methods=['POST'])
def get_posts():
    print(request.json)
    branch_id = request.json.get('branch')
    last_post_id = request.json.get('last_id')
    limit = 20

    branches_list = get_branches_list()

    if branch_id in branches_list:
        posts_for_print = get_posts_from_branch(branch_id, last_post_id, limit)
        return jsonify(posts_for_print)
    else:
        return jsonify([]), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25400)
