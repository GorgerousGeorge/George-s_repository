import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\logs\\masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_returner(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла со списком словарей и возвращает список словарей, как объект python.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    returned_list = []
    try:
        logger.info(f"Открываем файл {path}")
        with open(path, encoding="utf-8") as json_file:
            logger.info(f"Открыли файл {path} успешно")
            content = json.load(json_file)
            if isinstance(content, list):
                returned_list = content
                logger.info("Содержание файла корректное, возвращаем список")
            else:
                logger.error(f"Некорректный ввод. Файл {path} содержит не список")
    except Exception as exce:
        logger.error(f"Ошибка при попытке открыть файл {path}: {exce}")
    finally:
        return returned_list
