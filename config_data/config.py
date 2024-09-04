import os
from dotenv import load_dotenv, find_dotenv

# env_path = './outside/.env'
env_path = '/home/ben/PycharmProjects/maduro/outside/.env'

if not os.path.exists(env_path):
    exit("Переменные окружения не загружены, т.к. отсутствует файл .env по указанному пути")
else:
    load_dotenv(dotenv_path=env_path)



database_location = os.getenv("DATABASE_LOCATION")
main_branch_address = os.getenv("MAIN_BRANCH")
english_branch_address = os.getenv("ENGLISH_BRANCH")
spanish_branch_address = os.getenv("SPANISH_BRANCH")
russian_branch_address = os.getenv("RUSSIAN_BRANCH")
api_tonconsole = os.getenv("API_TONCONSOLE")