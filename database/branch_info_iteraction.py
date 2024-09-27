from datetime import datetime

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
    total_comments = IntegerField()
    last_comment_date = IntegerField()

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


def get_branches_list():
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%_branch';"
    cursor = db.execute_sql(query)
    tables = [row[0] for row in cursor.fetchall()]
    return tables




# def get_post_using_hash(branch_id, post_hash):
#     """получаю из таблицы пост по хешу если он есть"""
#     DynamicBranchTable = create_branch_model(branch_id)
#     query = DynamicBranchTable.select().where(DynamicBranchTable.transfer_hash == post_hash).order_by(DynamicBranchTable.id.desc()).first()
#     if query:
#         return query.__data__


# def check_filters(amount_from=None, amount_to=None,date_from=None, date_to=None)

def get_posts_list(branch_id, last_post_id=None, limit=20, amount_from=None, amount_to=None, date_from=None,
                   date_to=None, post_sender=None, post_hash=None, site_version=None, user_age=None, min_post_id=None,
                   max_post_id=None):

    print(branch_id, last_post_id, limit, amount_from, amount_to, date_from,
                   date_to, post_sender, post_hash, site_version, user_age, min_post_id,
                   max_post_id)
    print(amount_from)
    print(amount_to)

    # Преобразование строки в объект datetime
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    # Преобразование объекта datetime в timestamp (в секундах)
    date_from = int(date_from.timestamp())
    date_to = int(date_to.timestamp())



    DynamicBranchTable = create_branch_model(branch_id)

    # Создаем запрос с фильтрами
    query = DynamicBranchTable.select()

    # Добавляем условия по id
    if min_post_id is not None:
        query = query.where(DynamicBranchTable.id >= min_post_id)

    if max_post_id is not None:
        query = query.where(DynamicBranchTable.id <= max_post_id)

    # Добавляем условия по timestamp
    if date_from is not None:
        query = query.where(DynamicBranchTable.timestamp >= date_from)

    if date_to is not None:
        query = query.where(DynamicBranchTable.timestamp <= date_to)

    # Добавляем условия по сумме
    if amount_from is not None:
        print('amount_from')
        print(amount_from)
        print(type(amount_from))
        # amount_from = amount_from * 1000000000
        print(amount_from)
        query = query.where(DynamicBranchTable.amount_sent >= amount_from * 1000000000)

    if amount_to is not None:
        print('amount_to')
        print(amount_to)
        query = query.where(DynamicBranchTable.amount_sent <= amount_to * 1000000000)

    # Добавляем условие для sender
    if post_sender:
        query = query.where(DynamicBranchTable.sender_wallet == post_sender)

    # Добавляем условие для hash
    if post_hash:
        query = query.where(DynamicBranchTable.transfer_hash == post_hash)



    # Устанавливаем пагинацию

    if last_post_id:
        query = query.where(DynamicBranchTable.id > last_post_id)  # Получаем посты с id больше, чем last_post_id

    query = query.order_by(DynamicBranchTable.id).limit(limit)  # Ограничиваем до limit постов

    # Используем dicts() для получения результата в виде списка словарей
    list_for_users = list(query.dicts())
    for transaction in list_for_users:
        if 'amount_sent' in transaction:
            transaction['amount_sent'] = transaction['amount_sent'] / 1000000000
        if 'timestamp' in transaction:
            transaction['timestamp'] = transaction['timestamp'] * 1000  # Преобразуем timestamp в миллисекунды
        if 'black_list_message' in transaction:
            if transaction['black_list_message'] == 'True':
                transaction[
                    'text_message'] = 'содержание данного поста скрыто по этическим соображениям, либо его текст нарушает законодательство той страны из которой вы его смотрите'
    # print(list_for_users)  # Изменил на вывод всех постов для лучшего понимания
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
        'transfer_hash': record.transfer_hash,
        'total_comments': record.total_comments
    }

        if result['black_list_message'] == 'True':
            result[
                'text_message'] = 'содержание данного поста скрыто по этическим соображениям, либо его текст нарушает законодательство той страны из которой вы его смотрите'

    return result

def get_comments(branch_id, post_num, last_comment_id=None, limit=20):
    # print('function')
    # print(branch_id, post_num, last_comment_id, limit)
    # print(type(branch_id), type(post_num), type(last_comment_id), type(limit))
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
    result_list = []
    for record in comments_list:
        # print(record['timestamp'])
        # print(type(record['timestamp']))
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

    return result_list




def add_comment(branch_id, post_num, sender_name, comment_text, user_id = 0, user_foto = 'poka_net'):
    current_time = int(time.time())
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


    new_comment = CommentsTab.create(
        comment_id=new_comment_id,
        post_num=post_num,
        post_branch=branch_id,
        comment_text=comment_text,
        user_name=sender_name,
        timestamp=current_time,  # Генерируем текущее время в секундах
        user_foto=user_foto,
        user_id=user_id
    )
    # Создаем динамическую модель таблицы
    DynamicBranchTable = create_branch_model(branch_id)


    # Находим строку с нужным post_num
    record = DynamicBranchTable.get(DynamicBranchTable.post_num == post_num)

    # Увеличиваем поле total_comments на 1
    record.total_comments += 1
    print(current_time)
    record.last_comment_date = current_time

    # Сохраняем изменения
    record.save()
    # Возвращаем созданный комментарий (или его ID)
    return True