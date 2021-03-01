import random
class MyHashableKey:
    def __init__(self, int_value, str_value):
        self.i = int_value
        self.s = str_value

    def __eq__(self, other):
        return self.i == other.i and self.s == other.s

    def __hash__(self):                
        ret_val = 0
        mask = (1 << 32) - 1
        for char in self.s:
            ret_val = (ret_val << 5 & mask) | (ret_val >> 27)
            ret_val += ord(char)

        ret_val += self.i

        if ret_val < 0:
            ret_val *= -1
            ret_val += 1

        return ret_val + self.i

if __name__ == "__main__":
    length = 13
    table = [0 for _ in range(length)]
    hashes = []
    for i in range(length*1000):
        str_val = "".join([chr(random.randint(100,300)) for _ in range(5)])
        int_val = random.randint(0,100)

        a = hash(MyHashableKey(int_val, str_val))
        hashed = hash(MyHashableKey(int_val, str_val)) % length
        
        if a in hashes:
            print("Got same hash twice")
            break
        hashes.append(a)
        
        table[hashed] += 1
    print(table)

    assert hash(MyHashableKey(1, "ab")) != hash(MyHashableKey(-1, "ab"))