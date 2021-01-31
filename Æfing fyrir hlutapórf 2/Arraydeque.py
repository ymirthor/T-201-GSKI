class Arraydeque:

    def __init__(self):
        self.capacity = 4
        self.array = [0] * self.capacity
        self.size = 0
        self.start = 0
        self.end = 0
    
    def __str__(self):
        ret_str = ""
        walk = self.start
        for i in range(self.size):
            ret_str += str(self.array[walk]) + " "
            walk = (walk + 1) % (self.capacity)
        return ret_str

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity

    def get_end(self):
        self.end = ((self.start + self.size) % self.capacity) - 1

    def get_size(self):
        return self.size

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize(False)
        self.size += 1
        self.array[self.get_end()] = value
            

    def push_front(self, value):
        if self.size == self.capacity:
            self.resize(True)
        else:
            self.start = (self.start - 1) % self.capacity
        self.size += 1
        self.array[self.start] = value


    def pop_back(self):
        if self.is_empty():
            return
        ret_val = self.array[self.get_end()]
        self.array[self.get_end()] = 0
        self.size -= 1
        return ret_val
        


    def pop_front(self):
        pass

    def get_size(self):
        pass

    def resize(self, pushFront = False):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        if not pushFront:
            start = 0
        else:
            start = 1
        end = self.size if not pushFront else self.size + 1
        walk = self.start
        for i in range(start, end):
            new_arr[i] = self.array[walk]
            walk = (walk + 1) % self.size
        self.array = new_arr
        self.start = 0

    
if __name__ == "__main__":
    lol = Arraydeque()
    lol.push_front("REND")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    lol.push_front("ANAL")
    print(lol)