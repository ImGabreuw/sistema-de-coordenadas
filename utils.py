from typing import List


def format_number(number: float) -> str:
    return "{:.2f}".format(number).replace(".", ",")


def int_input(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        return int_input(message)


def int_list_input(message: str) -> List[int]:
    try:
        return [int(i) for i in input(message).split()]
    except ValueError:
        return int_list_input(message)
