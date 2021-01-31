import sys

class GeneralTree:
    def __init__(self, data = "", children = []):
        self.data = data
        self.children = children

class AlphabetTree:
    def __init__(self):
        self.root = GeneralTree()
        self.root.children = [GeneralTree("b")]

    def add_word(self, word):
        current = self.root
        for letter in word:
            change = False 
            for child in current.children: # Move to node
                if letter == child.data[-1]:
                    current = child
                    change = True
            if not change: # Add node
                current.children.append(GeneralTree(current.data + letter))
                for child in current.children:
                    if child.data == (current.data + letter):
                        current = child
                        continue
    
    def print_all(self):
        print(self.root)
        for child in self.root.children:
            print(child.data)
            for c in child.children:
                print(c.data)

    def print_leaves(self):
        #TODO: Implement
        pass



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())
    
    tree.print_all()
    print("Gar[ar er hammi")
    tree.print_leaves()
    
    file.close()
