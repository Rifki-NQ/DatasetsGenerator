import pandas as pd
import random
import string

class Generator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.columns_length = 0
        self.rows_length = 0
        
    def data_config(self, custom_columns: bool):
        while True:
            self.columns_length = input("Select length of column: ")
            if self.columns_length.isdigit():
                self.columns_length = int(self.columns_length)
                break
            else:
                print("length of column must be digit!")
        while True:
            self.rows_length = input("Select length of row: ")
            if self.rows_length.isdigit() and int(self.rows_length) > 0:
                self.rows_length = int(self.rows_length)
                break
            elif self.rows_length.isdigit():
                print("Length of row must be at least 1")
            else:
                print("Length of row must be digit!")
    
    def generate(self):
        if not self.check_dataset():
            print("Cancelled!")
            return
        self.data_config(custom_columns=False)
        #generate the dataset
        for column in range(self.columns_length):
            pass
        print("success!")
    
    def generate_custom(self):
        pass
    
    def ask_overwrite(self) -> bool:
        print("Data file already has data inside it, overwrite?")
        while True:
            option = input("y/n: ")
            if option.lower() == "y":
                return True
            elif option.lower() == "n":
                return False
            else:
                print("Invalid option inputted!")
    
    def check_dataset(self):
        try:
            df = pd.read_csv(self.file_path)
            overwrite = self.ask_overwrite()
            return overwrite
        except:
            return True