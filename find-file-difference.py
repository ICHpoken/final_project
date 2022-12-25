import yaml
import argparse
from collections.abc import MutableMapping

#проверка на идентичность файлов
def isEqual(data1, data2):
    data1 = dict(sorted(data1.items()))
    data2 = dict(sorted(data2.items()))
    return data1 == data2 

#Делаем плоский словарь
def flat_dict(d: MutableMapping, parent_key: str = '', sep: str ='.'):
    items = []
    for key, value in d.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flat_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


#сравнение файлов, вывод отличий
def find_difference(data1, data2):

    all_keys = list(data1.keys()) + list(data2.keys())
    all_keys = sorted(list(set(all_keys)))
    
    for key in all_keys:
        
        if key in data1 and key in data2 and data1[key] != data2[key]:
            print(f"Ключ '{key}' изменён. Было '{data1.get(key)}'. Стало '{data2.get(key)}'")
        
        if key not in data1 and key in data2:
            print(f"Ключ '{key}' добавлен: '{data2.get(key)}'")
        
        if key in data1 and key not in data2:
            print(f"Ключ '{key}' удален")


def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--file1', required = True)
    parser.add_argument('--file2', required = True)

    args = parser.parse_args()

    with open(args.file1) as file:
        data1 = yaml.safe_load(file)
    data1 = flat_dict(data1)
    
    with open(args.file2) as file:
        data2 = yaml.safe_load(file)
    data2 = flat_dict(data2)
    
    if isEqual(data1, data2):
        print('Файлы идентичные')
        exit()
    
    
    find_difference(data1, data2)


if __name__ == '__main__':
    main()
    





