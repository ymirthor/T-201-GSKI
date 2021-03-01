import sys

class InvalidCommand(Exception):
    pass

class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.children = BinarySearchTree()

class BinarySearchTree:
    class BinaryTreeNode:
        def __init__(self, data = None, parent = None, left = None, right = None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
        
    def __init__(self):
        self.root = self.BinaryTreeNode()

    def inorder_recur(self, node):
        if node == None:
            return
        if node.left != None:
            for x in self.inorder_recur(node.left) :
                yield x
        yield node
        if node.right != None:
            for x in self.inorder_recur(node.right) :
                yield x

    def inorder(self):
        for node in self.inorder_recur(self.root):
            yield node.data.name

    def __str__(self):
        return "\n".join(map(str, self.inorder()))

    def add_recur(self, node, data):
        if node.data == None:
            node.data = data
            return

        if node.data.name >= data.name:
            if node.left == None:
                node.left = self.BinaryTreeNode(None, node)
            self.add_recur(node.left, data)
        else:
            if node.right == None:
                node.right = self.BinaryTreeNode(None, node)
            self.add_recur(node.right, data)

    def add(self, data):
        self.add_recur(self.root, data)

    def find_recur(self, node, name, ret=False):
        if node == None:
            return
        if node.data.name == name:
            return node
        
        if node.data.name >= name:
            ret = self.find_recur(node.left, name)
        else:
            ret = self.find_recur(node.right, name)
        return ret
        
    def find(self, name):
        if self.root.data == None:
            return False
        return self.find_recur(self.root, name)

    def remove(self, name):
        node = self.find(name)
        if node.left == None and node.right == None:
            if node == self.root:
                node.data = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
        
        elif node.left and node.right:
            delNode = node.right
            while delNode.left != None:
                delNode = delNode.left
            node.data = delNode.data
            if node.right == delNode:
                node.right = None
            else:
                delNode.parent.left = None
      
        elif node.left and node.right == None:
            if node == self.root:
                self.root = node
            else:
                new_parent = node.parent
                node.parent.left = node.left
                node.left.parent = new_parent
        
        elif node.right and node.left == None:
            if node == self.root:
                self.root = node
            else:
                new_parent = node.parent
                node.parent.right = node.right
                node.right.parent = new_parent

class Commands:
    def __init__(self, directory):
        self.directory = directory

    def mkdir(self, name):
        print("  Making subdirectory " + name)
        if self.directory.children.find(name) or name == "..":
            print("  Subdirectory with same name already in directory")
        else:
            self.directory.children.add(TreeNode(name, self.directory))

    def ls(self, name):
        print("  Listing the contents of current directory,  " + str(self.directory.name))
        if self.directory.children.root.data:
            print(self.directory.children)

    def cd(self, name):
        print("  switching to directory " + name)
        if name == "..":
            if self.directory.parent == None:
                print("Exiting directory program")
                return True
            else:
                self.directory = self.directory.parent
        else:
            if not self.directory.children.find(name):
                print("  No folder with that name exists")
            else:
                self.directory = self.directory.children.find(name).data
                
        print("  current directory: " + str(self.directory.name))

    def rm(self, name):
        print("  removing directory " + name)
        if self.directory.children.find(name):
            self.directory.children.remove(name)
            print("  directory successfully removed!")
        else:
            print("  No folder with that name exists")

def run_commands_on_tree(tree):
    cmds = Commands(tree)
    cmd_chooser = {"mkdir": cmds.mkdir,
                   "ls":     cmds.ls,
                   "cd":     cmds.cd,
                   "rm":     cmds.rm}
    exit = None

    print("  current directory: " + cmds.directory.name)
    while not exit:
        command = input().split()
        try:
            if not command:
                raise InvalidCommand()
            if command[0] == "ls":
                command.append("_") # To avoid Index Error for ls command
            if len(command) != 2:
                raise InvalidCommand()
            command, name = command
            if command not in cmd_chooser:
                raise InvalidCommand()
            
            exit = cmd_chooser[command](name)
        
        except InvalidCommand:
            print("  command not recognized")

def run_directories_program():
    run_commands_on_tree(TreeNode("root"))

def simple_test(safe=True):
    orig_stdin = sys.stdin
    fin = open(sys.path[0] + "/commands3.txt")
    sys.stdin = fin
    if safe:
        try:
            run_directories_program()
        except:
            print("Exiting directory program in a BAD way")
    else:
        run_directories_program()
    sys.stdin = orig_stdin

if __name__ == "__main__":
    # simple_test(False)
    run_directories_program()