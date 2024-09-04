import json

from peewee import SqliteDatabase, Model, AnyField, IntegerField, TextField, FloatField
from config_data.config import database_location, api_tonconsole, main_branch_address, english_branch_address, spanish_branch_address, russian_branch_address
import requests

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

my_wallet = 'UQC6sXDfQ8lafiDiwQcW7u0Ec3-vqigVjaWvQO5qO61vXOPc'


def get_messages_from_API(any_wallet: str):


    url = f"https://tonapi.io/v2/blockchain/accounts/{any_wallet}/transactions"
# url = 'https://tonapi.io/v2/blockchain/masterchain-head'
    headers = {
        'Authorization': f'Bearer {api_tonconsole}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

    post_num = 0
    list_of_posts = []
    # Преобразование ответа в словарь
    data = response.json()

    # Получение элемента "transactions" из словаря
    poluchil = data.get('transactions', None)

    # print(poluchil)

    for transaction in poluchil[::-1]:
        # print(transaction)
        #
        # print('предполагаем что он входящий')
        # print('предполагаем что он правильный')
        # if transaction['credit_phase']['credit'] != null_balance:

        if transaction['orig_status'] == "uninit" and transaction['end_status'] == "active":
            pass
        else:

            if 'decoded_body' in transaction['in_msg'] and transaction['in_msg']['value'] != 0:
                post_num += 1
                # print(sender_name)
                post_dict = {
                    'post_num': post_num,
                    # 'sender_name': sending_timestamp,
                    'amount_sent': transaction['in_msg']['value'],
                    'text_message': transaction['in_msg']['decoded_body']['text'],
                    'timestamp': transaction['utime'],

                    'sender_wallet': transaction['in_msg']['source']['address'],
                    'transfer_hash': transaction['hash']

                }
                # Преобразование словаря в строку JSON с отступами
                formatted_data = json.dumps(post_dict, indent=4, ensure_ascii=False)

                # Вывод на экран
                print(formatted_data)
                list_of_posts.append(post_dict)


get_messages_from_API(my_wallet)