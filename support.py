import os
from data import name_data, surname_data, phone_data, address_data


def write():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    form = int(input("В каком формате записать данные\n\n"
                     "1 вариант\n"
                     f"{name}\n{surname}\n{phone}\n{address}\n\n"
                     "2 вариант: \n"
                     f"{name};{surname};{phone};{address}\n"
                     "Выбрать вариант: "))
    while form != 1 and form != 2:
        form = int(input('Вы ввели неправильный номер, запишите его снова\n'))
    if form == 1:
        with open('varian1.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif form == 2:
        with open('varian2.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def readln():
    form = int(input("Выберите файл для просмотра\n"
                     "1 файл varian1.csv\n"
                     "2 файл varian2.csv\n"))
    while form != 1 and form != 2:
        form = int(input('Вы ввели неправильный номер, запишите его снова\n'))
    if form == 1:
        if os.path.exists("varian1.csv"):
            print('Выводим данные из файла varian1.csv\n')
            with open('varian1.csv', 'r', encoding='utf-8') as f:
                log1 = f.readlines()
                print(''.join(log1))
        else:
            print('Файл не существует')
    elif form == 2:
        if os.path.exists("varian2.csv"):
            print('Выводим данные из файла varian2.csv\n')
            with open('varian2.csv', 'r', encoding='utf-8') as f:
                log2 = f.readlines()
                print(''.join(log2))
        else:
            print('Файл не существует')


def deletef():
    form = int(input("Выберите файл для удаления\n"
                     "1 файл varian1.csv\n"
                     "2 файл varian2.csv\n"))
    while form != 1 and form != 2:
        form = int(input('Вы ввели неправильный номер, запишите его снова\n'))

    if form == 1:
        if os.path.exists("varian1.csv"):
            os.remove("varian1.csv")
            print("Файл varian1.csv был удален.")
        else:
            print("Файл varian1.csv не существует.")
    elif form == 2:
        if os.path.exists("varian2.csv"):
            os.remove("varian2.csv")
            print("Файл varian2.csv был удален.")
        else:
            print("Файл varian2.csv не существует.")


def update():
    form = int(input("Выберите файл для изменения\n"
                     "1 файл varian1.csv\n"
                     "2 файл varian2.csv\n"))
    while form != 1 and form != 2:
        form = int(input('Вы ввели неправильный номер, запишите его снова\n'))
    if form == 1:
        file_name="varian1.csv"
    elif form == 2:
        file_name="varian2.csv"
    if os.path.exists(file_name):
        print(f'Выводим данные из файла {file_name}\n')
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                print(f"{i + 1}: {lines[i].strip()}")
            numlist = int(input(f"Введите номер строки для изменения (1-{len(lines)}): "))
            while numlist < 1 or numlist > len(lines):
                numlist = int(
                    input(f'Некорректный номер строки. Введите номер строки для изменения (1-{len(lines)}): '))
            line_to_change = lines[numlist - 1]
            stro = input("Введите новое значение строки: ")
            listn = stro + '\n'
            lines[numlist - 1] = listn
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Данные изменены.")
    else:
        print(f'Файл {file_name} не существует')


