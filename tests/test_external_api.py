import pytest
from src.external_api import converter_into_rubles
from unittest.mock import patch
import requests
import json


@patch("requests.request")
def test_converter_into_rubles_from_usd(mock_api_responce):
    mock_data = {"result":100.01}
    mock_api_responce.return_value.json.return_value = json.dumps(mock_data)
    assert converter_into_rubles({
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "code": "USD"
            }
        },
       }) == 100.01
    mock_api_responce.assert_called_once()
