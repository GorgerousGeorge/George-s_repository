from sys import exception
import os


def log(filename: str = "DEFAULT"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logging = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                result = None
            else:
                logging = f"{func.__name__} ok"
            if filename == "DEFAULT":
                print(logging)
            else:
                if os.path.isdir(f"{os.getcwd()}\\logs") == False:
                    os.mkdir(f"{os.getcwd()}\\logs")
                with open(f"{os.getcwd()}\\logs\\{filename}", "a") as file:
                    file.write(f"{logging} \n")
            return result

        return wrapper

    return decorator
