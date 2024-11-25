def filter_by_currency(transaction_list:list[dict], valute: str = "USD") -> dict:
    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == valute:
            yield transaction


