import pytest

from src.filereaders import reader_from_csv, reader_from_excel

from unittest.mock import patch

import csv


@patch("csv.DictReader")
def test_reader_from_csv(mock_datafiles):
    mock_datafiles.return_value = [{"test": "1"}]
    assert (reader_from_csv("C:\\Users\\Lenovo\\PycharmProjects\\George-s_repository\\data\\transactions.csv") ==
            [{"test": "1"}])


def test_reader_from_csv_not_files():
    assert reader_from_csv("C:\\Users\\Lenovo\\PycharmProjects\\George-s_repository\\data\\qwerty.csv") == []


@patch("reader.to_dict")
def test_reader_from_excel(mock_datafiles):
    mock_datafiles.return_value = [{"test": "1"}]
    assert (reader_from_excel("C:\\Users\\Lenovo\\PycharmProjects\\George-s_repository\\data\\transactions_excel.xlsx")
            == [{"test": "1"}])