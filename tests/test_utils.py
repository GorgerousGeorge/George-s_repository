from src.utils import transaction_returner
import os


def test_transaction_returner(list_transactions_from_json):
    assert \
        (transaction_returner(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\operations.json") ==
         list_transactions_from_json)


def test_transaction_returner_empty():
    assert transaction_returner(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\empty.json") == []


def test_transaction_returner_not_list():
    assert (transaction_returner(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\onedict.json") ==
            [])


def test_transaction_returner_incorrect_path():
    assert (transaction_returner(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\somename.json")
            == [])

