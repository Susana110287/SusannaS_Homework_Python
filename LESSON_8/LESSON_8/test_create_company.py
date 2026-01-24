import requests

base_url = "https://ru.yougile.com"


def test_add_new():
    resp = requests.get(base_url+'/company/list')  # Получаем список
    body = resp.json()  # Сохраняем его в переменную
    len_before = len(body)  # Находим длину переменной
