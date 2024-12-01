from sys import exception


def log(filename: str = "DEFAULT"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logging = f"{func} error: {e}. Inputs: {*args}, {** kwargs}"
            else:
                logging = f"{func} ok"
            if filename == "DEFAULT":
                print(logging)
            else:
                with open(filename, "a") as file:
                    file.write(f"{logging} \n")
            return result
        return wrapper
    return decorator
