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

def is_ordered(head):
    if head is None: # If empty return True
        return True
    elif head.next is None:
        return head.data
    # Comperes all items in the list and returns True if they are in a desending or asending order
    return head.data > is_ordered(head.next) or head.data < is_ordered(head.next)

class DLL_List:
    class DLL_Node:
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.DLL_Node("Head")
        self.tail = self.DLL_Node("Tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = self.tail

    def _insert(self, val, p, n): # Helper function for inserting between
        new_node = self.DLL_Node(val, p, n)
        p.next = new_node
        n.prev = new_node
        
    def build_list(self, lis):
        for x in lis:
            self._insert(x, self.current.prev, self.current)

    def _next(self, node, bool): # Helper function for iterating correct way trough list
        return node.prev if bool else node.next

    def print(self, backwards = False):
        # chooses first in list or last in list dependent on what way is wished to print
        curr = self._next(self.head, backwards) if not backwards else self._next(self.tail, backwards)
        while self._next(curr, backwards) != None:
            print(curr.data, end = " ")
            curr = self._next(curr, backwards)
        print()
    
        
    def contains(self, val):
        curr = self.head.next
        while curr.next != None:
            if curr.data == val:
                return True
            curr = curr.next
        return False
        
# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
    print(is_ordered(SLL_Node(1, SLL_Node(2, SLL_Node(3)))))
    print(is_ordered(SLL_Node(3, SLL_Node(2, SLL_Node(1)))))
    print(is_ordered(SLL_Node(1, SLL_Node(3, SLL_Node(2)))))

    my_dll = DLL_List()
    my_dll.build_list([2,6,3,6,2,8,9])
    my_dll.print()
    my_dll.print(True)
    print("6:" + str(my_dll.contains(6)) + "7:" + str(my_dll.contains(7)))