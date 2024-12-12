import json
import os

import requests
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
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
               f"{transaction["operationAmount"]["currency"]["code"]}&amount="
               f"{transaction["operationAmount"]["amount"]}")
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text
        result = json.loads(result)
        return round(result["result"], 2)
    else:
        raise ValueError("неподходящая валюта для конвертации")
