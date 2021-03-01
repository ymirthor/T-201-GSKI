class IndexOutOfBounds(Exception):
    pass
class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList():
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [0] * self.capacity
        self.sorted = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self, index = 0):
        if self.size <= 0:
            return ""
        string = str(self.array[index])
        if index == self.size - 1:
            return str(self.array[index])
        return string + ", " + self.__str__(index + 1)

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value): # :/
        if type(value) is int:
            if value > self.array[0]:
                self.sorted = False
        else:
            self.sorted = False
        
        if self.size == self.capacity:
            self.resize()
        
        temp = self.array[0]
        for i in range(self.size):
            temp2 = self.array[i + 1]
            self.array[i + 1] = temp
            temp = temp2

        self.array[0] = value
        self.size += 1
   
    def check_if_sorted(self, lis, target, index): # :)
        if index == 0 and target > lis[index]:
            self.sorted = False
        elif index == self.size and lis[index - 1] > target:
            self.sorted = False
        elif lis[index - 1] > target > lis[index]:
            self.sorted = False

    def insert(self, value, index):
        if index > self.size or index < 0:
            raise IndexOutOfBounds()

        if self.size == self.capacity:
            self.resize()
        
        if type(value) is int:
            if index == 0 and value > self.array[index]:
                self.sorted = False
            elif index == self.size and self.array[index - 1] > value:
                self.sorted = False
            elif self.array[index - 1] > value:
                self.sorted = False
            elif value > self.array[index]:
                self.sorted = False
        else:
            self.sorted = False

        if index == self.size:
            self.append(value)
        else:
            temp = self.array[index]
            for i in range(index, self.size):
                temp2 = self.array[i + 1]
                self.array[i + 1] = temp
                temp = temp2
            self.size += 1
            self.array[index] = value
    
    #Time complexity: O(1) - constant time
    def append(self, value):
        if type(value) is int:
            if value < self.array[self.size - 1]:
                self.sorted = False
        else:
            self.sorted = False
        
        if self.size >= self.capacity:
            self.resize()
        
        self.array[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index > self.size - 1:
            raise IndexOutOfBounds()

        if type(value) is int:
            self.check_if_sorted(self.array, value, index)
        else:
            self.sorted = False
        
        self.array[index] = value
       
    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if 0 <= index <= self.size - 1:
            return self.array[index]
        else:
            raise IndexOutOfBounds()
        
    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.array[self.size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *= 2
        temp_arr = [0] * self.capacity
        for i in range(self.size):
            temp_arr[i] = self.array[i]
        self.array = temp_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index > self.size -1:
            raise IndexOutOfBounds
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = 0
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        return self.__init__()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        if not self.sorted:
            raise NotOrdered
        else:
            if value < self.array[0]:
                return self.prepend(value)
            elif value > self.array[self.size - 1]:
                return self.append(value)
            self.binary_ordered(self.array, value, 0, self.size)
        
    def binary_ordered(self, lis, value, start, end):
        middle = (end + start) // 2
        if lis[middle - 1] <= value <= lis[middle]:
            return self.insert(value, middle)
        elif lis[middle] < value:
            return self.binary_ordered(lis, value, middle, end)
        else:
            return self.binary_ordered(lis, value, start, middle)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.sorted:
            return self.binary_search(self.array, value, 0, self.size - 1)
        else:
            return self.linear_search(self.array, value)
        
    def linear_search(self, lis, value, index = 0):
        if index == self.size: # Base Case
            raise NotFound()
        elif lis[index] == value:
            return index
        else:
            return self.linear_search(lis, value, index + 1)

    def binary_search(self, lis, value, start, end, insert=False):
        middle = start + ((end - start) // 2)
        if lis[end] < value or value < lis[start]:
            if insert:
                return middle
            else:
                raise NotFound()
        if lis[middle] == value: # Base Case
            return middle
        elif lis[middle] < value:
            return self.binary_search(lis, value, middle + 1, end)
        else:
            return self.binary_search(lis, value, start, middle - 1)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        if self.sorted:
            return self.remove_at(self.binary_search(self.array, value, 0, self.size - 1))
        else:
            return self.remove_at(self.linear_search(self.array, value))

    def sort(self):
        if not self.sorted:
            bubble_sort()
            self.sorted = True
    
    def bubble_sort()
        for i in range(self.size - 1):
            for j in range(0, self.size-i-1):
                if self.array[j] > self.array[j+1] :
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

    def quick_sort():
        pass
        
def check_sorted(arr_lis):
    print(arr_lis)
    if arr_lis.sorted:
        print("Array is sorted")
    else:
        print("Array is not sorted")

def find_in_list(arr_lis, target):
    print(arr_lis)
    print(target, "is located at index:", arr_lis.find(target))

if __name__ == "__main__":
    try:
        arr_lis = ArrayList()
        print(arr_lis)
        
       

    except IndexOutOfBounds:
        print("Index out of bounds!")

    except NotFound:
        print("Object not found!")

    except Empty:
        print("List is empty!")

    except NotOrdered:
        print("List not ordered!")
