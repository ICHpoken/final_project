#Делаем плоский словарь
def flat_dict(d: dict, parent_key: str = '', sep: str ='.'):
    
    items = []
    for key, value in d.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            items.extend(flat_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    
    return dict(items)