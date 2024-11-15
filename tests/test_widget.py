from src.widget import mask_account_card
from src.widget import get_date

def test_mask_account_card():
    assert mask_account_card("Visa 1234567890123456") == "1234 56** **** 3456"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"