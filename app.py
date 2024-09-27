from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from database.branch_info_iteraction import get_branches_list, get_posts_list, get_post_data, get_comments, add_comment
from outside_iteraction.api_cheker import check_api_key
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
    # Извлекаем параметр 'name' из GET-запроса
    branch_id = request.args.get('branchId')  # Второй аргумент - значение по умолчанию, если параметр не передан
    post_num = int(request.args.get('post_num'))
    last_comment = request.args.get('lastCommentId')
    comments_list = get_comments(branch_id, post_num, last_comment)
    # print(comments_list)
    return comments_list

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
    # извлекаем переменные из запроса
    branch_id = request.json.get('branch_id')
    last_post_id = request.json.get('last_post_id')
    amount_from = request.json.get('amount_from')
    amount_from = float(amount_from)
    amount_to = request.json.get('amount_to')
    if amount_to:
        amount_to = float(amount_to)
    date_from = request.json.get('date_from')
    date_to = request.json.get('date_to')
    post_sender = request.json.get('post_sender')
    post_hash = request.json.get('post_hash')
    site_version = request.json.get('site_version')
    user_age = request.json.get('user_age')
    min_post_id = request.json.get('min_post_id')
    max_post_id = request.json.get('max_post_id')
    posts_list = get_posts_list(branch_id=branch_id, last_post_id=last_post_id, post_hash=post_hash,
                                amount_from=amount_from, amount_to=amount_to, site_version=site_version,
                                date_from=date_from, date_to=date_to, post_sender=post_sender, user_age=user_age,
                                min_post_id =min_post_id, max_post_id =max_post_id)
    if posts_list:
        return jsonify(posts_list)
    else:
        return jsonify([]), 404


@app.route('/get_post_for_comment', methods=['GET'])
def get_post():
    # Извлекаем параметр 'name' из GET-запроса
    branch_id = request.args.get('branchId')  # Второй аргумент - значение по умолчанию, если параметр не передан
    post_num = request.args.get('post_num')
    # post_for_print = {
    #     'id': '2',
    #     'post_num': '2',
    #     'sender_name': 'ANONYM',
    #     'amount_sent': '2',
    #     'text_message': 'Этот пост мы сецчас обсудим',
    #     'timestamp': '7777777',
    #     'black_list_message': 'False',
    #     'sender_wallet': '888888888888',
    #     'transfer_hash': '9999999999999999'
    # }
    post_for_print = get_post_data(branch_id, post_num)
    # print(f'получил вводные данные пост{post_num}, ветка{branch_id}')
    return jsonify(post_for_print)


@app.route('/add_comment', methods=['POST'])
def push_comment_to_db():
    # print(request.headers.get('Authorization'))
    if check_api_key('add_comment', request.headers.get('Authorization')) == False:
        abort(401, description="Unauthorized: Invalid API key")
    else:
        # print(request.json)
        branch_id = request.json.get('branch_id')
        # print(branch_id)
        post_num = request.json.get('post_num')
        sender_name = request.json.get('user_name')
        comment_text = request.json.get('comment_text')
        # print(comment_text, '---', sender_name, '---', post_num, '---', branch_id)
        if add_comment(branch_id, post_num, sender_name, comment_text):
            return jsonify({
                "success": True,
                "message": "Комментарий успешно добавлен"
            })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25400)
