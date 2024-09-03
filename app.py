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



@app.route('/get_list', methods=['GET'])
def api_interact():
    # otvet = get_posts(0)
    otvet = [{'message_text': 'Третий видимый пост', 'send_date': 1724891810, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 1, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Очередной пост для публикации', 'send_date': 1724727850, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 2, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Это описание видно всем', 'send_date': 1724727802, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 3, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Это вторая запись', 'send_date': 1724725729, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 4, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'First money trasnsfer', 'send_date': 1724722059, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 5, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}]

    return otvet


@app.route('/get_list_filter1', methods=['GET'])
def return_data1():
    otvet = get_posts(1)
    # otvet = [{'message_text': 'Третий видимый пост', 'send_date': 1724891810, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 1, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Очередной пост для публикации', 'send_date': 1724727850, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 2, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Это описание видно всем', 'send_date': 1724727802, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 3, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Это вторая запись', 'send_date': 1724725729, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 4, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}]
    return otvet


@app.route('/get_list_filter10', methods=['GET'])
def return_data10():
    # otvet = get_posts(10)

    otvet = [{'message_text': 'Третий видимый пост', 'send_date': 1724891810, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 1, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Очередной пост для публикации', 'send_date': 1724727850, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 2, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Это описание видно всем', 'send_date': 1724727802, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 3, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}]
    return otvet

@app.route('/get_list_filter100', methods=['GET'])
def return_data100():
    # otvet = get_posts(100)
    otvet = [{'message_text': 'Третий видимый пост', 'send_date': 1724891810, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 1, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}, {'message_text': 'Очередной пост для публикации', 'send_date': 1724727850, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 2, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}]
    return otvet

@app.route('/get_list_filter1000', methods=['GET'])
def return_data1000():
    # otvet = get_posts(1000)
    otvet = [{'message_text': 'Третий видимый пост', 'send_date': 1724891810, 'sender_wallet': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c', 'post_number': 1, 'sender_name': 'Имя если зарегистрировано start (0:97a), fin (a455c)'}]
    return otvet



# Пример данных
posts = {
    "main_branch": [
        {'sender_name': 'Anonym',
         'ton_amount': 0.5,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'первый пост',
         'send_date': 1724891810,
         'post_number': 1,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'vtoroi пост',
         'send_date': 1724891810,
         'post_number': 2,
         },
{'sender_name': 'Anonym',
         'ton_amount': 10,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'tree пост',
         'send_date': 1724891810,
         'post_number': 3,
         }
    ],
    "russian_branch": [
        {'sender_name': 'Anonym',
         'ton_amount': 100,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'four пост',
         'send_date': 1724891810,
         'post_number': 4,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1000,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'five пост',
         'send_date': 1724891810,
         'post_number': 5,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 100,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'первый пост',
         'send_date': 1724891810,
         'post_number': 6,
         }
        ,
        {'sender_name': 'Anonym',
         'ton_amount': 100,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'первый пост',
         'send_date': 1724891810,
         'post_number': 7,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1000,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'five пост',
         'send_date': 1724891810,
         'post_number': 5,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1000,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'five пост',
         'send_date': 1724891810,
         'post_number': 5,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1000,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'five пост',
         'send_date': 1724891810,
         'post_number': 5,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1000,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'five пост',
         'send_date': 1724891810,
         'post_number': 5,
         }
    ],
"english_branch": [
        {'sender_name': 'Anonym',
         'ton_amount': 0.5,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'первый пост english_branch',
         'send_date': 1724891810,
         'post_number': 1,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'english_branch ghfgjhdfhjdf',
         'send_date': 1724891810,
         'post_number': 2,
         },
{'sender_name': 'Anonym',
         'ton_amount': 10,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'tree пост',
         'send_date': 1724891810,
         'post_number': 3,
         }
    ],
"spanish_branch": [
        {'sender_name': 'Anonym',
         'ton_amount': 0.5,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'первый пост spanish_branch',
         'send_date': 1724891810,
         'post_number': 1,
         },
        {'sender_name': 'Anonym',
         'ton_amount': 1,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'vtoroi пост spanish_branch',
         'send_date': 1724891810,
         'post_number': 2,
         },
{'sender_name': 'Anonym',
         'ton_amount': 10,
         'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
         'message_text': 'tree пост',
         'send_date': 1724891810,
         'post_number': 3,
         }
    ]
}


@app.route('/get_posts', methods=['POST'])
def get_posts():
    print(request)
    print(request.json)

    # Получаем id_нужной_ветки из JSON-данных запроса
    branch_id = request.json.get('branch')
    print(branch_id)

    # Проверяем, существует ли такая ветка
    if branch_id in posts:
        # Возвращаем список постов для данной ветки
        return jsonify(posts[branch_id])
    else:
        # Если ветка не найдена, возвращаем пустой список с кодом 404
        return jsonify([]), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25400)
