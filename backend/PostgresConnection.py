import psycopg2 as psycopg2

from backend.data_request_model import User, User_to_UserLogin, UserLogin

db = [item.split('=')[1] for item
      in open('../db/database.env').read().split('\n')]


def add(SQL: str):
    conn = psycopg2.connect(
        host='127.0.0.1',
        port=5432,
        user=db[0],
        password=db[1],
        database=db[2])
    cur = conn.cursor()
    cur.execute(SQL)

    data = cur.fetchall() if SQL.startswith("SELECT") else "done"

    conn.commit()
    conn.close()
    cur.close()
    return data


def select_user(userID: str):
    return add(
        "SELECT login, name, surname, patronymic, email, birthdate, category "
        "FROM users "
        "WHERE login = '{}' "
        "OR email = '{}'"
        .format(userID, userID))


def insert_user(user: User):
    if not check(User_to_UserLogin(user)):
        add("INSERT INTO users (login, password, name, surname, patronymic, email, birthdate, category)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"
            .format(user.login, user.password, user.name
                    , user.surname, user.patronymic, user.email
                    , user.birthdate, user.category))


def check(data: UserLogin):
    response = add('''SELECT login, email, password
                    FROM users 
                    WHERE login = '{}' 
                    OR email = '{}';'''
                   .format(data.login, data.email, data.password))
    return response
