from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:123@localhost/postgres"
db = create_engine(db_connection_string)


# Тест на создание нового предмета
def test_insert_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        # Создаем новый предмет
        sql = text(
            "INSERT INTO subject (subject_id, subject_title) " +
            "VALUES (:new_id, :new_title)"
            )
        connection.execute(sql, {'new_id': 16, 'new_title': 'Music'})

        # Проверяем, что предмет действительно добавлен
        sql_check = text(
            "SELECT subject_title FROM subject WHERE subject_id = :new_id"
            )
        result = connection.execute(sql_check, {'new_id': 16}).fetchone()
        assert result is not None, "Предмет не был добавлен в базу данных"
        assert result.subject_title == 'Music', "Предмет не соответствует"

    except Exception as e:
        transaction.rollback()
        print(f"Ошибка в тесте создания предмета: {e}")
        raise
    else:
        # Удаляем созданный предмет (очистка)
        sql_delete = text("DELETE FROM subject WHERE subject_id = :new_id")
        connection.execute(sql_delete, {'new_id': 16})
        transaction.commit()
    finally:
        connection.close()


# Тест на изменение существующего предмета
def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        # Предварительно создаем предмет для изменения
        sql_insert = text(
            "INSERT INTO subject (subject_id, subject_title) " +
            "VALUES (:id, :title)"
            )
        connection.execute(sql_insert, {'id': 17, 'title': 'Art'})

        # Изменяем название предмета
        sql_update = text(
            "UPDATE subject SET subject_title = :new_title " +
            "WHERE subject_id = :id")
        connection.execute(sql_update, {'new_title': 'Technical', 'id': 17})

        # Проверяем, что изменение прошло успешно
        sql_check = text(
            "SELECT subject_title FROM subject " +
            "WHERE subject_id = :id")
        result = connection.execute(sql_check, {'id': 17}).fetchone()
        assert result is not None, "Предмет не найден после обновления"
        assert result.subject_title == 'Technical', "Предмет не был обновлен"

    except Exception as e:
        transaction.rollback()
        print(f"Ошибка в тесте изменения предмета: {e}")
        raise
    else:
        # Удаляем предмет после теста (очистка)
        sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql_delete, {'id': 17})
        transaction.commit()
    finally:
        connection.close()


# Тест на удаление предмета
def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        # Предварительно создаем предмет для удаления
        sql_insert = text(
            "INSERT INTO subject (subject_id, subject_title) " +
            "VALUES (:id, :title)")
        connection.execute(sql_insert, {'id': 18, 'title': 'Archaeology'})

        # Удаляем предмет
        sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql_delete, {'id': 18})

        # Проверяем, что предмет больше не существует
        sql_check = text("SELECT * FROM subject WHERE subject_id = :id")
        result = connection.execute(sql_check, {'id': 18}).fetchone()
        assert result is None, "Предмет не был удален из базы данных"

    except Exception as e:
        transaction.rollback()
        print(f"Ошибка в тесте удаления предмета: {e}")
        raise
    else:
        transaction.commit()
    finally:
        connection.close()
