class Sll:
    class Node:
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next
        
        def __str__(self):
            if self.data == None:
                return
            else:
                return str(self.data)

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        curr = self.head
        str_out = ""
        while curr != None:
            str_out += str(curr) + " "
            curr = curr.next
        return str_out

    def push_front(self, value):
        self.size += 1
        self.head = self.Node(value, self.head)

    def push_back(self, value):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        new = self.Node(value)
        curr.next = new

    def pop_front(self):
        if not self.head:
            return None
        self.size -= 1
        popped = str(self.head)
        self.head = self.head.next
        return popped


lel = Sll()
lel.push_front("Anal")
lel.push_front("Beads")
lel.push_front("GOOD")
lel.push_front("YES")
lel.push_back("typpi")
lel.pop_front()
print(lel)