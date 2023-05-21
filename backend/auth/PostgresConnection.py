import psycopg2 as psycopg2

from data_request_model import User, User_to_UserLogin, UserLogin


class PostgreConn:
    def __init__(self, settings):
        self.settings = settings

    def add(self, SQL: str):
        conn = psycopg2.connect(
            host='127.0.0.1',
            port=5432,
            user=self.settings[0],
            password=self.settings[1],
            database=self.settings[2])
        cur = conn.cursor()
        cur.execute(SQL)

        data = cur.fetchall() if SQL.startswith("SELECT") else "done"

        conn.commit()
        conn.close()
        cur.close()
        return data

    def select_user(self, userID: str):
        pdata = self.add(
            "SELECT login, name, surname, patronymic, email, birthdate, categories.category "
            "FROM users JOIN categories ON users.category + 1 = categories.category_id "
            "WHERE login = '{}' "
            "OR email = '{}'"
            .format(userID, userID))[0]
        return {
            'login': pdata[0],
            'name': pdata[1],
            'surname': pdata[2],
            'patronymic': pdata[3],
            'email': pdata[4],
            'birthdate': pdata[5],
            'category': pdata[6],
        }

    def insert_user(self, user: User):
        if not self.check(User_to_UserLogin(user)):
            self.add("INSERT INTO users (login, password, name, surname, patronymic, email, birthdate, category)"
                     "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"
                     .format(user.login, user.password, user.name
                             , user.surname, user.patronymic, user.email
                             , user.birthdate, user.category))
            return 'done'
        else:
            return 'Пользователь с таким логином или почтой уже зарегистрирован!'

    def check(self, data: UserLogin):
        response = self.add('''SELECT login, email, password
                        FROM users 
                        WHERE login = '{}' 
                        OR email = '{}';'''
                            .format(data.login, data.email, data.password))
        return response
