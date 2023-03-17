# Upsert user
UPSERT_USER = '''
    INSERT INTO "users" (telegram_id, firs_name, last_name) VALUES (%s, %s, %s)
'''

# Upsert information
UPSERT_INFORMATION = '''
    INSERT INTO information (text, link) VALUES (%s, %s) 
'''

# link ni olish
GET_LINK = '''
    SELECT link,id FROM information 
    WHERE text = %s
'''


# user va linkni bog'lash
UPSERT_USER_LINK = '''
    INSERT INTO user_link (user_id, information_id) VALUES (%s, %s)
'''

# information id ni olish
GET_INFORMATION_ID = '''
    SELECT id FROM information
    WHERE text = %s
'''

# user link ga malumot qoshish uchun user id ni olish
GET_USER_ID = '''
    SELECT id FROM users
    WHERE telegram_id = %s
'''

