import csv

import pandas as pd


def reader_from_csv(path: str) -> list[dict]:
    """Принимает на вход путь к файлу csv. Возвращает список словарей из файла"""
    returned_list = []
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            print(reader)
            for row in reader:
                returned_list.append(row)
    finally:
        return returned_list


def reader_from_excel(path: str) -> list[dict]:
    """Принимает на вход путь к файлу excel. Возвращает список словарей из файла"""
    returned_list = []
    try:
        reader = pd.read_excel(path)
        returned_list = reader.to_dict(orient="records")
    finally:
        return returned_list
