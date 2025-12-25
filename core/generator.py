import pandas as pd
import random
import string

class Generator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.columns_length = 0
        self.rows_length = 0
        
    def data_config(self):
        pass
    
    def generate(self):
        self.check_dataset()
        self.interface(custom=False)
        
        pass
    
    def generate_custom(self):
        pass
    
    def interface(self, custom: bool):
        
        pass
    
    def ask_overwrite(self):
        if self.df.empty:
            return True
        else:
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
        if not self.ask_overwrite:
            return