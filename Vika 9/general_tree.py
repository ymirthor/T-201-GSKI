class GeneralTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []
    
    def __str__(self):
        return str(self.data)

class GeneralTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, level=0, number=1):
        data_str = input()
        if data_str == "":
            return None
        level += 1
        node = GeneralTreeNode(data_str)
        while True:
            print(level*"  |" + "--Nr.{:2}:".format(number), end=" ")
            child_node = self._populate_tree_recur(level, number)
            if child_node == None:
                number = 0
                break
            number += 1
            node.children.append(child_node)
        return node

    def populate_tree(self):
        print("ROOT :", end=" ")
        self.root = self._populate_tree_recur()

    def _print_tree_recur(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        for child_node in node.children:
            self._print_tree_recur(child_node)

    def print_tree(self):
        self._print_tree_recur(self.root)
        print()

if __name__ == "__main__":
    tree = GeneralTree()
    tree.populate_tree()
    tree.print_tree()