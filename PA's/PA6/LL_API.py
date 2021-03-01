from IO_API import IO_API

class LL_API:
    def check_input(self, uinput, commands, length_of_menu):
        if uinput in commands or uinput == "q":
            return uinput

        if uinput.isdigit():
            if 1 <= int(uinput) <= length_of_menu:
                return int(uinput)
    
    def get_item(self, user):
        for item in self.users:
            user_, score = list(item.items())[0]
            if user == user_:
                return item
        
    def get_score(self, user):
        for item in self.users:
            user_, score = list(item.items())[0]
            if user == user_:
                return score

    def add_to_name(self, string, element):
        if string[-2:] == ": ":
            string += str(element)
        return string

    def list_to_nav(self, page, the_list):
        on_screen = 9
        
        total_pages = -1 * (-len(the_list) // on_screen) - 1
        nav = []
        for idx, word in enumerate(the_list):
            if page * on_screen <= idx < (page + 1) * on_screen:
                nav.append((self.the_screen["target"], word),)
        return nav, total_pages

    def edit_item(self, edit):
        self.list[self.list.index(self.selected_item)] = edit
        self.selected_word = edit
        IO_API().write_file(self.list, self.file_name)

    def add_item(self, item):
        if type(self.list[0]) == dict:
            self.list.append({item: 0})
        else:
            self.list.append(item)
        IO_API().write_file(self.list, self.file_name)

    def remove_item(self):
        if type(self.list[0]) == dict:
            
            self.list.remove(self.get_item(self.selected_item))
        else:
            self.list.remove(self.selected_item)
        IO_API().write_file(self.list, self.file_name)

    def search_items(self, search):
        alist = []
        for i in self.list:
            if type(i) == dict:
                i = list(i.items())[0][0]
            if search.lower() in i.lower():
                alist.append(i)
        return alist
