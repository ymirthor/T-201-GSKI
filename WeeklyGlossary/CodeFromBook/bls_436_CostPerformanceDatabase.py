from bls_430_SortedTableMap import *

class CostPerformanceDatabase:
    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        return self._M.find_le(c)

    def add(self, c, p):
        other = self._M.find_le(c)
        if other != None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_gt(c)
        while other != None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)

if __name__ == "__main__":
    cpd = CostPerformanceDatabase()
    print(cpd.best(2000))
    cpd.add(1995, 70)
    cpd.add(9995, 99)
    print(cpd.best(1995))
    print(cpd.best(9995))
    # keys = [print(x) for x in iter(cpd._M)]
