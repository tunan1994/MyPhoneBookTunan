import json


no = 'Такого пункта меню нет! Попробуйте еще раз.'
error = 'Ошибка!Попробуйте еще раз.'
srch = 'Введите номер пункта, который хотите выполнить: '

def check_main_menu():
    while True:
        try:
            num = int(input(srch))
            if 0<=num<=6:break
            else:
                print(no)
                continue
        except ValueError:
            print(error)


    return num

def check_search_menu():
    while True:
        try:
            num = int(input(srch))
            if 0<=num<=2:break
            else:
                print(no)
                continue
        except ValueError:
            print(error)


    return num

def check_directory():
    try:
        with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
            return True
    except:
        print('Ваш справочник пока еще пустой!')
        return False

def check_menu_act_contact():
    while True:
        try:
            num = int(input(srch))
            if 0<=num<=4:break
            else:
                print(no)
                continue
        except ValueError:
            print(error)


    return num

def check_menu_ch_con():
    while True:
        try:
            num = int(input(srch))
            if 1<=num<=4:break
            else:
                print(no)
                continue
        except ValueError:
            print(error)


    return num