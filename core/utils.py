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