from core.utils import Validation
from core.generator import Generator

class MainMenu:
    def __init__(self, total_menu):
        self.running = True
        self.total_menu = total_menu
        
    def show_menu(self):
        print("Datasets Generator")
        print("< ---------------- >")
        print("1. Create randomized dataset")
        print("2. Create custom randomized dataset")
        print("3. Set random values")
        
    def handle_choice(self, index):
        if Validation.check_input(index, 1, self.total_menu):
            index = int(index)
            generator = Generator("data/data1.csv")
            if index == 1:
                generator.start_generating(custom=False)
            elif index == 2:
                generator.start_generating(custom=True)
            elif index == 3:
                generator.set_random_values()
            elif index == 4:
                generator.dataset_file_info()
        elif index.lower() == "q":
            self.exit()

    def run(self):
        while self.running:
            self.show_menu()
            index = input("Select by index (q for quit): ")
            self.handle_choice(index)
            print("< ------------------------ >")
    
    def exit(self):
        self.running = False
    
if __name__ == "__main__":
    app = MainMenu(4)
    app.run()