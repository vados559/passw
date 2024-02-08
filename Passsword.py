import inline # библиотека для изменения input
def AdminAbil():
    while True:
        pass
def UserAbil(nick, password, users, path):
    choice = int(input("Функции:\n1.Сменить пароль\n>> "))
    if choice == 1:
        for i in range(3):
            check = input2("Введите старый пароль: ", secret=True)
            if password == check: # подтверждение пароля
                password = input2("Введите новый пароль: ", secret=True)
                users[nick] = password # обновление пароля в словаре
                bd = open(path, 'w+')
                for i in users: # обновление данных в файле
                    bd.write(f"{i} {users[i]}\n")
                print("Пароль успешно сменен!")
                exit(1)         
            else:
                print("Неверный пароль, попробуйте снова.\n")
        print("Превышено число ошибочных вводов пароля.")
        exit(0)


        


path = 'C:/Users/ilyxa/OneDrive/Desktop/passw/users.txt'
bd = open(path, 'r')
lines = bd.readlines()
bd.close()
users = {} # словарь для хранения имен и паролей пользователей

for i in range(len(lines)): # цикл для подгрузки пользователей в программу
    username, password = lines[i].split()
    users[username] = password 
    print(f"Имя: {username}\t Пароль: {users[username]} \n")
nick = input("Имя пользователя: ")
if nick == "admin": # проверка админ ли входит в систему
    for i in range(3):
        input2 = inline.input
        password = input2("Пароль:", secret = True) 
        if password == users[nick]:
            AdminAbil()
        else:
            print("Неверный пароль, попробуйте снова.")
elif nick in users: # поиск пользователя в базе
    for j in range(3):
        input2 = inline.input # изменение input
        password = input2("Пароль:", secret = True) # сокрытие введенных символов за *
        if password == users[nick]: # проверка пароля
            UserAbil(nick, password, users, path)
        else:
            print("Неверный пароль, попробуйте снова.\n")



    
