import os

import pytest

from src.decorators import log


@log()
def working_function_console():
    return 1


@log(filename="testdecor.txt")
def working_function_with_file():
    return 1


@log()
def error_function_console(*args, **kwargs):
    raise ValueError("Something went wrong!")


@log(filename="testdecor.txt")
def error_function_with_file(*args, **kwargs):
    raise ValueError("Something went wrong!")


def test_log_working_decorator_console(capsys):
    working_function_console()
    captured = capsys.readouterr()
    assert captured.out == "working_function_console ok\n"


def test_log_working_decorator_file():
    working_function_with_file()
    with open(f"{os.getcwd()}\\logs\\testdecor.txt", "r") as file:
        lines = file.readlines()
        assert lines[-1] == "working_function_with_file ok \n"


@pytest.mark.parametrize("positionarg, namearg, expected", [
    ((), {}, "error_function_console error: Something went wrong!. Inputs: (), {}\n"),
    (("a", "b"), {}, "error_function_console error: Something went wrong!. Inputs: ('a', 'b'), {}\n"),
    ((), {'argument': '1'}, "error_function_console error: Something went wrong!. Inputs: (), {'argument':'1'}\n"),
    (("a", "b"), {'argument': '1'},
     "error_function_console error: Something went wrong!. Inputs: ('a', 'b'), {'argument':'1'}\n")
])
def test_log_error_console(capsys, positionarg, namearg, expected):
    with pytest.raises(ValueError):
        error_function_console(*positionarg, **namearg)
        captured = capsys.readouterr()
        assert captured.out == expected


@pytest.mark.parametrize("positionarg, namearg, expected", [
    ((), {}, "error_function_console error: Something went wrong!. Inputs: (), {}\n"),
    (("a", "b"), {}, "error_function_console error: Something went wrong!. Inputs: ('a', 'b'), {}\n"),
    ((), {'argument': '1'}, "error_function_console error: Something went wrong!. Inputs: (), {'argument':'1'}\n"),
    (("a", "b"), {'argument': '1'},
     "error_function_console error: Something went wrong!. Inputs: ('a', 'b'), {'argument':'1'}\n")
])
def test_log_error_file(positionarg, namearg, expected):
    with pytest.raises(ValueError):
        error_function_with_file(*positionarg, **namearg)
        with open(f"{os.getcwd()}\\logs\\testdecor.txt", "r") as file:
            lines = file.readlines()
            assert lines[-1] == expected
