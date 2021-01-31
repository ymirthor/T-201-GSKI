from UI.list_screen import ListScreen
from UI.menu_screen import MenuScreen
from UI.game_screen import GameScreen
from UI.popup_screen import PopupScreen

class UI_API:
    def get_list_screen(self, *args):
        return ListScreen().create_list_screen(*args)

    def get_menu_screen(self, *args):
        return MenuScreen().create_menu_screen(*args)

    def get_game_screen(self, *args):
        return GameScreen(*args)

    def get_popup_screen(self, *args, yes_no = False):
        return PopupScreen().popup(*args, yes_no)

    def overlay_popup(self, *args):
        return PopupScreen().overlay_popup(*args)
        