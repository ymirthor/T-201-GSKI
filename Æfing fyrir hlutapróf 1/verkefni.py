class æfing:
    def __init__(self):
        self.size = 0
        self.array = [0] * 100

    def __str__(self, index = 0): # :)
        if self.size == 0:
            return ""
        string = str(self.array[index])
        if index == self.size - 1:
            return str(self.array[index])
        return string + ", " + self.__str__(index + 1)

    def append(self, value):
        self.array[self.size] = value
        self.size += 1
    
    def prepend(self, value):
        temp = self.array[0]
        for i in range(self.size):
            temp2 = self.array[i + 1]
            self.array[i + 1] = temp
            temp = temp2
        self.array[0] = value
        self.size += 1
    
    def insert(self, value, index):
        temp = self.array[index]
        for i in range(index, self.size):
            temp2 = self.array[i + 1]
            self.array[i + 1] = temp
            temp = temp2
        self.array[index] = value
        self.size += 1

    def sorted_insersition(self, value):
        for i in range(self.size):
            if self.array[i - 1] <= value <= self.array[i]:
                return self.insert(value, self.array[i - 1])
        self.size += 1

    def remove_at(self, index):
        for i in range(index, self.size -1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
    
    def remove_value(self, value):
        for i in range(self.size):
            if value == self.array[i]:
                self.remove_at(self.array[i])



arr_lis = æfing()
arr_lis.append(2)
arr_lis.prepend(1)
arr_lis.append(3)
arr_lis.append(4)
arr_lis.append(6)
arr_lis.append(7)
arr_lis.remove_at(2)
arr_lis.remove_value(7)
arr_lis.sorted_insersition(7)
print(str(arr_lis))
