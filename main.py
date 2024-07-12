import glob
import os
from random import choice
import re
from timeit import default_timer as timer

from constants import CACHE_PATH, TEST_DATA_PATH
from helpers import get_indexes, print_header
from solvers import linecache, naive, BucketFind


def run(algos_to_run, run_counts):
    test_files = TEST_DATA_PATH.glob('**/*')
    skipped_files = []
    print_header(algos_to_run)

    for test_file_path in sorted(test_files):
        if any([skip_test in str(test_file_path) for skip_test in skipped_files]):
            pass
        else:
            test_file_name = str(test_file_path.stem)
            length = int(re.findall(r'\d+', test_file_name)[1])
            random_indexes = get_indexes(length)

            runs = run_counts[0] if length > 1000 else run_counts[1]

            print(f"{test_file_name:<40}{runs:<20}", end="")

            for algorithm in selected_algos:
                start = timer()
                for i in range(runs):
                    index = choice(random_indexes)
                    algorithm(index, test_file_path)
                end = timer()
                run_time = end - start
                print(f"{run_time:<20.5f}", end="")
            print("")


if __name__ == '__main__':
    CACHE_PATH.mkdir(parents=True, exist_ok=True)
    TEST_DATA_PATH.mkdir(parents=True, exist_ok=True)
    clear_cache = False
    if clear_cache:
        print("Clearing cache...")
        files = glob.glob('./temp/*/*')
        for f in files:
            os.remove(f)

    # add the name of your function here
    selected_algos = [naive, linecache, BucketFind.okay_algo_5, BucketFind.okay_algo_1, BucketFind.okay_algo_01]

    run_counts = [10, 1000]
    run(selected_algos, run_counts)
