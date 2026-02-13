import os
from dotenv import load_dotenv, find_dotenv

# env_path = './outside/.env'
env_path = '/home/ben/PycharmProjects/madurodocker/outside/.env'

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
api_key_get_post = os.getenv("API_KEY_GET_POST")
api_key_get_comment = os.getenv("API_KEY_GET_COMMENT")
api_key_send_form = os.getenv("API_KEY_SEND_FORM")
api_key_get_walet = os.getenv("API_KEY_GET_WALLETS")
