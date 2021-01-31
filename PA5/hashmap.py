from bucket import *

class HashMap(Bucket):
    # -------------- Initialization of Class --------------
    def __init__(self):
        self.size = 13
        self.table = [Bucket() for i in range(self.size)]
        self.length = 0

    # ----------------- Helper function -----------------
    def __iter__(self):
        for bucket in self.table:
            for node in iter(bucket):
                yield node._i

    def __str__(self):
        ret_str = ""
        for idx, i in enumerate(self.table):
            ret_str += "{:>2} {}\n".format(idx, str(i))
        return ret_str

    def _resize(self):
        old = self.table[:]
        length = self.length
        self.table = [Bucket() for i in range(self.size)]
        for bucket in old:
            for node in bucket:
                key = node._i._k
                data = node._i._d
                self[key] = data
        self.length = length

    def _hash(self, key):
        return hash(self._Item(key)) % self.size

    # -------------- ABC' required functions --------------
    def __setitem__(self, key, data):
        i = self._hash(key)
        l1 = len(self.table[i])
        self.table[i][key] = data
        l2 = len(self.table[i])
        if l1 != l2:
            self.length += 1

        if len(self) / len(self.table) > 0.5:
            self.size = 2 * len(self.table) - 1
            self._resize()

    def __getitem__(self, key):
        i = self._hash(key)
        return self.table[i][key]

    def __delitem__(self, key):
        i = self._hash(key)
        del self.table[i][key]
        self.length -= 1

if __name__ == "__main__":
    m = HashMap()
    m.insert(1, "einn")
    m.insert(1.0, "as")
    m.insert("ab", "abb")
    m.insert("ba", "baa")
    m.insert("random", "rand")
    m.insert(12, "tolf")
    m.insert(13, "threttan")

    m.update(13, "thirteen")

    print(m.find(13))
    print(m.contains(13))
    m.remove(13)

    m[5] = "fimm"

    print(m[5])


    print(m)

    print(len(m))

    m1 = HashMap()
    import random
    for i in range(7):
        key = "".join([chr(random.randint(20, 120)) for i in range(6)])
        m1[key] = i

    for i, bucket in enumerate(m1.table):
        print("{:>2}: {:}".format(i, len(bucket)))

    print(len(m1))
