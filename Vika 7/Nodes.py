class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        if str(self.data):
            return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        ret = []
        node = self.head
        while node:
            ret.append(str(node))
            node = node.next
        return "[" + ', '.join(ret) + "]"

    def push_back(self, data):
        new_node = Node(data)
        if self.head == None: #Is the list empty?
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node



def push_front(head, data):
    new_node = Node(data, head)
    return new_node

listinn = LinkedList()
for i in range(1, 6):
    listinn.push_back("string " + str(i))

print(listinn)

# head = Node()
# head.data = "string 1"
# for i in range(2, 6):
#     head = push_front(head, "string " + str(i))

# node = head
# while node != None:
#     print(node.data)
#     node = node.next
