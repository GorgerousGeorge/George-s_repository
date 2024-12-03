from typing import Generator


def filter_by_currency(transaction_list: list[dict], valute: str = "USD") -> Generator:
    """Принимает список словарей, представляющих транзакции. Возвращает по одному словарю из списка, в котором валюта
    операции соответствует заданной (по умолчанию USD, для изменения вторым аргументом надо передать буквенный код
    валюты)"""
    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == valute:
            yield transaction


def transaction_descriptions(transaction_list: list[dict]) -> Generator:
    """Принимает список словарей, представляющих транзакции. Возвращает описания каждой операции из списка по одному"""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(start: int, finish: int) -> Generator:
    """Генерирует 16-значные номера карт в рамках заданного диапазона. При вызове генератора первым аргументом
    передаем начальное значение генерации диапазона, вторым аргументом передаем конечное значение диапазона
    (включительно)"""
    for card_number in range(start, finish + 1):
        card_number = str(card_number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
