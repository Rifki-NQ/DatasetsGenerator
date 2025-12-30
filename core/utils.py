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

    @staticmethod
    def input_column_length() -> int:
        while True:
            columns_length = input("Select length of column: ")
            if columns_length.isdigit():
                columns_length = int(columns_length)
                return columns_length
            else:
                print("length of column must be digit!")
                
    @staticmethod
    def input_row_length() -> int:
        while True:
            rows_length = input("Select length of row: ")
            if rows_length.isdigit() and int(rows_length) > 0:
                rows_length = int(rows_length)
                return rows_length
            elif rows_length.isdigit():
                print("Length of row must be at least 1")
            else:
                print("Length of row must be digit!")

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
        
    def input_file_name(self):
        while True:
            filename = input("Enter file name for the generated dataset: ")
            if filename[-4:] != ".csv":
                print("file must be csv!")
                return False
            elif filename == "random_values_setting.csv":
                print("filename cannot be the same as random values setting!")
                return False
            else:
                self.file_path = f"data/{filename}"
        
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