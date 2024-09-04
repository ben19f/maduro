from peewee import SqliteDatabase, Model, AnyField, IntegerField, TextField, FloatField
from config_data.config import database_location


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
    # anylist = ["main_branch", "russian_branch", "english_branch", "spanish_branch"]
    # SQL-запрос для получения списка таблиц
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%_branch';"

    # Выполнение запроса через peewee
    cursor = db.execute_sql(query)
    tables = [row[0] for row in cursor.fetchall()]
    return tables

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
    for transaction in list_for_users:
        if 'amount_sent' in transaction:
            transaction['amount_sent'] = transaction['amount_sent'] / 1000000000
        if 'timestamp' in transaction:
            transaction['timestamp'] = transaction['timestamp'] * 1000

    return list_for_users
