class Node:
    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data


class dll:
    def __init__(self):
        self.head = Node(None, None, "This is head")
        self.tail = Node(None, None, "This is tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def pushFront(self, value):
        n = Node(None, None, value)
        n.next = self.head.next 
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n

    def __str__(self):
        retStr = ""
        n = self.head.next
        while n != self.head:
            retStr = str(n.data) + " "
            n = n.next
        return retStr

lis = dll()
lis.pushFront(1)
lis.pushFront(2)
print(lis)