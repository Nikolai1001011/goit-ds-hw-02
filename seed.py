import sqlite3
from faker import Faker

# Підключення до бази даних
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Створення екземпляра Faker
fake = Faker()

# Заповнення таблиці status
statuses = [('new',), ('in progress',), ('completed',)]
cursor.executemany("INSERT INTO status (name) VALUES (?)", statuses)

# Заповнення таблиці users
users = [(fake.name(), fake.email()) for _ in range(10)]
cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)

# Заповнення таблиці tasks
tasks = [(fake.sentence(), fake.text(), fake.random_int(min=1, max=3), fake.random_int(min=1, max=10)) for _ in range(20)]
cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks)

# Збереження змін
conn.commit()
conn.close()
