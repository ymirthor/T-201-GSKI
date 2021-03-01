from GameScreen import GameScreen
from ListScreen import ListScreen
from MenuScreen import MenuScreen
from UI_API import UI_API
from IO_API import IO_API
from screens import SCREENS

from collections import deque

class HangmanMain(ListScreen, MenuScreen, GameScreen):
    def __init__(self):
        self.words = IO_API().read_file("words.txt")
        self.users = IO_API().read_file("users.txt")
        self.high_scores = self.get_highscore()

        self.screen_history = deque()
        self.screen_history.append(1)
        self.id = 1
        self.the_screen = SCREENS[self.id]

        self.selected_item = ""
        self.total_guesses = 10

        self.run_screen = {
            0: self.menu_main,
            1: self.list_main,
            2: self.game_main
            }

        self.exiting = {
            "b": self.back,
            "q": self.quit_program
        }
        self.screen = ""
    
    def get_highscore(self):
        scores = []
        for user in self.users:

            user, score = list(user.items())[0]
            scores.append((user, int(score)),)
        scores = sorted(scores)
        scores = sorted(scores, reverse=True, key=lambda k: k[1])[0:9]
        return ["{}: {}".format(k, v) for k, v in scores]

    def quit_program(self):
        popup = UI_API().get_popup_screen(["Are your sure?"], yes_no=True)
        print(UI_API().overlay_popup(str(self.screen), popup))
        uinput = input()
        if uinput in ["y", "q", ""]:
            self.screen_history.clear()

    def back(self):
        self.screen_history.pop()

    def get_screen(self):
        try:
            self.id = self.screen_history.pop()
            self.screen_history.append(self.id)
            self.the_screen = SCREENS[self.id]
            return self.id
        except IndexError:
            return None

    def main(self):
        while self.get_screen() != None:
            screen = SCREENS[self.id]
            the_type = screen["type"]
            id = self.run_screen[the_type]()

            if the_type == 2:
                self.back()
                continue
            
            if id in self.exiting:
                self.exiting[id]()

            elif id == None:
                popup = UI_API().get_popup_screen(["Invalid input!"])
                print(UI_API().overlay_popup(str(self.screen), popup))
                input()

            else:
                self.screen_history.append(id)

        popup = UI_API().get_popup_screen(["Thank you for", "playing our game"])
        print(UI_API().overlay_popup(str(self.screen), popup))

if __name__ == "__main__":
    hangman = HangmanMain()
    hangman.main()