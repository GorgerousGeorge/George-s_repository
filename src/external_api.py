import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()

payload = {}
headers = {
    "apikey": os.getenv("API_KEY")
}


def converter_into_rubles(transaction: dict) -> float:
    """Принимает на вход словарь с информацией о транзакции. Возвращает сумму транзакции в рублях. Поддерживает валюты
    RUB, USD, EUR"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif (transaction["operationAmount"]["currency"]["code"] == "USD" or
          transaction["operationAmount"]["currency"]["code"] == "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction["operationAmount"]
        ["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}"
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text
        result = json.loads(result)
        print(result)
        return round(result["result"], 2)
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
