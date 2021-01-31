from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, datastructure = "array"):
        if datastructure == "array":
            self.datastructure = ArrayDeque()
        else:
            self.datastructure = LinkedList()
    
    def add(self, value):
        self.datastructure.push_back(value)

    def remove(self):
        return self.datastructure.pop_front()
    
    def get_size(self):
        return self.datastructure.get_size()