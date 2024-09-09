from peewee import SqliteDatabase, Model, AnyField, IntegerField, TextField, FloatField, fn
from config_data.config import database_location
import time

db = SqliteDatabase(f'{database_location}/maduro_first.db')


class CommentsTab(Model):
    comment_id = IntegerField()
    post_num = IntegerField()
    post_branch = TextField()
    comment_text = TextField()
    user_name = TextField()
    timestamp = IntegerField()
    user_foto = TextField()
    user_id = IntegerField()

    class Meta:
        database = db
        table_name = 'comments_1'



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
    # anylist = ["main_branch", "russian_branch", "english_branch", "spanish_branch"]
    # SQL-запрос для получения списка таблиц
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%_branch';"

    # Выполнение запроса через peewee
    cursor = db.execute_sql(query)
    tables = [row[0] for row in cursor.fetchall()]
    return tables


# def get_posts_from_branch(branch_id, limit=20):
#     DynamicBranchTable = create_branch_model(branch_id)
#
#     # Получаем все записи в порядке убывания ID
#     query = (DynamicBranchTable
#              .select()
#              .order_by(DynamicBranchTable.id.desc())  # Сортировка по убыванию ID
#              .limit(limit)
#              .dicts())  # Преобразует записи в словари
#
#     # Преобразуем результат запроса в список словарей и переворачиваем его
#     list_for_users = list(query)
#     list_for_users = list_for_users[::-1]  # Переворачиваем список для получения последних записей в исходном порядке
#
#     for transaction in list_for_users:
#         if 'amount_sent' in transaction:
#             transaction['amount_sent'] = transaction['amount_sent'] / 1000000000
#         if 'timestamp' in transaction:
#             transaction['timestamp'] = transaction['timestamp'] * 1000
#
#     list_for_users= list_for_users[::-1]
#     return list_for_users

# 0000000000000000000000000000000000
def get_posts_from_branch(branch_id, last_post_id=None, limit=20):
    DynamicBranchTable = create_branch_model(branch_id)

    query = DynamicBranchTable.select().order_by(DynamicBranchTable.id.desc())  # Сортировка по ID

    if last_post_id:
        last_post_id = int(last_post_id)
        query = query.where(DynamicBranchTable.id < last_post_id)

    query = query.limit(limit).dicts()

    list_for_users = list(query)

    for transaction in list_for_users:
        if 'amount_sent' in transaction:
            transaction['amount_sent'] = transaction['amount_sent'] / 1000000000
        if 'timestamp' in transaction:
            transaction['timestamp'] = transaction['timestamp'] * 1000  # Преобразуем timestamp в миллисекунды

    return list_for_users



def get_post_data(branch_id, post_num):
    DynamicBranchTable = create_branch_model(branch_id)
    # Выполняем запрос к БД с фильтрацией по post_num
    query = DynamicBranchTable.select().where(DynamicBranchTable.post_num == post_num)

    for record in query:
        amount = record.amount_sent / 1000000000
        timestamp = record.timestamp * 1000
        result = {
        'id': record.id,
        'post_num': record.post_num,
        'sender_name': record.sender_name,
        'amount_sent': amount,
        'text_message': record.text_message,
        'timestamp': timestamp,
        'black_list_message': record.black_list_message,
        'sender_wallet': record.sender_wallet,
        'transfer_hash': record.transfer_hash
    }
    return result

def get_comments(branch_id, post_num, last_comment_id=None, limit=20):
    print('function')
    print(branch_id, post_num, last_comment_id, limit)
    print(type(branch_id), type(post_num), type(last_comment_id), type(limit))
    # Запрос для получения последних комментариев по post_num и branch_id
    query = CommentsTab.select().where(
        (CommentsTab.post_num == post_num) &
        (CommentsTab.post_branch == branch_id)
    ).order_by(CommentsTab.comment_id.desc())  # Сортировка по убыванию comment_id

    # Если передан last_comment_id, фильтруем запрос, чтобы получить комментарии с меньшим ID
    if last_comment_id:
        last_comment_id = int(last_comment_id)
        query = query.where(CommentsTab.comment_id < last_comment_id)

    # Ограничиваем количество комментариев
    query = query.limit(limit).dicts()

    # Преобразуем результат в список словарей
    comments_list = list(query)

    # # Преобразуем timestamp (если это нужно) в миллисекунды
    # for comment in comments_list:
    #     if 'timestamp' in comment:
    #         comment['timestamp'] = comment['timestamp'] * 1000  # Преобразуем timestamp в миллисекунды

    result_list = []
    for record in comments_list:
        print(record['timestamp'])
        print(type(record['timestamp']))
        timestamp = int(record['timestamp']) * 1000

        result = {
        'comment_id': record['comment_id'],
        'post_id': record['post_num'],
        'post_branch': record['post_branch'],
        'comment_text': record['comment_text'],
        'user_name': record['user_name'],
        'timestamp': timestamp,
        'user_foto': record['user_foto'],
        'user_id': record['user_id'],
        }
        result_list.append(result)
    # print(result_list)
    return result_list


# get_comments('english_branch', 1, last_comment_id=None, limit=20)


def add_comment(branch_id, post_num, sender_name, comment_text, user_id = 0, user_foto = 'poka_net'):
    # Находим максимальный comment_id для указанного post_num и branch_id
    max_comment_id = CommentsTab.select(fn.MAX(CommentsTab.comment_id)).where(
        (CommentsTab.post_num == post_num) &
        (CommentsTab.post_branch == branch_id)
    ).scalar()

    # Если таких комментариев нет, начинаем с 1
    if max_comment_id is None:
        new_comment_id = 1
    else:
        new_comment_id = max_comment_id + 1

    # print(branch_id)
    # Добавляем новый комментарий в таблицу
    new_comment = CommentsTab.create(
        comment_id=new_comment_id,
        post_num=post_num,
        post_branch=branch_id,
        comment_text=comment_text,
        user_name=sender_name,
        timestamp=int(time.time()),  # Генерируем текущее время в секундах
        user_foto=user_foto,
        user_id=user_id
    )

    # Возвращаем созданный комментарий (или его ID)
    return True