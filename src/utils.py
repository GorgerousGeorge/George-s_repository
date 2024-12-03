import json


def transaction_returner(path: str) -> list[dict]:
    returned_list = []
    try:
        with open(path, encoding="utf-8") as json_file:
            content = json.load(json_file)
            if isinstance(content, list):
                returned_list = content
    finally:
        return returned_list


print(transaction_returner('C:\\Users\\racco\\PycharmProjects\\Vidget_Operations_Project\\data\\operations.json'))
