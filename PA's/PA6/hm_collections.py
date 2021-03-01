class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        if self.data != None:
            return str(self.data)
        return str(None)

class BinarySearchTree:
    class BinaryTreeNode:
        def __init__(self, data = None, parent = None, left = None, right = None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
            
    def __init__(self):
        self.root = self.BinaryTreeNode()

    def inorder_recur(self, node):
        if node == None:
            return
        if node.left != None:
            for x in self.inorder_recur(node.left) :
                yield x
        yield node
        if node.right != None:
            for x in self.inorder_recur(node.right) :
                yield x

    def inorder(self):
        for node in self.inorder_recur(self.root):
            yield node.data.name

    def __str__(self):
        return "\n".join(map(str, self.inorder()))

    def add_recur(self, node, data):
        if node.data == None:
            node.data = data
            return

        if node.data.name >= data.name:
            if node.left == None:
                node.left = self.BinaryTreeNode(None, node)
            self.add_recur(node.left, data)
        else:
            if node.right == None:
                node.right = self.BinaryTreeNode(None, node)
            self.add_recur(node.right, data)

    def add(self, data):
        self.add_recur(self.root, data)

    def find_recur(self, node, name, ret=False):
        if node == None:
            return
        if node.data.name == name:
            return node
        
        if node.data.name >= name:
            ret = self.find_recur(node.left, name)
        else:
            ret = self.find_recur(node.right, name)
        return ret
        
    def find(self, name):
        if self.root.data == None:
            return False
        return self.find_recur(self.root, name)

    def remove(self, name):
        node = self.find(name)
        if node.left == None and node.right == None:
            if node == self.root:
                node.data = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
        
        elif node.left and node.right:
            delNode = node.right
            while delNode.left != None:
                delNode = delNode.left
            node.data = delNode.data
            if node.right == delNode:
                node.right = None
            else:
                delNode.parent.left = None
      
        elif node.left and node.right == None:
            if node == self.root:
                self.root = node
            else:
                new_parent = node.parent
                node.parent.left = node.left
                node.left.parent = new_parent
        
        elif node.right and node.left == None:
            if node == self.root:
                self.root = node
            else:
                new_parent = node.parent
                node.parent.right = node.right
                node.right.parent = new_parent


class Stack:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [0] * self.capacity
        self.sorted = True

    def prepend(self, value): 
        if self.size == self.capacity:
            self.resize()
        
        temp = self.array[0]
        for i in range(self.size):
            temp2 = self.array[i + 1]
            self.array[i + 1] = temp
            temp = temp2

        self.array[0] = value
        self.size += 1

    def pop_front(self):
        if self.size == self.capacity:
            self.resize()

        temp = self.array[0]
        self.array[0] = self.array[1]
        return temp

    def resize(self):
        self.capacity *= 2
        temp_arr = [0] * self.capacity
        for i in range(self.size):
            temp_arr[i] = self.array[i]
        self.array = temp_arr

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


class HashMap:
    pass