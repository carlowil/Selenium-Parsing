from Browser import *
from json_func import serialize_json

WB_ITEMS = []
YM_ITEMS = []


def handle_menu():
    print("1. Спарсить данные по вашему запросу\n"
          "2. Записать данные в postgre\n"
          "3. Записать данные в json\n"
          "4. Записать в файл txt\n"
          "5. Вывести данные в консоль\n"
          "6. Выйти")


def handle_input_menu():
    option = str(input("Ваш ввод: "))
    match option:
        case "1":
            request = str(input("Введите поисковой запрос: "))
            driver = init_driver()
            browser = Browser(driver)
            WB_ITEMS.extend(wb_parse(browser, request))
            YM_ITEMS.extend(ym_parse(browser, request))
            return False
        case "2":
            if not WB_ITEMS and not YM_ITEMS:
                print("Нет данных для записи!")
            else:
                print("2")
            return False
        case "3":
            if not WB_ITEMS and not YM_ITEMS:
                print("Нет данных для записи!")
            else:
                serialize_json(WB_ITEMS, "WB_ITEMS")
                serialize_json(YM_ITEMS, "YM_ITEMS")
            return False
        case "4":
            if not WB_ITEMS and not YM_ITEMS:
                print("Нет данных для записи!")
            else:
                print("4")
            return False
        case "5":
            if not WB_ITEMS and not YM_ITEMS:
                print("Нет данных для вывода!")
            else:
                print(f"{WB_ITEMS}\n{len(WB_ITEMS)}")
                print(f"{YM_ITEMS}\n{len(YM_ITEMS)}")
            return False
        case "6":
            print("Выход из программы")
            return True
        case _:
            print("Такой команды нет!")
