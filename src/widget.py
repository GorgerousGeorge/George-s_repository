from src import masks


def mask_account_card(card_info: str) -> str:
    """Принимает тип и номер карты/счета, возвращает замаскированный номер карты/счета"""
    if card_info == "":
        return "нет данных"
    card_infolist = card_info.split()
    if card_infolist[0] == "Счет" or card_infolist[0] == card_infolist[-1]:
        if card_infolist[-1] == "Счет":
            return "номер счета не указан"
        returned_number = masks.get_mask_account(card_infolist.pop(-1))
    else:
        if card_infolist[-1].isdigit():
            returned_number = masks.get_mask_card_number(card_infolist.pop(-1))
        else:
            return "номер карты не указан"
    card_infolist.append(returned_number)
    masked_number = " ".join(card_infolist)
    return str(masked_number)


def get_date(core_date: str) -> str:
    """Принимает дату и время в формате ISO 8601, возвращает дату в формате ДД.ММ.ГГГГ"""
    core_date_list = core_date.split("-")
    returned_date = core_date_list[2][:2] + "." + core_date_list[1] + "." + core_date_list[0]
    return returned_date
