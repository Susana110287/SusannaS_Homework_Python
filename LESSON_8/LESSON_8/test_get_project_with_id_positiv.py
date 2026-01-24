import pytest
import requests

BASE_URL = "https://ru.yougile.com"
TOKEN = (
    "Bearer HtPuI8gEQ75TAX1Atz7Pp3xIZ8I3Nf8kyq8arUMnn12lJIPzW2U3aeaIDQSNGrSj"
    )
USERS = {"0abc98f7-5c87-4694-a33d-567c2a60df6b": "admin"}


@pytest.fixture
def created_project_id():
    """Фикстура: создаёт проект и возвращает его ID"""
    payload = {
        "title": "Автотест_Проект_2026",
        "users": USERS
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': TOKEN
    }
    response = requests.post(
        BASE_URL + "/api-v2/projects",
        headers=headers,
        json=payload
    )
    assert response.status_code == 201
    return response.json()["id"]


def test_get_project_by_id(created_project_id):
    """Тест: получение проекта по ID"""
    headers = {'Authorization': TOKEN}
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{created_project_id}",
        headers=headers
    )
    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )
    project_data = response.json()
    expected_title = "Автотест_Проект_2026"
    actual_title = project_data["title"]
    assert actual_title == expected_title, (
        f"Ожидалось название '{expected_title}', получено '{actual_title}'"
    )
    assert "users" in project_data, "Поле 'users' отсутствует в ответе"
    print(f"""\
Проект успешно получен:
ID={created_project_id}
Название='{project_data['title']}'\
""")
