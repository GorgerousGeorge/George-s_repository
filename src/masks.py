import logging
import os
from typing import Any

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\logs\\masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Any) -> str:
    """Принимает на вход номер карты, возвращает маску карты в типе str"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    logger.info(f"Маскируем карту с номером {card_number}")
    if card_number.isdigit() and 12 < len(card_number) < 20:
        masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info("Номер карты замаскирован")
        return str(masked_card_number)
    logger.error(f"введен некорректный номер карты - {card_number}")
    raise ValueError("некорректный номер карты")


def get_mask_account(account_number: Any) -> str:
    """Принимет номер счета, возвращает маску счета в типе str"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    logger.info(f"Маскируем счет с номером {account_number}")
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[-4:]
        logger.info("Номер счета замаскирован")
        return str(masked_account)
    logger.error(f"введен некорректный номер счета - {account_number}")
    raise ValueError("некорректный номер счета")
