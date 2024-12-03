import pytest

from src.utils import transaction_returner


def test_transaction_returner(list_transactions_from_json):
    assert \
        (transaction_returner('C:\\Users\\racco\\PycharmProjects\\Vidget_Operations_Project\\data\\operations.json') ==
         list_transactions_from_json)


def test_transaction_returner_empty():
    assert transaction_returner('C:\\Users\\racco\\PycharmProjects\\Vidget_Operations_Project\\data\\empty.json') == []


def test_transaction_returner_not_list():
    assert (transaction_returner('C:\\Users\\racco\\PycharmProjects\\Vidget_Operations_Project\\data\\onedict.json') ==
            [])


def test_transaction_returner_incorrect_path():
    assert (transaction_returner('C:\\Users\\racco\\PycharmProjects\\Vidget_Operations_Project\\data\\somename.json')
            == [])


