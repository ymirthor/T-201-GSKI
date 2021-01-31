from UI_API import UI_API
from LL_API import LL_API

class MenuScreen(UI_API, LL_API):
    def generate_menu_screen(self):
        if self.the_screen["name"] == "select":
            name = "Selected {}: ".format(self.list_name)
        else:
            name = self.the_screen["name"]
        message = self.add_to_name(self.the_screen["message"], self.total_guesses)
        name = self.add_to_name(name, self.selected_item)

        try:
            if self.the_screen["name"] == "select" and self.list_name == "user":
                name += "\nScore:" + str(self.get_score(self.selected_item))
        except AttributeError:
            None
        
        self.screen = self.get_menu_screen(
            name,
            message,
            self.the_screen["menu"],
            self.the_screen["commands"]
        )

    def menu_main(self):
        while True:
            self.generate_menu_screen()
            print(self.screen)

            uinput = input("Input: ")

            commands = [key.lower() for key,_ in self.the_screen["commands"]]
            cmd = self.check_input(
                uinput.lower(),
                commands,
                len(self.the_screen["menu"])
            )
            if cmd in self.exiting:
                return cmd
            
            try:
                exec(self.the_screen["update_int"])
                if uinput.isdigit():
                    if int(uinput) > 0:
                        exec(self.the_screen["update_int"] + " = int(uinput)")
                        return "b"
                else:
                    popup = self.get_popup_screen(["Enter in a", "positive number"])
                    print(self.overlay_popup(self.screen, popup))
                    uinput = input("Input: ")
                continue
            except KeyError:
                None
                
            if not cmd:
                popup = self.get_popup_screen(["Invalid input!"])
                print(self.overlay_popup(str(self.screen), popup))
                input()
                continue
            
            if cmd in commands:
                if cmd == "e":
                    self.generate_menu_screen()
                    print(self.screen)
                    edit = input("Edit: ")
                    self.edit_item(edit)
                    return "b"
                
                if cmd == "r":
                    self.remove_item()
                    return "b"

            return self.the_screen["menu"][int(uinput) - 1][0]
