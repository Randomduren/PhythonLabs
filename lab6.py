import sqlite3

def myfunc(dbname, list):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS Users(
         id INTEGER PRIMARY KEY,
         username TEXT NOT NULL,
         email TEXT NOT NULL,
         age INTEGER
         )
         ''')
    for i in list:
        username = i[0]
        email = i[1]
        age = i[2]
        cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
                       (username, email, age))
        connection.commit()
    for value in cursor.execute("SELECT * FROM users"):
        print(value)




database = str(input('Введите название базы данных: '))
list1 = ['randomduren', 'safonoxmax@mail.ru', 19]
list2 = ['kiselmalin', 'simonovoleg@mail.ru', 20]
mylist = [list1, list2]
myfunc(database, mylist)