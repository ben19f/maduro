from peewee import SqliteDatabase, Model, AnyField, IntegerField, TextField
from config_data.config import database_location
from datetime import datetime

db = SqliteDatabase(f'{database_location}/maduro_first.db')


class BaseBranch(Model):
    post_num = IntegerField()
    sender_name = TextField()
    amount_sent = IntegerField()
    text_message = TextField()
    timestamp = IntegerField()
    black_list_message = TextField()
    sender_wallet = TextField()
    transfer_hash = TextField()

    class Meta:
        database = db
        table_name = ''  # Переопределяется в подклассах
        abstract = True  # Указывает, что это абстрактная модель и таблица для нее не будет создаваться

def create_branch_model(wishful_table_name):
    class Branch(BaseBranch):
        class Meta:
            database = db
            table_name = wishful_table_name
    return Branch

# Создаем модели для каждой ветки
# MainBranch = create_branch_model('main_branch')
# RusBranch = create_branch_model('russian_branch')
# EngBranch = create_branch_model('english_branch')
# EspBranch = create_branch_model('spanish_branch')


def get_branches_list():
    anylist = ["main_branch", "russian_branch", "english_branch", "spanish_branch"]
    return anylist



def get_posts_from_branch(branch_id):
    # Пример использования
    start_row = 1  # Первая строка
    end_row = 20  # Двадцатая строка
    # Рассчитываем offset и limit
    offset = start_row - 1  # Начало отсчета с 0
    limit = end_row - start_row + 1  # Количество строк

    DynamicBranchTable = create_branch_model(branch_id)


    query = (DynamicBranchTable
             .select()
             .offset(offset)
             .limit(limit)
             .dicts())  # Преобразует записи в словари
    # Преобразуем результат запроса в список словарей
    list_for_users = list(query)
    list_for_users = list_for_users[::-1]
    return list_for_users

    # elif branch_id == "english_branch":
    #     return [
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 0.5,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'посты из "english_branch" будут тут',
    #          'send_date': 1724891810,
    #          'post_number': 1,
    #          }]
    # elif branch_id == "russian_branch":
    #     return [
    #     {'sender_name': 'Anonym',
    #      'ton_amount': 0.5,
    #      'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #      'message_text': 'посты из "russian_branch" будут тут',
    #      'send_date': 1724891810,
    #      'post_number': 1,
    #      }]
    # elif branch_id == "spanish_branch":
    #     return [
    #     {'sender_name': 'Anonym',
    #      'ton_amount': 0.5,
    #      'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #      'message_text': 'посты из "spanish_branch" будут тут',
    #      'send_date': 1724891810,
    #      'post_number': 1,
    #      }]
    # else:
    #     return [
    #         {'sender_name': 'такой ветки нету',
    #          'ton_amount': 100000001,
    #          'transaction_hash': 'хеш сумма транзакции',
    #          'message_text': 'посты будут тут',
    #          'send_date': 10000000000001,
    #          'post_number': 1000000001,
    #          }]
    #     return posts[branch_id]

    # Пример данных
    # posts = {
    #     "main_branch": [
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 0.5,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'первый пост',
    #          'send_date': 1724891810,
    #          'post_number': 1,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'vtoroi пост',
    #          'send_date': 1724891810,
    #          'post_number': 2,
    #          },
    # {'sender_name': 'Anonym',
    #          'ton_amount': 10,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'tree пост',
    #          'send_date': 1724891810,
    #          'post_number': 3,
    #          }
    #     ],
    #     "russian_branch": [
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 100,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'four пост',
    #          'send_date': 1724891810,
    #          'post_number': 4,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1000,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'five пост',
    #          'send_date': 1724891810,
    #          'post_number': 5,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 100,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'первый пост',
    #          'send_date': 1724891810,
    #          'post_number': 6,
    #          }
    #         ,
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 100,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'первый пост',
    #          'send_date': 1724891810,
    #          'post_number': 7,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1000,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'five пост',
    #          'send_date': 1724891810,
    #          'post_number': 5,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1000,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'five пост',
    #          'send_date': 1724891810,
    #          'post_number': 5,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1000,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'five пост',
    #          'send_date': 1724891810,
    #          'post_number': 5,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1000,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'five пост',
    #          'send_date': 1724891810,
    #          'post_number': 5,
    #          }
    #     ],
    # "english_branch": [
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 0.5,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'первый пост english_branch',
    #          'send_date': 1724891810,
    #          'post_number': 1,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'english_branch ghfgjhdfhjdf',
    #          'send_date': 1724891810,
    #          'post_number': 2,
    #          },
    # {'sender_name': 'Anonym',
    #          'ton_amount': 10,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'tree пост',
    #          'send_date': 1724891810,
    #          'post_number': 3,
    #          }
    #     ],
    # "spanish_branch": [
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 0.5,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'первый пост spanish_branch',
    #          'send_date': 1724891810,
    #          'post_number': 1,
    #          },
    #         {'sender_name': 'Anonym',
    #          'ton_amount': 1,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'vtoroi пост spanish_branch',
    #          'send_date': 1724891810,
    #          'post_number': 2,
    #          },
    # {'sender_name': 'Anonym',
    #          'ton_amount': 10,
    #          'transaction_hash': '0:97ad93444915089e812238ff10abe9066d0b03ea3dba2a8630fb9c9f88aa455c',
    #          'message_text': 'tree пост',
    #          'send_date': 1724891810,
    #          'post_number': 3,
    #          }
    #     ]
    # }
