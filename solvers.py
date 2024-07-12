import pickle
from itertools import zip_longest
from linecache import getline
from pathlib import Path
from constants import CACHE_PATH


def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def linecache(i: int, path: Path) -> str:
    return getline(str(path), i)


def naive(i: int, path: Path) -> str:
    with path.open() as f:
        lines = f.readlines()
        return lines[i]


# DO NO READ THIS SECRET RECIPE
class BucketFind:
    cached = []
    init = False
    cache_path = CACHE_PATH/"bucket"
    cache_list_path = Path(cache_path, 'bucket_find_cache.pkl')

    @staticmethod
    def initialize():
        BucketFind.cache_path.mkdir(parents=True, exist_ok=True)
        if BucketFind.cache_list_path.exists():
            with BucketFind.cache_list_path.open('rb') as f:
                BucketFind.cached = pickle.load(f)

    @staticmethod
    def okay_algo_1(i: int, path: Path, split_by: int = 1000) -> str:
        return BucketFind.okay_algo_5(i, path, split_by)

    @staticmethod
    def okay_algo_01(i: int, path: Path, split_by: int = 100) -> str:
        return BucketFind.okay_algo_5(i, path, split_by)

    @staticmethod
    def okay_algo_5(i: int, path: Path, split_by: int = 5000) -> str:
        if not BucketFind.init:
            BucketFind.initialize()
            BucketFind.init = True
        file_split_identifier = f"{str(path)}_{split_by}"
        if file_split_identifier not in BucketFind.cached:
            BucketFind.split_file(path, split_by)

        a = int(i / split_by)*split_by
        small_file_path = Path(BucketFind.cache_path / f"{path.stem}_{a}_{split_by}.txt")
        edited_index = i % split_by
        with small_file_path.open() as f:
            lines = f.readlines()
            return lines[edited_index]

    @staticmethod
    def split_file(path: Path, lines_per_file):
        file_split_identifier = f"{str(path)}_{lines_per_file}"
        with path.open() as input_file:
            for i, g in enumerate(grouper(lines_per_file, input_file, fillvalue='')):
                split_file_path = Path(BucketFind.cache_path / f"{path.stem}_{i*lines_per_file}_{lines_per_file}.txt")
                with split_file_path.open('w') as split_file:
                    split_file.writelines(g)
        BucketFind.cached.append(file_split_identifier)
        with BucketFind.cache_list_path.open('wb') as f:
            pickle.dump(BucketFind.cached, f)
