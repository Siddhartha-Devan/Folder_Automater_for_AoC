import os
import sys

class AoC:
    def __init__(self, folder_name):
        # os.makedirs(folder_name, exist_ok=True)
        self.folder_name = folder_name
        self.files = ["1.py", "2.py", "samp_inp.txt", "inp.txt"]

    def create_folders(self):
        if os.path.exists(self.folder_name):
            print(self.folder_name, "already exists...")
        else:
            print(os.makedirs(self.folder_name, exist_ok=True))
            for f in self.files:
                path = os.path.join(self.folder_name, f)
                with open(path, 'w') as file:
                    pass  # Create an empty file
                print(f"File '{f}' created in '{self.folder_name}'.")

def main():

    if len(sys.argv) != 2:
        print("Usage: create_folders.py <day_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    creator_obj = AoC(folder_name)
    creator_obj.create_folders()

if __name__ == "__main__":
    main()