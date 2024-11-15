import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize("value, expected", [
    (numbers_16, "7000 79** **** 6361"),
    (numbers_16_spases, "7000 79** **** 6361"),
    (numbers_16_int, "7000 79** **** 6361"),
    (numbers_20, "некорректный номер карты"),
    (numbers_19, "7000 79** **** 1123"),
    (numbers_13, "7000 79** **** 9606"),
    (numbers_12, "некорректный номер карты"),
    (letters, "некорректный номер карты"),
    (numbers_and_letters, "некорректный номер карты"),
    (blank, "некорректный номер карты")
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    (numbers_16, "некорректный номер счета"),
    (numbers_20, "**1234"),
    (numbers_19, "некорректный номер счета"),
    (letters, "некорректный номер счета"),
    (numbers_and_letters, "некорректный номер счета"),
    (blank, "некорректный номер счета"),
    (numbers_20_spases, "**1234"),
    (numbers_20_int, "**1234"),
    (numbers_21, "некорректный номер счета"),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
