class LRCNode:
    __slots__ = "_l", "_r", "_c", "_d"
    def __init__(self, left=None, right=None, center=None, data=None):
            self._l = left
            self._r = right
            self._c = center
            self._d = data

class LRCMap:
    __slots__ = "_r"
    
    def __init__(self, build = False):
        self._r = LRCNode()
        if build:
            self.build_tree()
    
    def build_tree_recur(self, n, l):
        if l >= 0:
            left = self.build_tree_recur(LRCNode(), l-1)
            right = self.build_tree_recur(LRCNode(), l-1)
            center = self.build_tree_recur(LRCNode(), l-1)
            return LRCNode(left, right, center)
            
    def build_tree(self):
        levels = 8
        self._r = self.build_tree_recur(self._r, levels)

    def _next_node(self, node, cmd, get_data):
        if cmd == "l":
            if not node._l:
                if get_data:
                    return
                node._l = LRCNode()
            return node._l
            
        elif cmd == "r":
            if not node._r:
                if get_data:
                    return
                node._r = LRCNode()
            return node._r
        
        elif cmd == "c":
            if not node._c:
                if get_data:
                    return
                node._c = LRCNode()
            return node._c
        
        return LRCNode()
            

    def _travel(self, key, get_data=False):
        curr = self._r
        for cmd in key:
            curr = self._next_node(curr, cmd, get_data)
            if curr == None:
                return None
        return curr

    def put_data(self, key, data):
        self._travel(key)._d = data

    def get_data(self, key):
        ret = self._travel(key, True)
        if ret == None:
            return
        else:
            return ret._d

if __name__ == "__main__":

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))
