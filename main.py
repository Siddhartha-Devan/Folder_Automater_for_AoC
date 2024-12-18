import os
import sys

class AoC:
    def __init__(self, folder_name):
        os.makedirs(folder_name, exist_ok=True)
        self.files = ["1.py", "2.py", "samp_inp.txt", "inp.txt"]

    def create_folders(self):