import inline # библиотека для изменения input
import re
import os
def AdminAbil(nick, password, users, path): # функции администратора
    while True:
        choice = int(input("Функции:\n1.Сменить пароль\n2.Список пользвоателей\n3.Добавить пользователя\n4.Заблокировать пользователя\n5.Ограничение на выбираемые пароли\n6.Завершить работу\n>> "))
        if choice == 1: # смена пароля
            ChangePassword(nick, password, users, path)
        elif choice == 2: # вывод списка пользователей
            for i in users:
                print(f"Имя: {i}\t Пароль: {users[i][0]}\t Блокировка: {'YES' if users[i][1] == '1' else 'NO'}\t Ограничения на пароль: {'YES' if users[i][2] == '1' else 'NO'} \n")
        elif choice == 3: # добавление нового пользователя
            username = input("Введите имя пользователя: ")
            users[username] = ["0", "0", "0"]
            Refresh_db(path, users) # сохранение изменений
        elif choice == 4: # блокировка пользователя
            for i in  users: # список имен существующих пользователей
                print(i+"\n")
            username = input("Введите имя пользователя: ")
            if username in users:
                users[username][1] =  "1"
                Refresh_db(path, users) # сохранение изменений
                print("Пользователь заблокирван!\n")
            else:
                print("Пользователь с указанным именем не найден!\n")
        elif choice == 5: # установка ограничений на пароль
            for i in  users:
                print(i+"\n")
            username = input("Введите имя пользователя: ")
            if username in users:
                users[username][2] =  "1"
                Refresh_db(path, users) # сохранение изменений
                print("Ограничения установлены!\n")
            else:
                print("Пользователь с указанным именем не найден!\n")
        elif choice == 6: # завершение работы
            exit(1)
   
def UserAbil(nick, password, users, path): # функции польззователя
    choice = int(input("Функции:\n1.Сменить пароль\n>> "))
    if choice == 1:
        ChangePassword(nick, password, users, path)
    exit(1)
        
def ChangePassword(nick, password, users, path): # функция смены пароля
    pattern = "r(?=.*[а-яА-Яa-zA-Z])(?=.*[,.!?])" # регулярное выражение для пароля
    for i in range(3):
        check = input2("Введите старый пароль: ", secret=True)
        if password == check: # подтверждение пароля
            if users[nick][2] == "1": # проверка на ограничение на ввода пароля
                while True: 
                    print("Пароль должен содержать буквы и знаки препинания(, . ! ?).\n")
                    password = input2("Введите новый пароль: ", secret=True)
                    if re.search(pattern, password):
                        break
                    else:
                        print("Пароль не удоволетворяет требованиям.\n1. Завершить работу\n2. Оставить старый пароль\n3. Продолжить\n")
                        choice = int(input(">> "))
                        if choice == 1:
                            exit(1)
                        elif choice == 2:
                            return
            else:
                password = input2("Введите новый пароль: ", secret=True)
            users[nick][0] = password # обновление пароля в словаре
            Refresh_db(path, users) # сохранение изменений
            print("Пароль успешно сменен!")
            return
        else:
            print("Неверный пароль, попробуйте снова.\n")
        print("Превышено число ошибочных вводов пароля.")

def Refresh_db(path, users): #функция для обновления данных в файле
    bd = open(path, 'w+')
    for i in users: # обновление данных в файле
        bd.write(f"{i} {users[i][0]} {users[i][1]} {users[i][2]}\n")
    bd.close()

current_directory = os.path.dirname(__file__) # определение пути к каталогу в котором находится скрипт и текстовый файл
path = os.path.join(current_directory, 'users.txt')
bd = open(path, 'r')
lines = bd.readlines()
bd.close()
users = {} # словарь для хранения имен и паролей пользователей
for i in range(len(lines)): # цикл для подгрузки пользователей в программу
    username, password, block, limit = lines[i].split()
    users[username] = [password, block, limit] 
    print(f"Имя: {username}\t Пароль: {users[username][0]}\t Блокировка: {'YES' if users[username][1] == '1' else 'NO'}\t Ограничения на пароль: {'YES' if users[username][2] == '1' else 'NO'} \n")
nick = input("Имя пользователя: ")
if nick == "admin": # проверка админ ли входит в систему
    for i in range(3):
        input2 = inline.input
        password = input2("Пароль:", secret = True) 
        if password == users[nick][0]:
            AdminAbil(nick, password, users, path)
        else:
            print("Неверный пароль, попробуйте снова.")
elif nick in users: # поиск пользователя в базе
    if users[nick][1] == "1":
        print("Вы были забанены пожизненно)")
        exit(0)
    for j in range(3):
        input2 = inline.input # изменение input
        password = input2("Пароль:", secret = True) # сокрытие введенных символов за *
        if password == users[nick][0]: # проверка пароля
            UserAbil(nick, password, users, path)
        else:
            print("Неверный пароль, попробуйте снова.\n")



    
