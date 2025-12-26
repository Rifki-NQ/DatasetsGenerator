import pandas as pd
import random
import string

class Generator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.columns_length = 0
        self.rows_length = 0
        self.custom_columns_name = []
        self.custom_columns_type = {}
        
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
        #custom columns (optional)
        if custom_columns:
            #input custom columns name
            self.custom_columns_name = []
            skip_custom_columns = False
            for i in range(self.columns_length):
                if not skip_custom_columns:
                    column_name = input(f"Enter name for column no. {i} (s to skip the rest): ")
                    #option if user want to randomize the rest of columns name
                    if column_name.lower() == "s":
                        skip_custom_columns = True
                        self.custom_columns_name.append(self.randomizer(5))
                        continue
                    self.custom_columns_name.append(column_name)
                else:
                    self.custom_columns_name.append(self.randomizer(5))
            #select data type for each columns
            
    
    def generate(self):
        if not self.check_dataset():
            print("Cancelled!")
            return
        self.data_config(custom_columns=False)
        #generate the dataset
        generated_columns = []
        generated_df = {}
        for column in range(self.columns_length):
            generated_columns.append(self.randomizer(5).upper())
            generated_rows = []
            for row in range(self.rows_length):
                generated_rows.append(self.randomizer(5))
            generated_df[generated_columns[column]] = generated_rows
        #add generated dataset to dataframe
        self.df = pd.DataFrame(generated_df)
        self.df = self.df.to_csv(self.file_path, index=False)
        print("success!")
    
    def generate_custom(self):
        if not self.check_dataset():
            print("Cancelled!")
            return
        self.data_config(custom_columns=True)
        generated_df = {}
        for column in range(self.columns_length):
            generated_rows = []
            for row in range(self.rows_length):
                generated_rows.append(self.randomizer(5))
            generated_df[self.custom_columns_name[column]] = generated_rows
        #add generated dataset to dataframe
        self.df = pd.DataFrame(generated_df)
        self.df = self.df.to_csv(self.file_path, index=False)
        print("success!")
    
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
            self.df = pd.read_csv(self.file_path)
            overwrite = self.ask_overwrite()
            return overwrite
        except:
            self.df = pd.DataFrame()
            return True
        
    def randomizer(self, string_length: int) -> str:
        rand_string = "".join(random.choices(string.ascii_letters, k=string_length))
        return rand_string