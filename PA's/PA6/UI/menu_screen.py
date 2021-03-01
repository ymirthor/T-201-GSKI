from UI.UI_base import UIBase

class MenuScreen(UIBase):
    def create_menu_screen(self, name, message, menu, commands):
        adjust_for_mainmenu = 1 if commands else 0
        start = (self.rows // 2) - ((len(menu) + 2 + adjust_for_mainmenu) // 2) - 2
        self.screen = self.header()
        self.screen += (" " * self.columns) + "\n"
        self.screen += "{:<{size}}\n".format(message, size=self.columns)
        self.screen += ((" " * self.columns) + "\n") * (start - 3)
        for i in name.split("\n"):
            self.screen += self.center_align(i, self.columns) + "\n"
        self.screen += (" " * self.columns) + "\n"
        
        size = 4
        longest = 0
        for _, value in menu:
            if len(value) > longest:
                longest = len(value)
        size += longest
        
        for idx, i in enumerate(menu):
            command = i[1]
            option = self.left_align("[{}] {}".format(idx + 1, command), size)
            self.screen += self.center_align(option, self.columns) + "\n"
        try:
            size = max([len(i) for _, i in commands]) + 4
        except ValueError:
            None
        
        for cmd, cmd_name in commands:
            cmd_formated = self.left_align("[{}] {}".format(cmd, cmd_name), size)
            self.screen += self.center_align(cmd_formated, self.columns) + "\n"
        
        self.screen = self.fill_window_with_empty(self.screen)
        
        return self.screen



