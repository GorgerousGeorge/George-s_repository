import csv

def reader_from_csv(path: str) -> list[dict]:
    """Принимает на вход путь к файлу csv. Возвращает список словарей из файла"""
    returned_list = []
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                returned_list.append(row)
    except Exception:
        raise ValueError("ошибка при открытии файла")
    finally:
        return returned_list

