class Stack:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [0] * self.capacity

    def __str__(self, index = 0):
        if self.size <= 0:
            return ""
        string = str(self.array[index])
        if index == self.size - 1:
            return str(self.array[index])
        return string + ", " + self.__str__(index + 1)

    def push(self, value):
        if self.size == self.capacity:
            self.resize()
            self.push(value)
        else:
            self.array[self.size] = value
            self.size += 1
        
    def pop(self):
        pop = self.array[self.size -1]
        self.array[self.size - 1] = 0
        self.size -= 1
        return pop

    def resize(self):
        self.capacity *= 2
        temp_arr = [0] * self.capacity
        for i in range(self.size):
            temp_arr[i] = self.array[i]
        self.array = temp_arr


stack = Stack()
stack.push(3)
stack.push(4)
stack.push(1)
print(stack.pop())
print(stack)