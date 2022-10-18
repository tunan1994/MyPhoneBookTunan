import json


def search(num):

    with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)

    search_res = []
    if num == 1:
        surname_key = input('Введите фамилию контакта: ')
        for i in phone_dir:
            if i['surname'] == surname_key:
                search_res.append(i)
        return search_res


    search_res = []
    if num == 2:
        tel_key = input('Введите номер контакта: ')
        for i in phone_dir:
            if i['tel'] == tel_key:
                search_res.append(i)
        return search_res



