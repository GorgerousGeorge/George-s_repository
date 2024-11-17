import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"


def test_get_mask_card_number_with_spaces(numbers_16_spases):
    assert get_mask_card_number(numbers_16_spases) == "7000 79** **** 6361"


def test_get_mask_card_number_int(numbers_16_int):
    assert get_mask_card_number(numbers_16_int) == "7000 79** **** 6361"


def test_get_mask_card_number_maxnumber(numbers_19):
    assert get_mask_card_number(numbers_19) == "7000 79** **** 1123"


def test_get_mask_card_number_minnumber(numbers_13):
    assert get_mask_card_number(numbers_13) == "7000 79** **** 9606"


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


def test_get_mask_account(numbers_20):
    assert get_mask_account(numbers_20) == "**1234"


def test_get_mask_account_with_spaces(numbers_20_spases):
    assert get_mask_account(numbers_20_spases) == "**1234"


def test_get_mask_account_int(numbers_20_int):
    assert get_mask_account(numbers_20_int) == "**1234"


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
