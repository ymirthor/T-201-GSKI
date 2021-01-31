import sys

class InvalidCommand(Exception):
    pass

class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.children = list()
    
    def in_children(self, name):
        for child in self.children:
            if child.name == name:
                return True
        return False
    
    def add_child(self, name):
        if len(self.children) == 0:
            self.children.append(TreeNode(name, self))

        elif len(self.children) == 1:
            if self.children[0].name < name:
                self.children.append(TreeNode(name, self))
            else:
                self.children.insert(0, TreeNode(name, self)) 
        
        for i in range(len(self.children) - 1):
            if name < self.children[0].name:
                self.children.insert(i, TreeNode(name, self))
                return

            elif name > self.children[len(self.children) - 1].name:
                self.children.append(TreeNode(name, self))
                return

            child = self.children[i].name
            next_child = self.children[i + 1].name
            if child < name < next_child:
                self.children.insert(i + 1, TreeNode(name, self))

    def rm_child(self, name):
        for child in self.children:
            if child.name == name:
                self.children.remove(child)
                return

class Commands:
    def __init__(self, directory):
        self.directory = directory

    def mkdir(self, name):
        print("  Making subdirectory " + name)
        if self.directory.in_children(name):
            print("  Subdirectory with same name already in directory")
        else:
            self.directory.add_child(name)
            

    def ls(self, name):
        print("  Listing the contents of current directory,  " + str(self.directory.name))
        if self.directory.children:
            for child in self.directory.children:
                print(child.name)

    def cd(self, name):
        print("  switching to directory " + name)
        if name == "..":
            if self.directory.parent == None:
                print("Exiting directory program")
                return True
            else:
                self.directory = self.directory.parent
        else:
            if self.directory.in_children(name):
                for child in self.directory.children:
                    if child.name == name:
                        self.directory = child
            else:
                print("  No folder with that name exists")

        print("  current directory: " + str(self.directory.name))

    def rm(self, name):
        print("  removing directory " + name)
        if self.directory.in_children(name):
            self.directory.rm_child(name)
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
                raise InvalidCommand
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
    fin = open(sys.path[0] + "/commands.txt")
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
    simple_test(False)
    # run_directories_program()