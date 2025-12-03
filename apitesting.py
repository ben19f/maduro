import requests

# URL из константы url
url = 'http://127.0.0.1:25400/get_posts'

# Данные из объекта data
data = {
    "branch_id": "main_branch",
    "last_post_id": None,
    "date_from": "2024-08-29",
    "date_to": "2025-12-04",
    "amount_from": "0.000000001",
    "amount_to": None,
    "post_sender": "",
    "min_post_id": "1",
    "max_post_id": None,
    "post_hash": None,
    "site_version": "0"
}

# Заголовки (аналогично headers в fetch)
headers = {
    "Content-Type": "application/json"
}

try:
    # Отправка POST‑запроса
    response = requests.post(url, json=data, headers=headers)

    # Проверка статуса ответа
    if response.status_code != 200:
        raise Exception(f"HTTP error! Status: {response.status_code}")

    # Парсинг JSON‑ответа
    result = response.json()
    print("Ответ API:", result)

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)
except Exception as e:
    print("Ошибка:", e)