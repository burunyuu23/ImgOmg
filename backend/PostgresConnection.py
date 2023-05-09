import psycopg2 as psycopg2

db = [item.split('=')[1] for item
      in open('../db/database.env').read().split('\n')]


def add(SQL):
    conn = psycopg2.connect(
        host='127.0.0.1',
        port=5432,
        user=db[0],
        password=db[1],
        database=db[2])
    cur = conn.cursor()

    cur.execute(SQL)

    conn.commit()
    conn.close()
    cur.close()
    return 'done'
