import os

import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

payload = {}
headers = {
    "apikey": API_KEY
}


def converter_into_rubles(transaction: dict) -> float:
    """Принимает на вход словарь с информацией о транзакции. Возвращает сумму транзакции в рублях. Поддерживает валюты
    RUB, USD, EUR"""
    if transaction["operationAmount"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    elif transaction["operationAmount"]["code"] == "USD" or transaction["operationAmount"]["code"] == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction["operationAmount"]
        ["code"]}&amount={transaction["operationAmount"]["amount"]}"
        response = requests.request("GET", url, headers=headers, data=payload)
        result = float(response.text)
        return result
    else:
        raise ValueError("неподходящая валюта для конвертации")

print(converter_into_rubles({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}))
