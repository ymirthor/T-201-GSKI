from UI.UI_base import UIBase

class GameScreen(UIBase):
    def __init__(self, hidden_word, guesses_left, guessed_letters, guessed_words, message):
        self.clear_screen()
        self.create_game_screen(hidden_word, guesses_left, guessed_letters, guessed_words, message)

    # ------------------------------------- Create graphic --------------------------------

    def left_side(self, hidden_word, guesses_left, guessed_letters, guessed_words, message):
        size = self.columns // 2
        
        empty = self.center_align(" " * self.columns, self.columns) + "\n"
        self.screen += empty
        self.screen += empty
        
        game = self.center_align("Hidden word is: {}".format(hidden_word), size)
        self.screen += self.left_align(game, self.columns) + "\n"
        
        self.screen += empty
        self.screen += empty

        guesses = self.left_align("Guesses left: {}".format(guesses_left), size)
        self.screen += self.left_align(guesses, self.columns) + "\n"
        
        self.screen += empty

        guessed_letters_str = self.left_align("Guessed letters:", size)
        self.screen += self.left_align(guessed_letters_str, self.columns) + "\n"
        letters = self.left_align(", ".join(guessed_letters), size)
        self.screen += self.left_align(letters, self.columns) + "\n"
        
        self.screen += empty

        guessed_words_str = self.left_align("Guessed words:", size)
        self.screen += self.left_align(guessed_words_str, self.columns) + "\n"
        words = self.left_align(", ".join(guessed_words), size)
        self.screen += self.left_align(words, self.columns) + "\n"
        self.screen += empty
        guess_info = self.center_align(message, size)
        self.screen += self.left_align(guess_info, self.columns) + "\n"


    def create_game_screen(self, hidden_word, guesses_left, guessed_letters, guessed_words, message):
        self.screen = self.header()
        self.left_side(hidden_word, guesses_left, guessed_letters, guessed_words, message)
        self.screen = self.fill_window_with_empty(self.screen)
        return self.screen
