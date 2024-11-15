import pytest


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
