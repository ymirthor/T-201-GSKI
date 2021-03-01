class ItemExistsException(Exception):
    pass
class NotFoundException(Exception):
    pass

class Hash:
    pass

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def _insert(self, key, value):
        self.length += 1
        new_node = Node(MyHashableKey(key, value), self.head.next)
        self.head.next = new_node

    def insert(self, key, value):
        if self.contains(key):
            raise ItemExistsException()
        self._insert(key, value)
        
    def update(self, key, value):
        data = self._find_node(key).data
        data.k = key
        data.v = value
    
    def nodes(self):
        def _nodes(node):
            if node != None:
                yield node
                yield from _nodes(node.next)
        for node in _nodes(self.head.next):
            yield node
    
    def _find_node(self, key):
        for node in self.nodes():
            if node.data.k == key:
                return node
        raise NotFoundException()
    
    def find(self, key):
        return self._find_node(key).data.v

    def contains(self, key):
        try:
            if self._find_node(key):
                return True
        except NotFoundException:
            return False

    def remove(self, key):
        for node in self.nodes():
            if node.next.data.k == key:
                node.next = node.next.next
                return
        raise NotFoundException()

    def __setitem__(self, key, value):
        try:
            self._find_node(key).data.v = value
        except NotFoundException:
            self._insert(key, value)
    
    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.length

    def __str__(self):
        ret_str = ""
        for node in self.nodes():
            ret_str += "{}:{}\n".format(node.data.k, node.data.v)
        return ret_str[:-1] 

class HashMap:
    def __init__(self):
        self.size = 4
        self.bucket_list = [Bucket() for _ in range(self.size)]
        self.length = 0

    def _get_bucket(self, key):
        new_entry = MyHashableKey(key, None)
        hashing_val = hash(new_entry)
        idx = hashing_val % self.size
        return self.bucket_list[idx]

    def insert(self, key, value):
        new_entry = MyHashableKey(key, value)
        self._get_bucket(key).insert(key, value)
        self.length += 1

    def update(self, key, value):
        self._get_bucket(key)._find_node(key).data.v = value

    def find(self, key):
        return self._get_bucket(key).find(key)

    def contains(self, key):
        return self._get_bucket(key).contains(key)

    def remove(self, key):
        self._get_bucket(key).remove(key)

    def __setitem__(self, key, value):
        try:
            self._get_bucket(key)._find_node(key).data.v = value
        except NotFoundException:
            self.insert(key, value)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.length

    def __str__(self):
        ret_str = ""
        for i in self.bucket_list:
            ret_str += "{}, ".format(i.length)
        ret_str += "\n"
        return ret_str

class MyHashableKey:
    def __init__(self, key, value):
        self.k = key
        self.v = value

    def __eq__(self, other):
        return self.k == other.k and self.v == other.v

    def __hash__(self):
        if type(self.k) == str:
            return sum([ord(x) for x in self.k])
        return int(self.k)

if __name__ == "__main__":
    m = Bucket()
    m.insert(3, "þristur")
    m.insert(2, "tvistur")
    m.insert(1, "ás")
    m.update(2, "Tvissari")
    print(m.find(2))
    print(m[2])
    myhash = MyHashableKey(1, "ba")
    print(hash(myhash))
    myhash = MyHashableKey(1, "ab")
    print(hash(myhash))