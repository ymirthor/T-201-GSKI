from UI.UI_base import UIBase

class ListScreen(UIBase):
    def __init__(self):
        self.clear_screen()
        self.words = list() #BST()
    
    def create_list_screen(self, name, alist, commands, page, total_pages):
        start = (self.rows // 2) - ((len(alist) + 2) // 2) - 2
        self.screen = self.header()
        self.screen += (" " * self.columns) + "\n"
        self.screen += (" " * self.columns) + "\n"
        self.screen += ((" " * self.columns) + "\n") * (start - 3)
        self.screen += self.center_align(name, self.columns) + "\n"
        self.screen += (" " * self.columns) + "\n"
        
        size = 4
        longest = 0
        for _, value in alist:
            if len(str(value)) > longest:
                longest = len(str(value))
        size += longest

        for idx, i in enumerate(alist):
            command = i[1]
            option = self.left_align("[{}] {}".format(idx + 1, command), size)
            self.screen += self.center_align(option, self.columns) + "\n"
        
        if alist == []:
            self.screen += self.center_align("Nothing to display", self.columns)

        pagenr = self.left_align("Page {}/{}".format(page + 1, total_pages + 1), size)
        self.screen += self.center_align(pagenr, self.columns) + "\n"
        
        cmds_formated = " ".join(["[{}] {}".format(cmd, cmd_name) for cmd, cmd_name in commands])      
        self.screen += self.center_align(cmds_formated, self.columns) + "\n"

        self.screen = self.fill_window_with_empty(self.screen)

        return self.screen