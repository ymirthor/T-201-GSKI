from UI.UI_base import UIBase

class PopupScreen(UIBase):
    def popup_line(self, border, width, middle):
        return border + self.center_align(middle, width - 2) + border

    def popup(self, message, yes_no):
        if yes_no:
            message.append("[Y] Yes / [N] No")
        
        width = max([len(i) for i in message]) + 4
        height = len(message) + 4

        line = self.popup_line("+", width, "-" * (width - 2))
        empty = self.popup_line("|", width, " " * (width - 2))
        popup_messages = []
        
        for message in message:
            popup_messages.append(self.popup_line("|", width, message))

        popup = "\n" * (self.rows // 2 - height // 2)
        popup += self.center_align(line, self.columns) + "\n"
        popup += self.center_align(empty, self.columns) + "\n"

        for message in popup_messages:
            popup += self.center_align(message, self.columns) + "\n"
        popup += self.center_align(empty, self.columns) + "\n"

        popup += self.center_align(line, self.columns) + "\n"
        return self.fill_window_with_empty(popup)

    def overlay_popup(self, screen, popup):
        self.clear_screen()
        ret, popup = ret, popup = screen.split("\n"), popup.split("\n")
        x_start = x_end = None
        for idx, line in enumerate(popup):
            if not line == "":
                if not x_start:
                    x_size = [i for i in range(len(line) - 1) if line[i] != " "]
                    x_start, x_end = x_size[0], x_size[-1] + 1
                new = ret[idx][:x_start] + popup[idx][x_start:x_end] + ret[idx][x_end:]
                ret[idx] = new
        return "\n".join(ret)

if __name__ == "__main__":
    PopupScreen().popup(["Invalid","input!"], False)