# Функция для проверки API-ключа
from flask import abort, request
from config_data.config import api_key_get_post, api_key_get_walet, api_key_get_comment, api_key_send_form



api_keys_dict = {
    'add_comment': api_key_send_form,
    'get_post_for_comment': api_key_get_comment,
    'get_wallets': api_key_get_walet,
    'get_posts': api_key_get_post
}

def check_api_key(function_name, api_key):
    try_key = api_keys_dict[f'{function_name}']
    if api_key != try_key:
        return False

