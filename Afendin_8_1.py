import sqlite3


def LimitTask1(cursor):
     cursor.execute("select * from workers limit 6")
     print(cursor.fetchall())


def LimitTask2(cursor):
     cursor.execute("select * from workers limit 3 offset 1")
     print(cursor.fetchall())


def OrderByTask3(cursor):
     cursor.execute("select * from workers order by salary")
     print(cursor.fetchall())


def OrderByTask4(cursor):
     cursor.execute("select * from workers order by salary desc")
     print(cursor.fetchall())


def OrderByTask5(cursor):
     cursor.execute("select * from (select * from workers limit 5 offset 1) order by age")
     print(cursor.fetchall())


def CountTask1(cursor):
     cursor.execute("select count(*) from workers")
     print(cursor.fetchone()[0])


def LikeTask1(cursor):
     cursor.execute("select * from pages where author like '%ов %'")
     print(cursor.fetchall())


def LikeTask2(cursor):
     cursor.execute("select * from pages where article like '%элемент%'")
     print(cursor.fetchall())


def LikeTask3(cursor):
     cursor.execute("select * from workers where age like '3_'")
     print(cursor.fetchall())


def LikeTask4(cursor):
     cursor.execute("select * from workers where name like '%я'")
     print(cursor.fetchall())


w = [("Ладюша", 18, 400),
     ("Дилярушка", 32, 500),
     ("Лейладжон", 14, 500),
     ("Аделинаджон", 16, 1000),
     ("Элинушка", 19, 500),
     ("Анюша", 15, 1000),
     ("Эльзахон", 17, 2000),
     ("Амалишка", 18, 1700),
     ("Сонюша", 16, 2540),
     ("Каринушка", 16, 1890),
     ("Луизахон", 18, 2570),
     ("Настюша (Шеф)", 14, 1698),
     ("Иделиябону", 19, 2578)]


t = [("Архипов Артем",  "В своей статье рассказывает о машинах."),
     ("Бабаджанов Камолджон",  "Написал статью об инфляции."),
     ("Веткин Даниил",  "Придумал новый химический элемент."),
     ("Коснырев Лев",  "Также писал о машинах."),
     ("Низамов Ильнар",  "Написал статью о том, как разрабатывать элементы дизайна."),
     ("Мубаракшин Булат",  "Написал статью о своей девушке."),
     ("Трифонов Илья",  "Также писал о девушке")]

con = sqlite3.connect("firstDB1.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    salary INTEGER
                )''')
cursor.executemany('INSERT INTO workers (name, age, salary) VALUES (?, ?, ?)', w)

cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author TEXT,
                    article TEXT
                )''')
cursor.executemany('INSERT INTO pages (author, article) VALUES (?, ?)', t)