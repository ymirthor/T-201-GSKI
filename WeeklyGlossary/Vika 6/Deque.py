class Que:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [0] * self.capacity
        self.begin = 0
        self.end = 0

    def __str__(self, index = 0):
        if self.size <= 0:
            return ""
        string = str(self.array[index])
        if index == self.size - 1:
            return str(self.array[index])
        return string + ", " + self.__str__(index + 1)

    def PushFront(self, value):
       self.array[self.end] = value
       self.size += 1
       self.end += 1

    def PushBack(self, value):
       self.array[self.end] = value
       self.size += 1
       self.end += 1
        
    def PopFront(self):
        retVal = self.array[self.begin]
        self.begin += 1
        self.size -= 1
        return retVal

    def PopBack(self):
        retVal = self.array[self.begin]
        self.begin += 1
        self.size -= 1
        return retVal

    # def resize(self):
    #     self.capacity *= 2
    #     temp_arr = [0] * self.capacity
    #     for i in range(self.size):
    #         temp_arr[i] = self.array[i]
    #     self.array = temp_arr

q = Que()
q.add(4)
q.add(5)
print(q)
q.remove()
print(q)