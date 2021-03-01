class Deque:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [0] * self.capacity
        self.begin = 0
        self.end = 0


    def __str__(self, index = 0):
        retString = ""
        if self.size == 0:
            return "empty"
        if self.begin >= self.end:
            for i in range(self.begin, self.capacity):
                retString += str(self.array[i]) + ", "
            for i in range(0, self.end):
                retString += str(self.array[i]) + ", "
        else:
            for i in range(self.begin, self.end):
                retString += str(self.array[i]) + ", "
        return retString[:-2]
        

    def add(self, value):
        if self.end == self.capacity:
            self.end = 0
        if self.size == self.capacity:
            self.resize()
            self.add(value)
        else:
            self.array[self.end] = value
            self.size += 1
            self.end += 1
            
    def remove(self):
        if self.begin == self.capacity:
            self.begin = 0
        retVal = self.array[self.begin]
        self.begin += 1
        self.size -= 1
        return retVal

    def resize(self):
        newArr = [0] * self.capacity * 2
        counter = 0
        for i in range(self.begin, self.capacity):
            newArr[counter] = self.array[i]
            counter += 1
        for i in range(0, self.end):
            newArr[counter] = self.array[i]
            counter += 1
        self.array = newArr
        self.capacity *= 2
        self.begin = 0
        self.end = self.size

def add(val):
    print('Adding: ',val)
    q.add(val)

q = Deque()
add(4)
print('Size: ',q.size)
print('Array: ',q.array)
q.remove()
add(5)
print('Size: ',q.size)
print('Array: ',q.array)

print(q)
add(4)
print('Size: ',q.size)
print('Array: ',q.array)

add(6)
print('Size: ',q.size)
print('Array: ',q.array)

add(8)
print('Size: ',q.size)
print('Array: ',q.array)

add(9)
print('Size: ',q.size)
print('Array: ',q.array)
q.remove()
print('Size: ',q.size)
print('Array: ',q.array)
print(q)
