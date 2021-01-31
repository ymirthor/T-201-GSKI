from mapbase import *

class Bucket(MapBase):
    # -------------- _Node nested Sub Class --------------
    class _Node:
        def __init__(self, item = None, next = None):
            self._i = item
            self._n = next
    
    # -------------- Initialization of Class --------------
    def __init__(self):
        self._h = self._Node()
        self.length = 0
            
    # ----------------- Helper functions -----------------
    def __iter__(self):
        curr = self._h._n
        while curr != None:
            yield curr
            curr = curr._n
    
    def __str__(self):
        r = "{"
        empty = True
        for node in iter(self):
            empty = False
            key = node._i._k
            data = node._i._d
            if type(key) == str:
                key = "'" + key + "'"
            if type(data) == str:
                data = "'" + data + "'"
            r += "{}: {}, ".format(str(key), str(data))
        if not empty:
            r = r[:-2]
        return r + "}"

    def _find_item(self, key, prev_node = False):
        prev = self._h
        for curr in iter(self):
            if curr._i._k == key:
                return curr._i if not prev_node else prev
            prev = curr
        raise NotFoundException()

    # -------------- ABC' required functions --------------
    def __setitem__(self, key, data):
        try:
            self._find_item(key)._d = data
            return None
        except NotFoundException:
            item = self._Item(key, data)
            new_node = self._Node(item, self._h._n)
            self._h._n = new_node
            self.length += 1

    def __getitem__(self, key):
        return self._find_item(key)._d

    def __delitem__(self, key):
        prev = self._find_item(key, prev_node = True)
        prev._n = prev._n._n
        self.length -= 1
