class LinkedList:
    class _Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def __str__(self):
            if self.data:
                return str(self.data)
            return ""

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self, curr="get_head", ):
        if curr == "get_head":
            curr = self.head
        if not curr:
            return ""
        else:
            return str(curr) + " " + self.__str__(curr.next)

    def push_back(self, value, curr="get_head"):
        if curr == "get_head":
            curr = self.head
        if not self.head:
            self.size += 1
            self.head = self._Node(value, None)
        elif not curr.next:
            self.size += 1
            curr.next = self._Node(value, None)
        else:
            return self.push_back(value, curr.next)

    def push_front(self, value):
        self.size += 1
        self.head = self._Node(value, self.head)

    def pop_front(self):
        if not self.head:
            return None
        self.size -= 1
        popped = self.head.data
        self.head = self.head.next
        return popped
        
    def get_size(self, curr="get_head"):
        return self.size

if __name__ == "__main__":
    print("\nTESTING LINKED_LIST\n")

    lis = LinkedList()
    lis.push_back(3)
    lis.push_back(1)
    lis.push_back(6)
    lis.push_back(9)
    print("container of size: " + str(lis.get_size()) + ":")
    print(lis)
    print(lis.pop_front())
    print(lis.pop_front())
    print("container of size: " + str(lis.get_size()) + ":")
    print(lis)
    lis.push_front(11)
    lis.push_front(16)
    lis.push_front(13)
    print("container of size: " + str(lis.get_size()) + ":")
    print(lis)
    print(lis.pop_front())
    print(lis.pop_front())
    print(lis.pop_front())
    print(lis.pop_front())
    print("container of size: " + str(lis.get_size()) + ":")
    print(lis)
    print(lis.pop_front())
    print(lis.pop_front())
    print("container of size: " + str(lis.get_size()) + ":")
    print(lis)