import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture
def numbers_16():
    return "7000792289606361"


@pytest.fixture
def numbers_16_spases():
    return "7000 7922 8960 6361"


@pytest.fixture
def numbers_16_int():
    return 7000792289606361


@pytest.fixture
def numbers_20():
    return "70007922896063611234"


@pytest.fixture
def numbers_20_spases():
    return "70007 92289 60636 11234"


@pytest.fixture
def numbers_20_int():
    return 70007922896063611234


@pytest.fixture
def numbers_19():
    return "7000792289606361123"


@pytest.fixture
def numbers_21():
    return "700079228960636112345"


@pytest.fixture
def numbers_13():
    return "7000792289606"


@pytest.fixture
def numbers_12():
    return "700079228960"


@pytest.fixture
def letters():
    return "тестовые_буквы"


@pytest.fixture
def numbers_and_letters():
    return "a1b2c3d4e5f6g7h8i9j0"


@pytest.fixture
def blank():
    return ""


@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    (numbers_16, "7000 79** **** 6361"),
    (numbers_16_spases, "7000 79** **** 6361"),
    (numbers_16_int, "7000 79** **** 6361"),
    (numbers_19, "7000 79** **** 1123"),
    (numbers_13, "7000 79** **** 9606")
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    (numbers_20, "некорректный номер карты"),
    (numbers_12, "некорректный номер карты"),
    (letters, "некорректный номер карты"),
    (numbers_and_letters, "некорректный номер карты"),
    (blank, "некорректный номер карты")
])
def test_get_mask_card_number_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    (numbers_20, "**1234"),
    (numbers_20_spases, "**1234"),
    (numbers_20_int, "**1234"),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize("value, expected", [
    (numbers_16, "некорректный номер счета"),
    (numbers_19, "некорректный номер счета"),
    (letters, "некорректный номер счета"),
    (numbers_and_letters, "некорректный номер счета"),
    (blank, "некорректный номер счета"),
    (numbers_21, "некорректный номер счета"),
])
def test_get_mask_account_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_mask_account(value) == expected
