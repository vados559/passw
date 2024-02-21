import re # для регулярных выражений
import os # для динамического определения пути к файлу
from tkinter import * # для создания главного окна
from tkinter import ttk # для виджетов (кнопок, полей и т.д.)
from tkinter.messagebox import showerror # для показа окна с ошибкой

WrongPassA = 0 # Число неверых вводов пароля админа
WrongPassU = 0 # Число неверых вводов пароля пользователя

def encryption(users): # шифрование паролей шифром цезаря
    key = 3
    for i in users:
        EncPass = ""
        for j in list(users[i][0]):
            EncPass += chr(ord(j) + key)
        users[i][0] = EncPass
    return users

def decode(users): # дешефровка паролей
    key = 3
    for i in users:
        EncPass = ""
        for j in list(users[i][0]):
            EncPass += chr(ord(j) - key)
        users[i][0] = EncPass
    return users

def AdminAbil(nick, password, users, path): # функции администратора
    WindowAdmin = Tk()
    WindowAdmin.title("Здравствуйте, Администартор")
    WindowAdmin.geometry("1500x800")
    root.destroy()
    ttk.Label(WindowAdmin, text="Здравствуйте, Администартор", font=("Arial", 14)).pack(anchor=CENTER)

    ttk.Button(WindowAdmin, text="Сменить пароль", command= lambda: ChangePasswordWindow(nick, password, users, path)).pack(anchor=CENTER, pady=10)
    
    ttk.Button(WindowAdmin, text="Cписок пользовтелей", command= lambda: ListUsers(users)).pack(anchor=CENTER, pady=10)
    
    ttk.Button(WindowAdmin, text="Добавление пользователя", command= lambda: AddUser(path, users)).pack(anchor=CENTER, pady=10)

    ttk.Button(WindowAdmin, text="Заблокировать пользователя", command= lambda: BlockUser(path, users)).pack(anchor=CENTER, pady=10)

    ttk.Button(WindowAdmin, text="Ограничить пароль пользователя", command= lambda: LimitUser(path, users)).pack(anchor=CENTER, pady=10)
        
    ttk.Button(WindowAdmin, text="Завершить работу", command= lambda: Logout(WindowAdmin)).pack(anchor=CENTER, pady=10)

def Logout(window): # Выход из системы
    window.destroy()

def LimitUser(path, users):
    WindowBU = Tk()
    WindowBU.title("Ограничение пользователя")
    WindowBU.geometry("470x700")
    ttk.Label(WindowBU, text="Имя пользователя").pack(pady=2)
    username = ttk.Entry(WindowBU)
    username.pack()
    ttk.Button(text="Ограничить пароль пользователя", command = lambda: LimCheckUser(path, users, username.get(), WindowBU)).pack(pady=2) # сохранение изменений

def LimCheckUser(path, users, username, window):
    if username in users:
        users[username][2] = "1"
        Refresh_db(path, users) # сохранение изменений
        window.destroy()
    else:
        showerror(title="Ошибка", message="Пользователя с таким именем не существует")

def BlockUser(path, users): # функция оболочка для блокировки пользователя
    WindowBU = Tk()
    WindowBU.title("Блокировка пользователя")
    WindowBU.geometry("470x700")
    ttk.Label(WindowBU, text="Имя пользователя").pack(pady=2)
    username = ttk.Entry(WindowBU)
    username.pack()
    ttk.Button(text="Заблокировать пользователя", command = lambda: CheckUser(path, users, username.get(), WindowBU)).pack(pady=2) # сохранение изменений

def CheckUser(path, users, username, window): # проверка на наличие пользователя в базе и блокировка
    if username in users:
        users[username][1] = "1"
        Refresh_db(path, users) # сохранение изменений
        window.destroy() # закрытие окна
    else:
        showerror(title="Ошибка", message="Пользователя с таким именем не существует")

def ListUsers(users): # функция для вывода списка пользователей
    WindowLU = Tk()
    WindowLU.title("Список пользователей")
    WindowLU.geometry("470x700")
    ttk.Label(WindowLU, text=[f"Имя: {i}\t Пароль: {users[i][0]}\t Блокировка: {'YES' if users[i][1] == '1' else 'NO'}\t Ограничения на пароль: {'YES' if users[i][2] == '1' else 'NO'} \n" for i in users]).pack()

def AddUser(path, users): # функция оболочка для добавления пользователей
    WindowAU = Tk()
    WindowAU.title("Добавление пользователя")
    WindowAU.geometry("470x500")
    ttk.Label(WindowAU, text="Имя нового пользователя").pack()
    username = ttk.Entry(WindowAU)
    username.pack()
    ttk.Button(WindowAU, text="Добавить пользователя", command = lambda: add_destroy(path, users, WindowAU, username.get())).pack(anchor=CENTER) # сохранение изменений

def add_destroy(path, users, window, username): # функция для добавления новго пользователя
    users[username] = ["0", "0", "0"]
    Refresh_db(path, users)
    window.destroy()

def UserAbil(nick, password, users, path): # функции польззователя
    WindowUser = Tk()
    WindowUser.title(f"Здравствуйте, {nick}")
    WindowUser.geometry("1500x800")
    root.destroy()
    ttk.Label(WindowUser, text=f"Здравствуйте, {nick}", font=("Arial", 14)).pack(anchor=CENTER)

    ChangePasswordButton = ttk.Button(WindowUser, text="Сменить пароль", command= lambda: ChangePasswordWindow(nick, password, users, path))
    ChangePasswordButton.pack(anchor=CENTER, pady=10)

    ttk.Button(WindowUser, text="Завершить работу", command= lambda: Logout(WindowUser)).pack(anchor=CENTER, pady=10)
        
def ChangePasswordWindow(nick, password, users, path): # функция оболочка смены пароля
    WindowCP = Tk()
    WindowCP.title("Смена пароля")
    WindowCP.geometry("450x700")
    ttk.Label(WindowCP, text="Cтарый пароль").pack(anchor=CENTER)
    check = ttk.Entry(WindowCP)
    check.pack(anchor=CENTER)
    ttk.Label(WindowCP, text="Новый пароль").pack(anchor=CENTER)
    password_entry = ttk.Entry(WindowCP) 
    password_entry.pack(padx=5, pady=5, anchor=CENTER)
    ttk.Button(WindowCP, text="сменить пароль", command = lambda: ChangePassword(nick, password, check.get(), users, path, password_entry.get(), WindowCP)).pack()
    
def ChangePassword(nick, password, check, users, path, password_new, Window): # функция для смены пароля
    pattern = "r(?=.*[а-яА-Яa-zA-Z])(?=.*[,.!?])" # регулярное выражение для пароля
    if password == check: # подтверждение пароля
        if users[nick][2] == "1": # проверка на ограничение на ввода пароля 
            if not re.search(pattern, password_new):
                showerror(title="Ошибка", message="Пароль должен содержать буквы и знаки препинания(, . ! ?).\n")
            else:
                users[nick][0] = password_new # обновление пароля в словаре
        else:
            users[nick][0] = password_new # обновление пароля в словаре
        Refresh_db(path, users) # сохранение изменений
        Window.destroy()
    else:
        showerror(title="Ошибка", message="Пароль неверный")

def Refresh_db(path, users): #функция для обновления данных в файле
    bd = open(path, 'w+')
    users = encryption(users) # шифрование паролей
    for i in users: # обновление данных в файле
        bd.write(f"{i} {users[i][0]} {users[i][1]} {users[i][2]}\n")
    bd.close()

def entry():
    current_directory = os.path.dirname(__file__) # определение пути к каталогу в котором находится скрипт и текстовый файл
    path = os.path.join(current_directory, 'users.txt')
    bd = open(path, 'r')
    lines = bd.readlines() #занесение данных из файла в программу
    bd.close()

    users = {} # словарь для хранения имен и паролей пользователей
    for i in range(len(lines)): # цикл для подгрузки пользователей в программу
        username, password, block, limit = lines[i].split()
        users[username] = [password, block, limit]
    users = decode(users) # дешифровка паролей
    
    nick = EntrNick.get() # получение никнейма пользователя из поля ввода
    password = EntrPassword.get() # получение пароля пользователя из поля ввода

    if nick == "admin": # проверка админ ли входит в систему
        if password == users[nick][0]:
            AdminAbil(nick, password, users, path)
        else:
            showerror(title="Ошибка", message="Пароль неверный")
            global WrongPassA
            WrongPassA += 1
            if WrongPassA == 3: # Прекращение работы если превышено число неверных вводов пароля
                exit(0)
    elif nick in users: # поиск пользователя в базе
        if users[nick][1] == "1": # Проверка забанен ли пользовтель
            showerror(title="Ошибка", message="Вы были забанены пожизнено)")
            exit(0)
        if password == users[nick][0]: # проверка пароля
            UserAbil(nick, password, users, path)
        else:
            showerror(title="Ошибка", message="Пароль неверный")
            global WrongPassU
            WrongPassU += 1
            if WrongPassU == 3: # Прекращение работы если превышено число неверных вводов пароля
                exit(0)
    else:
        showerror(title="Ошибка", message="Пользователь не найден")

root = Tk() # создание главного окна
root.title("Вход в систему")
root.geometry("1500x800") 


ttk.Label(text="Имя").pack(anchor=CENTER)
EntrNick = ttk.Entry()
EntrNick.pack(anchor=CENTER) # Ввод имени
ttk.Label(text="Пароль").pack(anchor=CENTER)
EntrPassword = ttk.Entry()
EntrPassword.pack(anchor=CENTER) # Ввод пароля

EnterButton = ttk.Button(text="Войти", command=entry)
EnterButton.pack(anchor=CENTER, pady=10) # Кнопка входа

root.mainloop()




    
