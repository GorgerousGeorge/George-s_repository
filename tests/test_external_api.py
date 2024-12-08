import json
from unittest.mock import patch

import pytest

from src.external_api import converter_into_rubles


@patch("requests.request")
def test_converter_into_rubles_from_usd(mock_api_responce):
    mock_data = {"result":100.01}
    mock_api_responce.return_value.text = json.dumps(mock_data)
    assert converter_into_rubles({
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "code": "USD"
            }
        },
       }) == 100.01
    mock_api_responce.assert_called_once()


@patch("requests.request")
def test_converter_into_rubles_from_eur(mock_api_responce):
    mock_data = {"result":200.01}
    mock_api_responce.return_value.text = json.dumps(mock_data)
    assert converter_into_rubles({
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "code": "EUR"
            }
        },
       }) == 200.01
    mock_api_responce.assert_called_once()


def test_converter_into_rubles_from_rub():
    assert converter_into_rubles({
        "operationAmount": {
            "amount": "300.58",
            "currency": {
                "code": "RUB"
            }
        },
       }) == 300.58


def test_converter_into_rubles_from_gbp():
    with pytest.raises(ValueError):
        converter_into_rubles({
            "operationAmount": {
                "amount": "300.58",
                "currency": {
                    "code": "GBP"
                }
            },
        }) == "неподходящая валюта для конвертации"
