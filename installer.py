import zipfile # библиотека для разархивации 
from tkinter import * # для создания главного окна
from tkinter import ttk # для виджетов (кнопок, полей и т.д.)
from tkinter.messagebox import showerror # для показа окна с ошибкой
from tkinter import filedialog # для диалогового окна выбора файла
import psutil
import wmi
import win32api

def extract_file(zip_path, file_to_extract, extraction_path): # разархивация файлов
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(file_to_extract, extraction_path)

def install():
    zip_file = "auth.zip"
    file_to_extract = "passsword.exe"
    extraction_path = filedialog.askdirectory()
    extract_file(zip_file, file_to_extract, extraction_path)
    file_to_extract = "users.txt"
    extract_file(zip_file, file_to_extract, extraction_path)

    bd = open(extraction_path + "\\DataPC.txt", 'w+')
    
    # блок определения типа клавиатуры
    c = wmi.WMI()
    for keyboard in c.Win32_Keyboard():
        bd.write("Тип клавиатуры:" + keyboard.Description + "\n")
    
    # блок определения ширины экрана
    width_mm = win32api.GetSystemMetrics(0)
    bd.write("Ширина экрана:" + str(width_mm) + "мм\n")

    # блок определения объем памяти
    memory = psutil.virtual_memory()
    total_memory_gb = round(memory.total / (1024**3), 2)
    bd.write("Объем памяти:" + str(total_memory_gb) + "ГБ\n")

    # блок определения объема диска
    disk = psutil.disk_usage('/')
    total_disk_gb = round(disk.total / (1024**3), 2)
    bd.write("Объем диска:" + str(total_disk_gb) + "ГБ")

    root.destroy()
root = Tk() # создание главного окна
root.title("Вход в систему")
root.geometry("800x600") 

EnterButton = ttk.Button(text="УСТАНОВИТЬ", command=install)
EnterButton.pack(anchor=CENTER, pady=250) # Кнопка входа

root.mainloop()
