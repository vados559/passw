import inline # библиотека для изменения input
def AdminAbil():
    while True:
        pass
def UserAbil(nick, password):
    choice = input("Функции:\n1.Сменить пароль\n>>")
    if choice == 1:
        for i in range(3):
            check = input2("Введите старый пароль: ")
            if password == check:
                pass # НАПИСАТЬ ЗАМЕНУ ПАРОЛЯ ПОЛЬЗОВАТЕЛЯ В ФАЙЛЕ
            else:
                print("Неверный пароль, попробуйте снова.\n")


        


path = 'C:/Users/ilyxa/OneDrive/Desktop/passw/users.txt'
bd = open(path, 'r')
lines = bd.readlines()
users = [ [0, 0] for _ in range(len(lines))] # матрица для хранения имен и паролей пользователей

for i in range(len(lines)): # цикл для подгрузки пользователей в программу
    users[i][0], users[i][1] = lines[i].split() 
    print(f"Имя: {users[i][0]}\t Пароль: {users[i][1]} \n")
nick = input("Имя пользователя: ")
if nick == users[0][0]:
    for i in range(3):
        input2 = inline.input
        password = input2("Пароль:", secret = True) 
        if password == users[0][1]:
            AdminAbil()
        else:
            print("Неверный пароль, попробуйте снова.")
else:
    for i in users:
        if nick == i[0]:
            for j in range(3):
                input2 = inline.input
                password = input2("Пароль:", secret = True)
                if password == i[1]:
                    UserAbil(nick, password)
                else:
                    print("Неверный пароль, попробуйте снова.\n")



    
