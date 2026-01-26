from project_YouGile import ProjectYouGile


name = "Моя компания"
users = {"0abc98f7-5c87-4694-a33d-567c2a60df6b": "admin"}


api = ProjectYouGile('https://ru.yougile.com/api-v2/')


def test_create_project():
    # количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # создание проекта
    project_id = api.create_project('Тест создание проекта', users)

    # количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert len_after - len_before == 1
    # удаляем созданный проект
    api.edit_project(project_id, True, 'Del_Project_Test')


def test_get_project_with_id():
    title = 'Тест получение ID проекта'
    result = api.create_project(title, users)
    project_id = result['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project['title'] == title
    assert new_project['users'] == users


def test_edit_project():
    title = 'Тест изменение проекта'

    result = api.create_project(title, users)

    project_id = result['id']

    api.edit_project(project_id, False, 'Изменение названия проекта')

    edited = api.get_project_with_id(project_id)

    assert edited['title'] == 'Изменение названия проекта'
