import argparse
from typing import List

from csver.reader import CSVReader
from jsoner.reader import JSONReader

argParser = argparse.ArgumentParser()
argParser.add_argument("-f", "--filepath", type=str, help="Enter an absolute path to the file.")
argParser.add_argument("-q", "--search-query", nargs=2, type=int, metavar=('x', 'y'), help="Enter two integers, x and y.")

def main():
    args = argParser.parse_args()
    filepath: str = args.filepath
    x, y = args.search_query  # Получаем два целых числа из аргументов -q.

    client = None
    file_extension = filepath.rsplit(".", maxsplit=1)[-1]
    if file_extension == "csv":
        client = CSVReader(filepath)
    if file_extension == "json":
        client = JSONReader(filepath)


    result = client.get_at(x, y)
    print(result)

if __name__ == "__main__":
    main()
