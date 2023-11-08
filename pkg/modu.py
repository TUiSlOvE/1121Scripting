def triangle_zhonxin(a, b, c):
    x = (a[0] + b[0] + c[0]) / 3
    y = (a[1] + b[1] + c[1]) / 3
    return round(x), round(y)


import json

def read_json(file_name: str) -> dict:
    """將 json 檔案轉為字典後回傳"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def print_json(data: dict) -> None:
    """將字典轉爲 json 字串後輸出到螢幕"""
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_str)

def process_data(data: dict, discount: float) -> None:
    """將字典中每個菜品的價格打discount 折數"""
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)

def write_json(data: dict, file_name: str) -> None:
    """將字典轉為檔案"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
