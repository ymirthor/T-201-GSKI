from random import choice, seed, randint
from UI_API import UI_API
from LL_API import LL_API

class GameScreen(UI_API, LL_API):
    # ------------------------------------------ Logic ------------------------------------

    def finnished(self):
        state = "won" if self.won_game else  "lost"
        popup = self.get_popup_screen(["You have {} the game!".format(state), "The word was: {}".format(self.word)])
        print(self.overlay_popup(str(self.screen), popup))
        input()

        popup = self.get_popup_screen(["Play again?"], yes_no=True)
        print(self.overlay_popup(str(self.screen), popup))
        uinput = input("Input: ")
        if uinput in ["y", ""]:
            self.new_game()
        
    def get_guess(self):
        guess = input("Guess: ")

        if guess in ["Q", "B"]:
            popup = self.get_popup_screen(["Are you sure", "you want to exit?"], yes_no=True)
            print(self.overlay_popup(str(self.screen), popup))
            uinput = input("Input: ")
            if uinput in ["y", ""]:
                self.exit_game = True
            return
            

        guess = guess.lower()
        if guess == "":
            return ""
        
        if len(guess) == 1:
            ret_message = ""
            if guess in self.guesses_letters:
                self.guess_info = "Already guessed"
                return
            
            if guess in self.word.lower():
                self.won_game = True
                self.guess_info == "You got the correct word"

                self.guesses_letters.append(guess)
                
                for letter in self.word:
                    if letter.lower() not in self.guesses_letters:
                        self.won_game = False
                        self.guess_info = "Letter in word"
                        break
            else:
                self.guesses_letters.append(guess)
                self.tries += 1
                self.guess_info = "Letter not in word"

        else:
            if guess in self.guesses_words:
                self.guess_info = "Already guessed"
            self.guesses_words.append(guess)
            if self.word.lower() == guess:
                self.won_game = True
                self.guess_info = "You got the correct word"
            else:
                self.tries += 1
                self.guess_info = "Word {} is not correct".format(guess)
                
    def change_guesses(self):
        popup = self.get_popup_screen(["Change nr of guesses?"], yes_no=True)
        print(self.overlay_popup(str(self.screen), popup))
        uinput = input()
        if uinput in ["y", ""]:
            while True:
                popup = self.get_popup_screen(["Enter in number of guesses"])
                print(self.overlay_popup(str(self.screen), popup))
                uinput = input("Nr of guesses: ")
                if uinput.isdigit():
                    if int(uinput) >= 0:
                        self.total_guesses = int(uinput)
                        break
                popup = self.get_popup_screen(["Invalid input"])
                print(self.overlay_popup(str(self.screen), popup))
                input()
    
    def new_game(self):
        self.change_guesses()
        self.game_main()

    def game_loop(self):
        return (self.total_guesses - self.tries) > 0 and (self.won_game == False)

    def render_hidden_word(self):
        if self.won_game or (self.total_guesses - self.tries) == 0:
            self.hidden_word = self.word
            return
        self.hidden_word = ""
        for letter in self.word:
            if letter.lower() in self.guesses_letters:
                self.hidden_word += letter
            else:
                self.hidden_word += "-"

    def print_current_game_screen(self):
            self.screen = self.get_game_screen(
                self.hidden_word, 
                self.total_guesses - self.tries, 
                self.guesses_letters, 
                self.guesses_words,
                self.guess_info
            )
            print(self.screen)

    # -------------------------------------- Game screen -------------------------------------
    
    def game_main(self):
        seed(randint(0, 1_000_000))

        self.word = choice(self.words)

        self.guesses_words = []
        self.guesses_letters = []
        self.tries = 0

        self.guess_info = ""
        
        self.exit_game = False
        self.won_game = False
        self.screen = ""
        while self.game_loop():
            self.render_hidden_word()
            self.print_current_game_screen()
            self.get_guess()
            
            if self.exit_game == True:
                return self.total_guesses
        
        self.render_hidden_word()
        self.print_current_game_screen()
        self.finnished()
        return self.total_guesses

