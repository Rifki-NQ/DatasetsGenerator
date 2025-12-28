import pandas as pd

class Validation:
    @staticmethod
    def check_input(value: int, min_value: int, max_value: int):
        if value.isdigit() and min_value <= int(value) <= max_value:
            return True
        elif value.isdigit():
            print("Invalid inputted index!")
            return False
        else:
            print("Inputted index must be in digit!")
            return False

class DataIO:
    def __init__(self, file_path, value_setting: bool):
        self.file_path = file_path
        self.value_setting = value_setting
        self.value_setting_headers = [
            "random_str_length",
            "random_int_min",
            "random_int_max",
            "random_float_min",
            "random_float_max",
            "random_float_round"
        ]
        
    def save_dataframe(self, df):
        df = pd.DataFrame(df)
        df.to_csv(self.file_path, index=False)
        
    def read_data(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError as e:
            print(f"failed to read {e.filename} because the file is missing!")
            self.create_new_file()
            return None
        except pd.errors.EmptyDataError as e:
            print(f"failed to read {self.file_path} because the file is empty!")
            print("please input new random values")
            return None
        
    def check_random_values_headers(self):
        df = self.read_data()
        if self.value_setting and df.columns.tolist() != self.value_setting_headers:
            print("invalid headers detected, please input new random values")
            return True
        return False
    
    def create_new_file(self):
        df = pd.DataFrame(columns=self.value_setting_headers)
        df.to_csv(self.file_path)
        print(f"new file {self.file_path} created!")