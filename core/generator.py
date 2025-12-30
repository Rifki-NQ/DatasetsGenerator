import pandas as pd
import numpy as np
import random
import string
from core.utils import Validation, DataIO

class Generator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.random_setting_value_path = "data/random_values_setting.csv"
        self.generated_df = {}
        self.columns_length = 0
        self.rows_length = 0
        self.custom_columns_name = []
        self.custom_columns_type = []
        self.update_random_values(how="pull")
    
    def update_random_values(self, how=""):
        if how == "push":
            updated_random_values = {
                "random_str_length": self.random_str_length,
                "random_int_min": self.random_int_min,
                "random_int_max": self.random_int_max,
                "random_float_min": self.random_float_min,
                "random_float_max": self.random_float_max,
                "random_float_round": self.random_float_round,
            }
            df = pd.DataFrame(updated_random_values, index=[0])
            df.to_csv(self.random_setting_value_path, index=False)
        elif how == "pull":
            data_io = DataIO(self.random_setting_value_path, value_setting=True)
            if data_io.read_data() is None:
                self.set_random_values()
            elif data_io.check_random_values_headers():
                self.set_random_values()
            else:
                df = data_io.read_data()
                self.random_str_length = df["random_str_length"].tolist()[0]
                self.random_int_min = df["random_int_min"].tolist()[0]
                self.random_int_max = df["random_int_max"].tolist()[0]
                self.random_float_min = df["random_float_min"].tolist()[0]
                self.random_float_max = df["random_float_max"].tolist()[0]
                self.random_float_round  = df["random_float_round"].tolist()[0]
    
    def set_random_values(self):
        while True:
            str_length = input("Set random string length: ")
            if str_length.isdigit():
                self.random_str_length = int(str_length)
                break
            else:
                print("value must be in digit!")
        while True:
            int_min = input("Set random int minimum value: ")
            if int_min.isdigit():
                self.random_int_min = int(int_min)
                break
            else:
                print("value must be in digit!")
        while True:
            int_max = input("Set random int maximum value: ")
            if int_max.isdigit() and int(int_max) > int(int_min):
                self.random_int_max = int(int_max)
                break
            elif int_max.isdigit():
                print("max must be higher than min!")
            else:
                print("value must be in digit!")
        while True:
            float_min = input("Set random float minimum value: ")
            if float_min.isdigit():
                self.random_float_min = int(float_min)
                break
            else:
                print("value must be in digit!")
        while True:
            float_max = input("Set random float maximum value: ")
            if float_max.isdigit() and int(float_max) > int(float_min):
                self.random_float_max = int(float_max)
                break
            elif float_max.isdigit():
                print("max must be higher than min!")
            else:
                print("value must be in digit!")
        while True:
            float_round = input("Set random float round value: ")
            if float_round.isdigit():
                self.random_float_round = int(float_round)
                break
            else:
                print("value must be in digit!")
        self.update_random_values(how="push")
            
    def data_config(self):
        self.columns_length = Validation.input_column_length()
        self.rows_length = Validation.input_row_length()
                    
    def data_config_custom(self):
        self.data_config()
        self.column_custom_name()
        self.column_custom_type()
    
    def column_custom_name(self):
        self.custom_columns_name = []
        skip_custom_columns = False
        for i in range(self.columns_length):
            if not skip_custom_columns:
                column_name = input(f"Enter name for column no. {i} (s to skip the rest): ")
                #option if user want to randomize the rest of columns name
                if column_name.lower() == "s":
                    skip_custom_columns = True
                    self.custom_columns_name.append(self.randomizer(value_type="str"))
                    continue
                self.custom_columns_name.append(column_name)
            else:
                self.custom_columns_name.append(self.randomizer(value_type="str"))
    
    def column_custom_type(self):
        self.custom_columns_type = []
        skip_custom_type = False
        print("1. String\n2. Int\n3. Float\n4. Mixed")
        print("Enter s to skip the rest (the rest will be string type)")
        for i in range(self.columns_length):
            #input custom columns type
            if not skip_custom_type:
                column_type_index = input(f"Enter type for column {self.custom_columns_name[i]} by index: ")
                if column_type_index.lower() == "s":
                    skip_custom_type = True
                    self.custom_columns_type.append("str")
                elif Validation.check_input(column_type_index, 1, 4):
                    column_type_index = int(column_type_index)
                    if column_type_index == 1:
                        self.custom_columns_type.append("str")
                    elif column_type_index == 2:
                        self.custom_columns_type.append("int")
                    elif column_type_index == 3:
                        self.custom_columns_type.append("float")
                    elif column_type_index == 4:
                        self.custom_columns_type.append("mixed")
            else:
                self.custom_columns_type.append("str")
    
    def generate(self):
        self.data_config()
        #generate the dataset
        generated_columns = []
        self.generated_df = {}
        for column in range(self.columns_length):
            generated_columns.append(self.randomizer(value_type="str").upper())
            generated_rows = []
            for row in range(self.rows_length):
                generated_rows.append(self.randomizer(value_type="str"))
            self.generated_df[generated_columns[column]] = generated_rows
        data_io = DataIO(self.file_path, value_setting=False)
        data_io.save_dataframe(self.generated_df)
    
    def generate_custom(self):
        self.data_config_custom()
        self.generated_df = {}
        for column in range(self.columns_length):
            generated_rows = []
            custom_type = self.custom_columns_type[column]
            for row in range(self.rows_length):
                generated_rows.append(self.randomizer(value_type=custom_type))
            self.generated_df[self.custom_columns_name[column]] = generated_rows
        data_io = DataIO(self.file_path, value_setting=False)
        data_io.save_dataframe(self.generated_df)
    
    def start_generating(self, custom: bool):
        if not self.check_dataset():
            print("Cancelled!")
            return
        else:
            if custom:
                self.generate_custom()
            else:
                self.generate()
            print("Dataset generated successfully!")
    
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
        
    def randomizer(self, value_type: str):
        if value_type == "str":
            rand_string = "".join(random.choices(string.ascii_letters, k=self.random_str_length))
            return rand_string
        elif value_type == "int":
            rand_int = np.random.randint(self.random_int_min, self.random_int_max)
            return rand_int
        elif value_type == "float":
            rand_float = round(np.random.uniform(self.random_float_min, self.random_float_max), self.random_float_round)
            return rand_float
        elif value_type == "mixed":
            rand_value_type = random.choice(["str", "int", "float"])
            rand_mixed = self.randomizer(rand_value_type)
            return rand_mixed