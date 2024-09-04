from peewee import SqliteDatabase, Model, AnyField, IntegerField, TextField
from config_data.config import database_location
from datetime import datetime

db = SqliteDatabase(f'{database_location}/maduro_first.db')


class MainBranch(Model):
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
        table_name = 'main_branch'



def get_branches_list():
    anylist = ["main_branch", "russian_branch", "english_branch", "spanish_branch"]
    return anylist



def get_posts_from_branch(branch_id):

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

    return posts[branch_id]