class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, level = 0):
        data_str = input()
        if data_str == "":
            return None
        level += 1
        print(level*"  |" + "- LEFT:", end=" ")
        left = self._populate_tree_recur(level)
        print(level*"  |" + "-RIGHT:", end=" ")
        right = self._populate_tree_recur(level)
        return BinaryTreeNode(data_str, left, right)

    def populate_tree(self):
        print("ROOT:", end=" ")
        self.root = self._populate_tree_recur()

    def _print_tree_recur(self, node, post=None):
        if node == None:
            return
        if not post:
            print(str(node.data), end=" ")
        self._print_tree_recur(node.left)
        self._print_tree_recur(node.right)
        if post:
            print(str(node.data), end=" ")

    def print_tree(self):
        print("Pre order")
        self._print_tree_recur(self.root)
        print()
    
    def print_postorder(self):
        print("Post order")
        self._print_tree_recur(self.root, True)
        print()

if __name__ == "__main__":
    tree = BinaryTree()
    tree.populate_tree()
    tree.print_tree()
    tree.print_postorder()