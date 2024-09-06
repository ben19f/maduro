from flask import Flask, request, jsonify
from flask_cors import CORS
from database.branch_info_iteraction import get_branches_list, get_posts_from_branch
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Flask server is running!"


@app.route('/get_wallets')
def index2():
    return "тут я выдаю оригинальные картинки и адрса кошельков для сравнения"


@app.route('/get_comments')
def index3():
    return "тут я выдаю по порядку комментарии для отображения"

@app.route('/post_reg_user')
def index4():
    return "тут я регаю постера"

@app.route('/post_reg_commrntator')
def index5():
    return "тут я регаю комментатора это как постер но функции ограничены комментами"

@app.route('/activate_user')
def index6():
    return "тут я после ввода секретного кода из почты активирую юзера"


@app.route('/censored')
def index7():
    return "тут я заношу пост в черный список этот запрос можно получить только от админа"

@app.route('/critika_posta')
def index8():
    return "Это жалоба на пост  после нескольких жалоб пост будет уходить в бан или чтото типо того"


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
