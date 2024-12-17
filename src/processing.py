import re
from collections import Counter
from datetime import datetime


def filter_by_state(dict_list: list, state_value: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state. Возвращает новый список словарей, содержащий
    только те, у которых ключ state соответствует указанному значению (по умолчанию 'EXECUTED')"""
    returned_list = []
    for dict_ in dict_list:
        if dict_["state"] == state_value:
            returned_list.append(dict_)
    return returned_list


def sort_by_date(dict_list: list, sort_by_date_descending: bool = True) -> list:
    """Принимает список словарей. Возвращает новый список, отсортированный по дате от новых к старым. Если надо
    изменить порядок сортировки, то при вызове функции вторым параметром передай False"""
    sorted_list = sorted(
        dict_list, key=lambda strindate: datetime.fromisoformat(strindate["date"]), reverse=sort_by_date_descending
    )
    return sorted_list


def filter_by_description(transaction_list: list[dict], search_value: str) -> list[dict]:
    """Принимает список словарей и строковое значение. Возвращает список словарей, у которых ключ description
    соответствует строке из второго аргумента (в том числе частично)"""
    returned_list = []
    for transaction in transaction_list:
        if re.search(search_value, transaction["description"], flags=re.IGNORECASE):
            returned_list.append(transaction)
    return returned_list


def counter_by_description(transaction_list: list[dict], description_list: list[str]) -> dict:
    """Принимает на вход список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории. Если категория была в передаваемом списке категорий операций, а в возвращенном словаре
    ее нет - значит, количество операций с такой категорией равно 0"""
    list_for_requirement = []
    for description in description_list:
        for transaction in transaction_list:
            if transaction["description"] == description.title():
                list_for_requirement.append(transaction["description"])
    returned_dict = Counter(list_for_requirement)
    return returned_dict
