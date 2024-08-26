import os
from dotenv import load_dotenv, find_dotenv

env_path = '.env'
# env_path = '/home/ben/Документы/outside/env-museum.env'

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    # load_dotenv()
    load_dotenv(dotenv_path=env_path)

btc_address = os.getenv("BITCOIN_ADDRESS")
# print(btc_address)