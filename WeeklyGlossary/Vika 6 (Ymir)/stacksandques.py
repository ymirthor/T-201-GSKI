class Array():
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity

    def __str__(self, index = 0):
        if self.size == 0:
            return ""
        elif index >= self.size - 1:
            return str(self.array[index])
        else:
            return str(self.array[index]) + ", " + self.__str__(index + 1)

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] == self.array[i]
        self.array = new_array

class Stack(Array):
    def push(self, value):
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        pop = self.array[self.size - 1]
        self.array[self.size - 1] = 0
        self.size -= 1
        return pop

class Que():
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity
        self.start = 0
        self.end = 0
    
    def __str__(self, index = 0):
        if self.size == 0:
            return ""
        # print("Array: ",self.array)
        # print("Capacity: ", self.capacity)
        # print("End: ",self.end- 1)
        # print("Start: ",self.start)
        # print("Index: ", index + self.start)
        # print("Value: ", self.array[index + self.start])
        # input()
        if index + self.start == self.end - 1:
            return str(self.array[index + self.start])
        elif index + self.start == self.capacity - 1:
            return str(self.array[index + self.start]) + ", " + self.__str__(-self.start)
        else:
            return str(self.array[index + self.start]) + ", " + self.__str__(index + 1)

    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        
        elif self.end == self.capacity:
            self.end = 0
        
        self.array[self.end] = value
        self.end += 1
        self.size += 1
    
    def remove(self):
        if self.end == self.capacity:
            self.start = 0
        
        self.array[self.start] = 0
        self.start += 1
        self.size -= 1

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.start, self.size):
            print(self.array[i])
            new_array[i - self.start] = self.array[i]

        for i in range(self.start):
            print(self.array[i])
            new_array[i + self.size - 1] = self.array[i]

        self.start = 0
        self.end = self.size - 1
        self.array = new_array    
        

if __name__ == "__main__":
    # s = Stack()
    # print(s)
    # s.push(9)
    # print(s)
    # s.push(8)
    # print(s)
    # s.pop()
    # print(s)

    q = Que()
    # print(q)
    q.add(1)
    q.add(2)
    q.add(3)
    # print(q)
    q.remove()
    # print(q)
    q.add(4)
    # print(q)
    q.add(5)
    # print(q)
    q.add(6)
    # print(q)
    q.add(7)
    q.add(7)
    q.remove()
    print(q)
