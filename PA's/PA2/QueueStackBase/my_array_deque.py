import random
class ArrayDeque:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity
        self.start = 0
        self.end = 0

    def __str__(self):
        retString = ""
        walk = self.start
        for i in range(self.size):
            retString += str(self.array[walk]) + " "
            walk = (walk + 1) % (self.capacity)
        return retString

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_end(self):
        self.end = ((self.start + self.size) % self.capacity) - 1
        return self.end

    def push_back(self, value):
        if self.is_full():
            self.resize()
        self.size += 1
        self.array[self.get_end()] = value
        
    def push_front(self, value):
        if self.is_full():
            self.resize(True)
        else:
            self.start = (self.start - 1) % self.capacity
        self.size += 1
        self.array[self.start] = value

    def pop_back(self):
        if self.is_empty():
            return
        retVal = self.array[self.get_end()]
        self.array[self.get_end()] = None
        self.size -= 1
        return retVal

    def pop_front(self):
        if self.is_empty():
            return
        retVal = self.array[self.start]
        self.array[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return retVal

    def get_size(self):
        return self.size

    def resize(self, push_front=False):
        self.capacity *= 2
        newArr = [None] * self.capacity
        if not push_front:
            start = 0
        else:
            start = 1
        end = self.size if not push_front else self.size + 1
        walk = self.start
        for i in range(start, end):
            newArr[i] = self.array[walk]
            walk = (walk + 1) % self.size  
        self.array = newArr
        self.start = 0

def print_details():
    print("Start:",q.start,"End:",q.end)
    print('Array:', q.array,'\n')
    print('Deque:',q)

def check_push_back(val, details=False):
    q.push_back(val)
    print('-- Pushing',val,'to the back of array--\nSize:',q.size)
    if details:
        print_details()
    else:
        print('Deque:',q)

def check_push_front(val, details=False):
    q.push_front(val)
    print('-- Pushing',val,'to the front array--\nSize:',q.size)
    if details:
        print_details()
    else:
        print('Deque:',q)

def check_pop_front(details=False):
    popped = q.pop_front()
    print('-- Removed',popped,'from the front of array--\nSize: ',q.size)
    if details:
        print_details()
    else:
        print('Deque:',q)

def check_pop_back(details=False):
    popped = q.pop_back()
    print('-- Removed',popped,'from the back of array--\nSize: ',q.size)
    if details:
        print_details()
    else:
        print('Deque:',q)

if __name__ == "__main__":
    t = True
    q = ArrayDeque()
    check_push_front(1, t)
    check_push_back(2, t)
    check_push_back(3, t)
    check_push_back(4, t)
    check_push_front(0, t)
    