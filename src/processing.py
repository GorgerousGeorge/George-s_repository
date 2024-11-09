def filter_by_state(dict_list: list, state_value: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа
    state. Возвращает новый список словарей, содержащий только те словари, у которых
    ключ state соответствует указанному значению по умолчанию 'EXECUTED')"""
    returned_list = []
    for dict_ in dict_list:
        if dict_['state'] == state_value:
            returned_list.append(dict_)
    return returned_list
