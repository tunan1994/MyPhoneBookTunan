import csv
import json

def import_csv():
    result = []
    with open("file_for_import.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue

            else:
                temp_dict = {}
                temp_dict['surname'] = row[0]
                temp_dict['name'] = row[1]
                temp_dict['tel'] = row[2]
                temp_dict['comment'] = row[3]
                result.append(temp_dict)

            count += 1
    with open('data_base.json', 'w') as file:
        json.dump(result, file, indent=2)

    print()
    print(f'Контакты импортированы. {count-1} контактов.')





