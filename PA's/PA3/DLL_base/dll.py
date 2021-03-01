class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        if self.data != None:
            return str(self.data)
        return str(None)

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.size = 0
        self.reversed = False
    
    def __str__(self):
        string = ""
        curr = self.first_in_list()
        while curr is not self.tail:
            string += str(curr) + " "
            curr = self._next(curr)
        return string

    def __len__(self):
        return self.size
    
    def _next(self, node):
        """ Helper function to check next even if reversed """
        return node.prev if self.reversed else node.next

    def _prev(self, node):
        """ Helper function to check previous even if reversed """
        return node.next if self.reversed else node.prev

    def _insert_between(self, value, p, n):
        """ Helper function to insert node between two others """
        self.size += 1
        new = Node(value, p, n)
        p.next = new
        n.prev = new
        return new

    def _remove(self, target):
        """ Helper function to remove node from list """
        self.size -= 1
        target.prev.next = target.next
        target.next.prev = target.prev
        return target.data

    def reset_current(self):
        self.curr = self.first_in_list()

    def first_in_list(self):
        return self._next(self.head)

    def last_in_list(self):
        return self._prev(self.tail)

    def is_empty(self):
        if self.size == 0:
            if self.reversed:
                self.reverse()
            return True
        return False

    def insert(self, value):
        if self.reversed:
            self._insert_between(value, self.curr, self.curr.next)
        else:
            self._insert_between(value, self.curr.prev, self.curr)
        self.curr = self._prev(self.curr)
        
    def remove(self):
        if self.is_empty():
            return    
        elif self.curr is self.tail or self.curr is self.head:
            return
        
        self.curr = self._next(self.curr)
        return self._remove(self._prev(self.curr))

    def get_value(self):
        return str(self.curr)

    def move_to_next(self):
        if self.is_empty():
            return
        if not self.curr is self.tail:
            self.curr = self._next(self.curr)
        return self.curr
    
    def move_to_prev(self):
        if self.is_empty():
            return
        if not self.curr is self.first_in_list():
            self.curr = self._prev(self.curr)
        return self.curr

    def move_to_pos(self, position):
        if position < 0 and position >= self.size:
            return
        curr = self.first_in_list()
        counter = 0
        while curr is not self._next(self.tail):
            if counter == position:
                self.index = position
                self.curr = curr
                return
            counter += 1
            curr = self._next(curr)

    def remove_all(self, value):
        if self.is_empty():
            return 
        curr = self.first_in_list()
        while curr is not self.tail:
            if curr.data == value:
                self._remove(curr) 
            curr = self._next(curr)
        if self.curr.data == value:
            self.reset_current()

    def reverse(self):
        self.reversed = not self.reversed
        self.head, self.tail = self.tail, self.head
        self.reset_current()

    def sort(self):
        if self.reversed:
            self.reverse()
        if self.size < 2:
            self.reset_current()
            return
    
        # Quicksort
        self.quicksort(self.first_in_list(), self.last_in_list())
        
        # Insertion sort
        # self.insertion_sort()
        
        self.reset_current()

    def insertion_sort(self):
        frwd = self.head.next
        while frwd is not self.tail:
            bwrd = frwd
            while bwrd is not self.head.next:
                if bwrd.prev.data > bwrd.data:
                    self.switch_data(bwrd.prev, bwrd)
                bwrd = bwrd.prev
            frwd = frwd.next

    def quicksort(self, first, last):
        middle = first

        if first.data == None or \
            last.data == None or \
            first == last or \
            first == last.next: # Base case, if size is 1
            return
      
        # Sorts list so all less than middle data is to the left
        mover = first.next
        while mover != last.next:
            if mover.data <= middle.data:
                self.switch_data(mover, middle)
            mover = mover.next
        
        # Recursive step through left and right side of middle
        return self.quicksort(first, middle.prev), \
               self.quicksort(middle.next, last)

    def switch_data(self, node1, node2):
        node1.data, node2.data = node2.data, node1.data

    
if __name__ == "__main__":
    dll = DLL()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    dll.insert(5)
    dll.insert(6)
    print(dll)
    dll.sort()
    print(dll)
