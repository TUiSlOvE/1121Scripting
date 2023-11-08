from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'

def main():
    # 讀取菜單 menu.json
    menu = read_json(MENU_FILE)

    # 將菜單顯示在畫面上
    print_json(menu)

    # 增加新的主菜項目
    new_item = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menu['categories'][1]['items'].append(new_item)

    # 讓使用者輸入折數
    discount = float(input("請輸入折扣率(0.0 ~ 1.0): "))

    # 根據折數將所有品項的單價打折
    process_data(menu, discount)

    # 顯示更新後的菜單
    print_json(menu)

    # 寫入 output.json
    write_json(menu, OUTPUT_FILE)

if __name__ == '__main__':
    main()
