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
    
    def get_size(self):
        return self.size

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
        lel = str(self.head)
        self.head = self.head.next
        return lel

    def pop_back(self):
        if not self.head:
            return None
        curr = self.head
        self.size -= 1
        while curr.next.next != None:
            curr = curr.next
        popped = curr.data
        curr.next = None
        return popped




if __name__ == "__main__":
    lol = Sll()
    lol.push_front("KOMDU")
    lol.push_front("ÝMIR")
    lol.push_back("ANAL")
    lol.push_back("ANAL")
    lol.push_back("ÞETTA")
    lol.push_back("ANAL")
    lol.pop_back()
    print(lol)
