import psycopg2
from tabulate import tabulate

conn=psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="12345", 
    port=5432
)
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    phone VARCHAR(255) UNIQUE NOT NULL
)
""")
conn.commit()

def search_by_pattern():
    pattern=input("Введите шаблон для поиска(Часть имени, фамилии или номера):")
    query="""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s
    """
    cur.execute(query, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    results=cur.fetchall()
    if results:
        print(tabulate(results, headers=["ID", "Имя", "Фамилия", "Номер телефона"], tablefmt='fancy_grid'))
    else:
        print("Нет соответствий ")

def insert_or_update_user():
    name=input("Введите имя: ")
    phone=input("Введите номер: ")
    surname=input("Введите фамилию: ")
    cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
    if cur.fetchall():
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (phone, name))
        print("Номер обновлен.")
    else:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
        print("Пользователь введен.")
    conn.commit()

def bulk_insert_users():
    n=int(input("Сколько пользователей вы хотите ввести ?: "))
    invalid=[]
    for _ in range(n):
        name=input("Введите имя: ")
        phone=input("Введите номер: ")
        surname = input("Введите фамилия: ")
        if not phone.isdigit():
            invalid.append((name, surname, phone))
            continue
        cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
        if cur.fetchall():
            cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (phone, name))
        else:
            cur.execute("INSErT INTO phonebook (name, surname, phone) VALUES(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    if invalid:
        print("Недействительные номера телефонов:")
        for entry in invalid:
            print(entry)
    
def paginate_query():
    limit=int(input("Введите лимит: "))
    offset=int(input("Введите пропуск: "))
    cur.execute("SELECT * FROM phonebook ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
    results=cur.fetchall()
    print(tabulate(results, headers=["ID", "Имя", "Фамилия", "Номер телефона"], tablefmt='fancy_grid'))

def delete_by_name_or_phone():
    value=input("Введите имя или номер который хотите удалить: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))
    conn.commit()
    print("Удалено")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows=cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def print_menu():
    print("""
### Меню ###
1. Поиск по шаблону
2. Ввод/обновление данных пользователя
3. Ввод нескольких пользователей
4. Постраничный запрос
5. Удаление по имени или номеру
6. Показать все данные
7. Выход
""")

while True:
    print_menu()
    command=input("Enter command: ").strip().lower()
    
    if command=="1":
        search_by_pattern()
    elif command=="2":
        insert_or_update_user()
    elif command=="3":
        bulk_insert_users()
    elif command=="4":
        paginate_query()
    elif command=="5":
        delete_by_name_or_phone()
    elif command=="6":
        show_all()
    elif command=="7":
        break
    else:
        print("Неизвестная команда.")

cur.close()
conn.close()