from db.conf import connection
from db import queries
from psycopg2.extras import RealDictCursor


def upsert_user(user_id, first_name, last_name):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.UPSERT_USER, (user_id, first_name, last_name))
        connection.commit()
    print(
        'user saved successfully'
    )


def get_link_info(text):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_LINK, (text,))
        link_data = cur.fetchone()
    print('link check is working')
    if link_data:
        return link_data


def upsert_information(text, link):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.UPSERT_INFORMATION, (text, link))
        connection.commit()
    print(
        'link upsert has been successfully'
    )


def upsert_user_link(user_id, info_id):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.UPSERT_USER_LINK, (user_id, info_id))
        connection.commit()
    print('user link has been successfully added')


def get_user_id(chat_id):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_ID, (chat_id,))
        user_id = cur.fetchone()
    print('user id has been get successfully')
    return user_id if user_id else None
