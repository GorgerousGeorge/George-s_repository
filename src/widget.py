import masks


def mask_account_card(card_info: str) -> str:
    """Принимает тип и номер карты/счета, возвращает замаскированный номер карты/счета"""
    card_info = card_info.split()
    print(card_info)
    if card_info[0] == "Счет":
        returned_number = masks.get_mask_account(card_info.pop(-1))
    else:
        returned_number = masks.get_mask_card_number(card_info.pop(-1))
    card_info.append(returned_number)
    card_info = " ".join(card_info)
    return card_info


def get_date(core_date: str) -> str:
    """Принимает дату и время в формате ISO 8601, возвращает дату в формате ДД.ММ.ГГГГ"""
    core_date = core_date.split("-")
    returned_date = core_date[2][:2] + "." + core_date[1] + "." + core_date[0]
    return returned_date
