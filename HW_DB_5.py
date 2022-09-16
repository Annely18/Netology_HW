from pprint import pprint
import psycopg2


conn = psycopg2.connect(database="HW_DB", user="postgres", password="AniKa20")
cur = conn.cursor()


# Удаление таблиц:
def delete_tables(cursor, table):
    sql_string = f"DROP TABLE {table};"
    cursor.execute(sql_string)
    conn.commit()
    print(f'Таблица {table} удалена')

# РЕАЛИЗАЦИЯ
delete_tables(cur, 'info')
delete_tables(cur, 'client')


# 1. Функция, создающая структуру БД (таблицы)
def create_client_info_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS client(
            client_id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            surname VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL UNIQUE
            );
        CREATE TABLE IF NOT EXISTS info(
            id SERIAL PRIMARY KEY,
            client_id INTEGER NOT NULL REFERENCES client(client_id),
            phone_number BIGINT CHECK (phone_number >= 81000000000 AND phone_number <= 89999999999) UNIQUE
            );
            """)
    conn.commit()
    print('БД создана')

# РЕАЛИЗАЦИЯ
create_client_info_tables(cur)


# 2. Функция, позволяющая добавить нового клиента
def add_client(cursor, name, surname, email, phone_number=None):
    cursor.execute("""
    INSERT INTO client (name, surname, email) 
    VALUES (%s, %s, %s) 
    RETURNING client_id;
    """, (name, surname, email))
    client_id = cur.fetchone()[0]
    if phone_number is not None:
        cursor.execute("""
        INSERT INTO info (client_id, phone_number)
        VALUES (%s, %s);
        """, (client_id, phone_number))
        conn.commit()
    print(f'Добавлено: {name}, {surname}, id {client_id}')

# РЕАЛИЗАЦИЯ
add_client(cur, 'Георгий', 'Вицин', 'vitsin17@mail.ru', '84955874111')
add_client(cur, 'Юрий', 'Никулин', 'nikulin21@mail.ru')
add_client(cur, 'Евгений', 'Моргунов', 'morgunov27@mail.ru')
add_client(cur, 'Юрий', 'Шатунов', 'sha@mail.ru')


# 3. Функция, позволяющая добавить телефон для существующего клиента ПО ИД
def add_info(cursor, client_id, phone_number):
    cursor.execute("INSERT INTO info (client_id, phone_number) VALUES (%s, %s)", (client_id, phone_number))
    return conn.commit()

# РЕАЛИЗАЦИЯ
add_info(cur, '3', '84957565333')
add_info(cur, '2', '84957485222')
add_info(cur, '2', '84957346222')


# 4. Функция, позволяющая изменить данные о клиенте
def update_client(cursor, client_id, name=None, surname=None, email=None, phone_number=None):
    if name is not None:
        cursor.execute("""
        UPDATE client
        SET name = %s
        WHERE client_id = %s; 
        """, (name, client_id))
    if surname is not None:
        cursor.execute("""
        UPDATE client
        SET surname = %s
        WHERE client_id = %s; 
        """, (surname, client_id))
    if email is not None:
        cursor.execute("""
        UPDATE client
        SET email = %s
        WHERE client_id = %s; 
        """, (email, client_id))
    if phone_number is not None:
        add_info(cursor, client_id, phone_number)
    conn.commit()

# РЕАЛИЗАЦИЯ
# update_client(cur, '1', surname='Vitsin', phone_number='89992154874', name='George')
# update_client(cur, '4', phone_number='89127858444')


# 5. Функция, позволяющая удалить телефон для существующего клиента
def del_info(cursor, client_id, phone_number):
    cursor.execute("""SELECT id FROM info WHERE phone_number = %s AND client_id =%s;""", (phone_number, client_id))
    del_id = cursor.fetchone()
    if del_id is not None:
        cursor.execute("DELETE FROM info WHERE id = %s;", (del_id,))
        conn.commit()
    else:
        print('Ошибка')

# РЕАЛИЗАЦИЯ
# del_info(cur, '1', '84950000000')
# del_info(cur, '2', '84957346222')


# 6.1. Функция, позволяющая удалить существующего клиента ПО ИМЕНИ
def del_client(cursor, name, surname, email):
    cursor.execute("SELECT client_id FROM client WHERE name =%s AND surname =%s AND email = %s;", (name, surname, email))
    client_id = cursor.fetchone()
    if client_id is not None:
        cursor.execute("DELETE FROM info WHERE client_id = %s;", (client_id,))
        cursor.execute("DELETE FROM client WHERE client_id = %s;", (client_id,))
        conn.commit()
    else:
        print('Ошибка')

# РЕАЛИЗАЦИЯ
# del_client(cur, 'Юрий', 'Вицин', 'nikulin21@mail.ru')
# del_client(cur, 'Юрий', 'Никулин', 'nikulin21@mail.ru')


# 6.2. Функция, позволяющая удалить существующего клиента ПО ИД
def del_client_id(cursor, client_id):
    cursor.execute("""
    DELETE FROM info WHERE client_id = %s;
    DELETE FROM client WHERE client_id = %s;
    """, (client_id, client_id))
    conn.commit()

# РЕАЛИЗАЦИЯ
# del_client_id(cur, '2')


# 7. Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
# частичное совпадение:
def find_client_1(cursor, name=None, surname=None, email=None, phone_number=None):
    if name is not None or surname is not None or email is not None or phone_number is not None:
        cursor.execute("""SELECT client_id, name, surname, email, phone_number
        FROM client
        LEFT JOIN info USING(client_id)
        WHERE name = %s OR surname = %s OR email = %s OR phone_number = %s;
        """, (name, surname, email, phone_number))
        pprint(cur.fetchall())

# РЕАЛИЗАЦИЯ
find_client_1(cur, name='Евгений', surname='Вицин')


# полное совпадение:
def find_client(cursor, name=None, surname=None, email=None, phone_number=None):
    if name is not None:
        if surname is not None:
            if email is not None:
                cursor.execute("""SELECT client_id, name, surname, email, phone_number
                FROM client
                LEFT JOIN info USING(client_id)
                WHERE name = %s AND surname = %s AND email = %s;
                """, (name, surname, email))
                pprint(cur.fetchall())
            else:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s AND surname = %s AND client_id = %s;
                    """, (name, surname, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s AND surname = %s;
                    """, (name, surname))
                    pprint(cur.fetchall())
        else:
            if email is not None:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s AND email = %s AND client_id = %s ;
                    """, (name, email, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s AND email = %s ;
                    """, (name, email))
                    pprint(cur.fetchall())
            else:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s AND client_id = %s ;
                    """, (name, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE name = %s;
                    """, (name, ))
                    pprint(cur.fetchall())
    else:
        if surname is not None:
            if email is not None:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE surname = %s AND email = %s AND client_id = %s;
                    """, (surname, email, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE surname = %s AND email = %s;
                    """, (surname, email))
                    pprint(cur.fetchall())
            else:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE surname = %s AND client_id = %s;
                    """, (surname, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE surname = %s;
                    """, (surname, ))
                    pprint(cur.fetchall())
        else:
            if email is not None:
                if phone_number is not None:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE email = %s AND client_id = %s ;
                    """, (email, client_id))
                    pprint(cur.fetchall())
                else:
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE email = %s ;
                    """, (email,))
                    pprint(cur.fetchall())
            else:
                if phone_number is None:
                    print('Пустой запрос')
                else:
                    cursor.execute("SELECT client_id FROM info WHERE phone_number = %s;", (phone_number,))
                    client_id = cur.fetchone()
                    cursor.execute("""SELECT client_id, name, surname, email, phone_number
                    FROM client
                    LEFT JOIN info USING(client_id)
                    WHERE client_id = %s;
                    """, (client_id,))
                    pprint(cur.fetchall())

# РЕАЛИЗАЦИЯ
#find_client(cur, surname='Моргунов', phone_number='84957565333')
#find_client(cur, surname='Шатунов')
#find_client(cur, name='Георгий', email='nikulin21@mail.ru')
#find_client(cur, email='nikulin21@mail.ru')
#find_client(cur, phone_number='84957565333', email='morgunov27@mail.ru')
#find_client(cur, name='Юрий', email='nikulin21@mail.ru')
#find_client(cur, name='Юрий')
#find_client(cur)


# Загрузить все
def show_all(cursor):
    cursor.execute("""SELECT client_id, name, surname, email, phone_number
    FROM client
    LEFT JOIN info USING(client_id);""")
    pprint(cur.fetchall())

# show_all(cur)


cur.close()
conn.close()