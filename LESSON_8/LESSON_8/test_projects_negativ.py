import requests

# Настройки
BASE_URL = "https://ru.yougile.com"
TOKEN = (
    "Bearer HtPuI8gEQ75TAX1Atz7Pp3xIZ8I3Nf8kyq8arUMnn12lJIPzW2U3aeaIDQSNGrSj"
    )
USERS = {"0abc98f7-5c87-4694-a33d-567c2a60df6b": "admin"}


def test_create_project():
    payload = {
        "title": "",
        "users": USERS
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": TOKEN
    }
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        headers=headers,
        json=payload
    )
    assert response.status_code == 201, (
        f"Ошибка: HTTP {response.status_code}, ответ: {response.text}"
    )
