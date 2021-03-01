from random import choice
from random import randint
class DoublyDeque:
    class _Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def __str__(self):
            if self.data != None:
                return str(self.data)
            return ""
    
    def __init__(self):
        self.head = self._Node("Head")
        self.tail = self._Node("Tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __str__(self):
        string = ""
        curr = self.head.next
        while curr.next != None:
            string += str(curr) + " "
            curr = curr.next
        return string

    def _insert_between(self, value, p, n):
        new = self._Node(value, p, n)
        p.next = new
        n.prev = new

    def _remove(self, target):
        target.prev.next = target.next
        target.next.prev = target.prev
        target = str(target)
        return target

    def push_back(self, value):
        self.size += 1
        self._insert_between(value, self.tail.prev, self.tail)
        
    def push_front(self, value):
        self.size += 1
        self._insert_between(value, self.head, self.head.next)
        
    def pop_back(self):
        if self.size == 0:
            return None
        
        self.size -= 1
        return self._remove(self.tail.prev)
    
    def pop_front(self):
        if self.size == 0:
            return None
        
        self.size -= 1
        return self._remove(self.head.next)

    def get_size(self):
        return self.size

if __name__ == "__main__":
    d = DoublyDeque()
    for i in range(1000):
        x = randint(0,3)
        num = randint(0,9)
        if x == 0:
            print("Numer:",num)
            print("Push Back")
            d.push_back(num)
            print(d)   
        elif x == 1:
            print("Numer:",num)
            print("Push Front")
            d.push_front(num)
            print(d)
        elif x == 2:
            print("Pop Back")
            d.pop_back()
            print(d)
        else:
            print("Pop Front")
            d.pop_front()
            print(d)
    
    # a.push_front("A")
    # a.push_front("B")
    # a.push_front("C")
    # a.push_back("B")
    # a.push_back("C")
    # a.push_back("D")
    # a.push_back("B")
    # print(a)
    # a.pop_front()
    # a.pop_front()
    # print(a)
   
    # deque = ArrayDeque()
    # deque.push_back(3)
    # deque.push_back(1)
    # deque.push_back(6)
    # deque.push_back(9)
    # print("container of size: " + str(deque.get_size()) + ":")
    # print(deque)
    # print(deque.pop_back())
    # print(deque.pop_back())
    # print("container of size: " + str(deque.get_size()) + ":")
    # print(deque)
    # deque.push_front(11)
    # deque.push_front(16)
    # deque.push_front(13)
    # print("container of size: " + str(deque.get_size()) + ":")
    # print(deque)
    # print(deque.pop_front())
    # print(deque.pop_front())
    # print(deque.pop_front())
    # print("container of size: " + str(deque.get_size()) + ":")
    # print(deque)
    # print(deque.pop_front())
    # print(deque.pop_back())
    # print(deque.pop_front())
    # print(deque.pop_back())
    # print("container of size: " + str(deque.get_size()) + ":")
    # print(deque)
