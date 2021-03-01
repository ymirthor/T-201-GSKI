class Node:
    def __init__(self, data, prev=None, nex=None):
        self.data = data
        self.next = nex
        self.prev = prev
    def __str__(self):
        return str(self.data)
    
class DLL:
    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None)
        self.current = self.trailer
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0 
        self.is_reversed = False


    def __str__(self):
        string = ""
        next_node = self._next(self.header)
        while next_node != self.trailer:
            string += str(next_node.data) + " "
            next_node = self._next(next_node)

        return string


    def __len__(self):
        return self.size

    """Helper functions"""
    def _insert_between(self, value, previous, next_node):
        new = Node(value, previous, next_node)
        previous.next = new
        next_node.prev = new
        self.size += 1
        return new

    def _next(self, node):
        return node.prev if self.is_reversed else node.next
    
    def _prev(self, node):
        return node.next if self.is_reversed else node.prev

    def _remove(self,node):
        removed = node.data
        node.prev.next = node.next 
        node.next.prev = node.prev
        self.size -= 1
        return removed

    def _switch_nodes(self, walker):
        """You'll need to draw the connections in 
        order to understand this algorithm"""
        walker.prev.next = walker.next 
        walker.next = walker.next.next 
        walker.next.prev = walker
        walker.prev.next.prev = walker.prev
        walker.prev.next.next = walker 
        walker.prev = walker.prev.next

    """The end of helper functions"""
        
    def insert(self, value):
        if not self.is_reversed:
            self.current = self._insert_between(value, self.current.prev, self.current)
        else:
            self.current = self._insert_between(value, self.current, self.current.next)



    def remove(self):
        if self.current.data is self.trailer.data:
            return 

        if self.current is self.header:
            return

        if self.size == 0:
            return

        self.current = self._next(self.current)
        return self._remove(self._prev(self.current))

    def get_value(self):
        return self.current.data

    def move_to_next(self):
        if self.current == self.trailer:
            return 

        self.current = self._next(self.current)

    def move_to_prev(self):
        if self.current == self._next(self.header):
            return

        self.current = self._prev(self.current)

    def move_to_pos(self, position):
        if 0 > position or position > self.size:
            return
            
        walker = self._next(self.header)
        counter = 0
        while walker != self._next(self.trailer):
            if counter == position:
                self.current = walker
                return

            counter += 1
            walker = self._next(walker)


    def remove_all(self, value):
        walker = self._next(self.header) 
        while walker != self.trailer:
            if walker.data == value:
                self._remove(walker)
            if value == self.current.data:
                self.move_to_pos(0)
            walker = self._next(walker)
        if self.current.data == value:
            self.current = self._next(self.header)


    def reverse(self):
        self.header, self.trailer = self.trailer, self.header
        self.is_reversed = not self.is_reversed
        self.current = self._next(self.header)

    def sort(self):
        if self.is_reversed:
            self.reverse()
        
        if self.size < 2:
            self.move_to_pos(0)
            return

        walker = self.header.next

        while walker.next.data != None:
            if walker.data == None:
                break
            if walker.data > walker.next.data:
                self._switch_nodes(walker)
                walker = self.header.next
            else:
                walker = walker.next

        self.move_to_pos(0)

    def get_current(self):
        return self.current
        

if __name__ == "__main__":
    dll = DLL()

    dll.insert("A")
    dll.insert("D")
    dll.insert("H")
    dll.insert("V")
    dll.insert("K")
    dll.insert("B")
    dll.insert("A")
    dll.insert("A")
    dll.insert("A")
    dll.insert("B")
    dll.sort()
    dll.remove_all("A")
    print(dll)
    