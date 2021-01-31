from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, datastructure = "array"):
        if datastructure == "array":
            self.datastructure = ArrayDeque()
        else:
            self.datastructure = LinkedList()

    def push(self, value):
        self.datastructure.push_front(value)

    def pop(self):
        return self.datastructure.pop_front()

    def get_size(self):
        return self.datastructure.get_size()