import pytest

from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    (7000792289606361, "7000 79** **** 6361"),
    ("7000792289606361123", "7000 79** **** 1123"),
    ("7000792289606", "7000 79** **** 9606")
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("70007922896063611234", "некорректный номер карты"),
    ("700079228960", "некорректный номер карты"),
    ("тестовые_буквы", "некорректный номер карты"),
    ("a1b2c3d4e5f6g7h8i9j0", "некорректный номер карты"),
    ("", "некорректный номер карты")
])
def test_get_mask_card_number_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("70007922896063611234", "**1234"),
    ("70007 92289 60636 11234", "**1234"),
    (70007922896063611234, "**1234"),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "некорректный номер счета"),
    ("7000792289606361123", "некорректный номер счета"),
    ("тестовые_буквы", "некорректный номер счета"),
    ("a1b2c3d4e5f6g7h8i9j0", "некорректный номер счета"),
    ("", "некорректный номер счета"),
    ("700079228960636112345", "некорректный номер счета"),
])
def test_get_mask_account_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_mask_account(value) == expected
