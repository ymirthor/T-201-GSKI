from UI_API import UI_API
from LL_API import LL_API

class ListScreen(UI_API, LL_API):
    def generate_list_screen(self, list_menu, page, total_pages):
        self.screen = self.get_list_screen(
            self.the_screen["name"].title() + " list",
            list_menu,
            self.the_screen["commands"],
            page,
            total_pages
        )

    def list_main(self):
        page = 0

        self.list_name = self.the_screen["name"]
        self.list = eval(self.the_screen["list"])
        self.file_name = self.the_screen["file_name"]
        displayed = self.list
        while True:
            if type(displayed[0]) == dict:
                displayed = [list(i.items())[0][0] for i in displayed]

            list_menu, total_pages = self.list_to_nav(page, displayed)
            self.generate_list_screen(list_menu, page, total_pages)
            print(self.screen)

            uinput = input("Input: ").lower()
            if not uinput:
                continue
            
            commands = [key.lower() for key,_ in self.the_screen["commands"]]
            cmd = self.check_input(
                uinput,
                commands,
                len(list_menu)
            )
            if cmd in self.exiting:
                return cmd
            
            if cmd in commands:
                if cmd == "n":
                    if page < total_pages:
                        page += 1
                    continue
                
                if cmd == "p":
                    if page > 0:
                        page -= 1
                    continue

                if cmd == "a":
                    self.generate_list_screen(list_menu, page, total_pages)
                    print(self.screen)
                    item = input("Input new {}: ".format(self.the_screen["name"]))
                    self.add_item(item)     
                    displayed = self.list   
                    continue
                if cmd == "s":
                    self.generate_list_screen(list_menu, page, total_pages)
                    print(self.screen)
                    search = input("Search: ")
                    displayed = self.search_items(search)
                    page = 0
                    continue
            self.selected_item = list_menu[int(uinput) - 1][1]
            return list_menu[int(uinput) - 1][0]
