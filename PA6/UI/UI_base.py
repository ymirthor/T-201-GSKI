import os

class UIBase:
    def __init__(self):
        self.clear_screen()
    
    def __str__(self):
        self.clear_screen()
        return self.screen

    def center_align(self, message, the_size):
        return "{:^{size}}".format(message, size = the_size)

    def left_align(self, message, the_size):
        return "{:<{size}}".format(message, size = the_size)

    def clear_screen(self):
        self.recalculate_screen()
        os.system('cls')

    def recalculate_screen(self):
        self.columns, self.rows = os.get_terminal_size()[0:2]
    
    def fill_window_with_empty(self, scr):
        rows = 0
        for char in scr:
            if char == "\n":
                rows += 1
        missing = self.rows - rows - 3
        scr += (" " * self.columns + "\n") * missing
        return scr
        
    def header(self):
        third = self.columns // 3
        left = "Ýmir's & Garðar's"
        middle = "Hangman"
        # middle = "Screen {}".format(self.get_screen())
        right = "[Q] Quit"
        return "{:<{size}}{:^{size}}{:>{size}}\n".format(left, middle, right, size=third)
        
    # def quit_program_message(self):
    #     self.clear_screen()
    #     endscr = self.pop_up("Thank you for", "playing our game")
    #     print(self.overlay_popup(endscr))
    #     self.quit_program()
