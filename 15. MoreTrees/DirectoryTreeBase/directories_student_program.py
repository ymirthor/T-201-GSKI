class TreeNode:
<<<<<<< HEAD
    def __init__(self, name = "", parent=None):
=======
    def __init__(self, name = "", parent = None):
>>>>>>> 47a9b219138f6da0595822db379313c1eb108336
        self.name = name
        # ADD STUFF HERE IF NEEDED
        self.children = []
        self.parent = parent
<<<<<<< HEAD
=======

>>>>>>> 47a9b219138f6da0595822db379313c1eb108336
        
    # ADD STUFF HERE IF NEEDED

# ADD STUFF HERE IF NEEDED

# IF YOU WANT TO PUT THIS ALL INTO A CLASS AND USE INSTANCE VARIABLES (self.xx) THAT IS OK

def run_commands_on_node(node):
    print("  current directory: " + node.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here

            node.children.append(TreeNode(command[1], node))
            # ADD STUFF HERE IF NEEDED
            node.children.append(TreeNode(command[1], node))

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + node.name)

            # ADD STUFF HERE IF NEEDED
            for child in node.children:
                print(child.name)

            for child in node.children:
                print(child.name)

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                if node.parent == None:
                    return
                else:
                    node = node.parent
                # "cd .." MEANS I WANT TO GO UP A FOLDER
                if node.parent:
                    node = node.parent
                else:
                    return # change if needed, but this should exit if you are in the root folder

            changed = False
            for child in node.children:
                if child.name == command[1]:
                    node = child
                    changed = True
                    break
            # ADD STUFF HERE IF NEEDED
<<<<<<< HEAD
            switch = False
            for child in node.children:
                if child.name == command[1]:
                    node = child
                    switch = True
                    break
            
            if not switch: # Change this to equivalent of "if folder not found":
=======

            if not changed == True: # Change this to equivalent of "if folder not found":
>>>>>>> 47a9b219138f6da0595822db379313c1eb108336
                print("  No folder with that name exists")

        else:
            print("  command not recognized")

        # ADD STUFF HERE IF NEEDED



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_node(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
