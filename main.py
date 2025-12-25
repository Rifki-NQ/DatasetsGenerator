from core.utils import Validation
from core.generator import Generator

class MainMenu:
    def __init__(self, total_menu):
        self.running = True
        self.total_menu = total_menu
        
    def show_menu(self):
        print("Datasets Generator")
        print("< ------------------------ >")
        print("1. Create randomized datasets")
        
    def handle_choice(self, index):
        if Validation.check_input(index, 1, self.total_menu):
            index = int(index)
            if index == 1:
                generator = Generator("data/data1.csv")
                generator.generate()
        elif index.lower() == "q":
            self.exit()

    def run(self):
        while self.running:
            self.show_menu()
            index = input("Select by index (q for quit): ")
            self.handle_choice(index)
    
    def exit(self):
        self.running = False
    
if __name__ == "__main__":
    app = MainMenu(1)
    app.run()