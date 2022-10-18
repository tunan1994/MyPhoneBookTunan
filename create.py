import json

def create(dict_ph):
    try:
        with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
    except:
        phone_dir = []

    phone_dir.append(dict_ph)
    with open('data_base.json', 'w') as file:
        json.dump(phone_dir, file, indent=2)
    print('Контакт добавлен в телефонный справочник')
    print()





