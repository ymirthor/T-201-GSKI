from mutablemapping import *

class MapBase(MutableMapping):
    class _Item:
        __slots__ = "_k", "_d"

        def __init__(self, key, data = None):
                self._k = key
                self._d = data

        def __hash__(self):
            if type(self._k) in [int, float]: 
                if type(self._k) == float:
                    self._k *= 10000000000
                    self._k = int(self._k)
                return self._k

            ret_val = 0
            mask = (1 << 32) - 1
            for char in self._k:
                ret_val = (ret_val << 5 & mask) | (ret_val >> 27)
                ret_val += ord(char)
            return ret_val
