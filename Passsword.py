def AdminAbil():
    while True:
        pass
def UserAbil(nick):
    while True:
        pass

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
        password = input("Пароль:")
        if password == users[0][1]:
            AdminAbil()
        else:
            print("Неверный пароль, попробуйте снова.")
else:
    for i in users:
        if nick == i[0]:
            for i in range(3):
                password = input("Пароль:")
                if password == i[1]:
                    UserAbil()
                else:
                    print("Неверный пароль, попробуйте снова.")


    
