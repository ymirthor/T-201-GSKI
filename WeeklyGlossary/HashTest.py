from random import Random
class Key:
    def __init__(self, int_value, str_value):
        self.i = int_value
        self.s = str_value

    def __hash__(self):
        return self.i


if __name__ == "__main__":
    rand = Random()
    lis_size = 8
    lis = [0] * lis_size
    for i in range(100):
        key = Key(rand.randint(0, 100), "string")
        index = hash(key) % lis_size
        lis[index] += 1
        
    
    print(lis)
    