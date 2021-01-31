class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] == None or self._table[j] == ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        firstAvial = None
        while True:
            if self._is_available(j):
                if firstAvial == None:
                    firstAvial = j
                if self._table[j] == None:
                    return (False, firstAvial)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1) % len(self._table)

    def _bucket_getitme(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_setitme(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

    