def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("""Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
        type_of_file = input()
        if type_of_file == "1" or type_of_file.lower() == "json":
            descr_type_file = "JSON"
            break
        elif type_of_file == "2" or type_of_file.lower() == "csv":
            descr_type_file = "CSV"
            break
        elif type_of_file == "3" or type_of_file.lower() == "xlsx":
            descr_type_file = "XLSX"
            break
        else:
            print("Некорректный выбор пункта в меню. Необходимо выбрать один из предложенных вариантов")
    print(f"Для обработки выбран {descr_type_file}-файл.\n")
    path = input("Введите путь к файлу.\n")
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        status_for_filter = input()
        status_for_filter = status_for_filter.upper()
        if status_for_filter == "EXECUTED" or status_for_filter == "CANCELED" or status_for_filter == "PENDING":
            print(f"Операции отфильтрованы по статусу {status_for_filter}")
            break
        else:
            print(f"Статус операции {status_for_filter} недоступен")

