import pickle
from pathlib import Path
from random import randint
from timeit import default_timer as timer
from faker import Faker


def generate_tests():
    fake = Faker()
    lines = []
    line_count = 1000000
    start = timer()
    for i in range(line_count):
        max_range = randint(10, 1000)
        line = fake.text(max_range).replace("\n", "")
        lines.append(f"{line}\n")
        if i % 100000 == 0 and i > 90000:
            end = timer()
            print(f"{i}/{line_count} - {end - start}s")

    file_path = Path(f"data", f"test_en_words_{line_count}_long_2.txt")
    with file_path.open('w') as f:
        f.writelines(lines)


def generate_number_data():
    number_list = []
    for i in range(100000):
        number_list.append(randint(0, 5000))
    number_list = sorted(number_list)
    with Path("data/number_array_list_0_positive_small").open('wb') as f:  # open a text file
        pickle.dump(number_list, f)  # serialize the list


if __name__ == '__main__':
    generate_tests()
