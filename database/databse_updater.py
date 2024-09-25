import datetime
import json
import time

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
    total_comments = IntegerField()

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


wallets_dict = {
    'main_branch': main_branch_address,
    'english_branch': english_branch_address,
    'spanish_branch': spanish_branch_address,
    'russian_branch': russian_branch_address
}

# wallets_list = list(wallets_dict.keys())
# print(wallets_dict)

def get_messages_from_API(any_wallet: str, list_of_posts = []):
    url = f"https://tonapi.io/v2/blockchain/accounts/{any_wallet}/transactions"
    # url = 'https://tonapi.io/v2/blockchain/masterchain-head'
    headers = {
        'Authorization': f'Bearer {api_tonconsole}'
    }
    # response = requests.get(url, headers=headers)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
    else:

        post_num = 0

        # Преобразование ответа в словарь
        data = response.json()
        # Получение элемента "transactions" из словаря
        poluchil = data.get('transactions', None)
        # print(poluchil)
        for transaction in poluchil[::-1]:
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
                    # formatted_data = json.dumps(post_dict, indent=4, ensure_ascii=False)
                    # Вывод на экран
                    # print(formatted_data)
                    list_of_posts.append(post_dict)
        return list_of_posts



for wallet_name in list(wallets_dict.keys()):
    # print(wallet)
    list_messages = get_messages_from_API(wallets_dict[wallet_name], [])
    time.sleep(2)
    # print(list_messages)
    for message_dict in list_messages:

        # print(wallet_name)

        BaseBranch = create_branch_model(wallet_name)
        # formatted_data = json.dumps(message_dict, indent=4, ensure_ascii=False)
        # Вывод на экран
        # print(formatted_data)
        # Проверяем, существует ли запись с указанными условиями
        # print(f'проверяю {message_dict["transfer_hash"]}')
        existing_record = BaseBranch.get_or_none(
            BaseBranch.transfer_hash == message_dict["transfer_hash"]
        )

        # Если запись не существует, создаем новую
        if existing_record is None:
            # print()
            BaseBranch.create(
                post_num=message_dict["post_num"],
                amount_sent=message_dict.get("amount_sent"),  # Используем значение из словаря или дефолтное
                text_message=message_dict.get("text_message", ""),
                timestamp=message_dict.get("timestamp"),
                sender_wallet=message_dict["sender_wallet"],
                transfer_hash=message_dict["transfer_hash"],
                sender_name=message_dict.get("sender_name")  or "UnknownSender",  # Значение по умолчанию, если не указано
                black_list_message=message_dict.get("black_list_message")   or False,  # Значение по умолчанию
                total_comments = 0
            )
            # print("Запись добавлена в базу данных.")
        else:
            pass
            # print("Запись уже существует.")