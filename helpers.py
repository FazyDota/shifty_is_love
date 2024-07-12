from random import randint
from typing import List


def get_indexes(length: int) -> List[int]:
    count = max([500, int(length/100)])
    indexes = set()
    for i in range(count):
        indexes.add(randint(0, length-1))
    return list(indexes)


def print_header(algos_list):
    print(f"{'TEST':<40}{'RUNS':<20}", end="")
    for algorithm in algos_list:
        print(f"{algorithm.__name__.upper():<20}", end="")
    print("")
