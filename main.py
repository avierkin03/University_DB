import sqlite3

# Підключення до бази даних
data_base = sqlite3.connect("university.db")
cursor = data_base.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS courses(
                    course_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    course_name TEXT,
                    instructor TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY (student_id) REFERENCES students (id),
               FOREIGN KEY (course_id) REFERENCES courses (course_id)
               )''')


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    # Додавання нового студента
    if choice == "1":
        name = input("Введіть і'мя студента: ").lower().strip()
        age = int(input("Введіть і'мя студента: "))
        major = input("Введіть і'мя студента: ").lower().strip()
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        data_base.commit()

    # Додавання нового курсу
    elif choice == "2":
        pass

    # Показати список студентів
    elif choice == "3":
        pass

    # Показати список курсів
    elif choice == "4":
        pass

    # Зареєструвати студента на курс
    elif choice == "5":
        pass

    # Показати студентів на конкретному курсі
    elif choice == "6":
        pass
    
    elif choice == "7":
        break
    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")