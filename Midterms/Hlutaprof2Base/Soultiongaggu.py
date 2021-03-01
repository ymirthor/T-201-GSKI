class Sll:
    class SLL_Node:
        # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
        # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next
        def __str__(self):
            ret_str = ""
            node = self
            while node != None:
                ret_str += str(node.data) + " "
                node = node.next
            return ret_str

    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
            return ret_str

    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, value):
        self.size += 1
        self.head = self.SLL_Node(value, self.head)

class DLL_List:
    pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":
    lol = Sll()
    lol.push_front(4)
    print(lol)
    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    # print("Singly-linked node example:")
    # head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    # print(str(head))
