import json
def get_value():
    print('Заполните следующие данные: ')
    dict_ph = {}
    dict_ph['surname'] = input('Введите фамилию: ')
    dict_ph['name'] = input('Введите имя: ')
    dict_ph['tel'] = input('Введите номер: ')
    dict_ph['comment'] = input('Комментарий: ')
    print()
    return dict_ph

def show_contact(list_res):

    print('Найдены следующие контакты: ')
    for num, i in enumerate(list_res):
        print()
        print(f'{num+1}'
              f'Фамилия: {i["surname"]}\n'
              f'Имя: {i["name"]}\n'
              f'Телефон: {i["tel"]}\n'
              f'Комментарий: {i["comment"]}\n')

def show_all_contact():

    with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
    print('Найдены следующие контакты: ')
    for num, i in enumerate(phone_dir):
        print()
        print(f'Контакт № {num+1}\n'
              f'Фамилия: {i["surname"]}\n'
              f'Имя: {i["name"]}\n'
              f'Телефон: {i["tel"]}\n'
              f'Комментарий: {i["comment"]}\n')