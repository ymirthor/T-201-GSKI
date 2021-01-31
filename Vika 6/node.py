class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if str(self.data):
            return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        self.head = Node(data, self.head)

    def append(self, data):
        new = Node(data, None)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def remove_front(self):
        self.head = self.head.next

    def remove_last(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    

if __name__ == "__main__":
    n = LinkedList()
    n.prepend("H")
    print(n)
    n.prepend("H")
    print(n)
    n.prepend("E")
    print(n)
    n.prepend("K")
    print(n)
    n.append("LoL")
    print(n)
    n.remove_front()
    print(n)
    n.remove_last()
    print(n)