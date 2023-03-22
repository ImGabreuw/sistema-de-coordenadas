from typing import List


def format_number(number: float) -> str:
    return "{:.2f}".format(number).replace(".", ",")


def int_list_input(message: str) -> List[int]:
    return [int(i) for i in input(message).split()]
