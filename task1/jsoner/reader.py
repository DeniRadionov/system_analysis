import json
import numpy as np
from reader import Reader

class JSONReader(Reader):
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            my_dict = json.load(f)
            self.json_data =[[inner_dict[key] for key in inner_dict] for inner_dict in my_dict.values()]


    def get_at(self, x: int, y: int) -> str:
        return self.json_data[0][x][y]