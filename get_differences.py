import yaml
from flact_dict import flat_dict

#Проверка словаря на вложенность
def check_if_nested(file):
    return any(isinstance(value, dict) for value in file.values())


#Получаем массив ключей
def get_all_keys(data1,data2):
    return sorted(list(set(list(data1.keys()) + list(data2.keys()))))


#получение данных из файла
def get_data(file):
    
    with open(file) as file:
       data = yaml.safe_load(file)
    
    if check_if_nested(data):
        return flat_dict(data)
    else:
        return data


#сравнение данных из файлов, вывод отличий
def get_differences(file1, file2):

    data1 = get_data(file1)
    data2 = get_data(file2)

    all_keys = get_all_keys(data1, data2)
    
    for key in all_keys:
        
        if key in data1 and key in data2 and data1[key] != data2[key]:
            print(f"Ключ '{key}' изменён. Было '{data1.get(key)}'. Стало '{data2.get(key)}'")
        
        if key not in data1 and key in data2:
            print(f"Ключ '{key}' добавлен: '{data2.get(key)}'")
        
        if key in data1 and key not in data2:
            print(f"Ключ '{key}' удален")