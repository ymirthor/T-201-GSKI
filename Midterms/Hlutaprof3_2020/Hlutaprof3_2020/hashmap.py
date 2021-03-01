class Item:
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

class HashMap:
    def __init__(self):
        self.array_length = 16
        self.hash_table = [ [ ] for _ in range(self.array_length) ]
        self.item_count = 0

    def __setitem__(self, key, data): # overrides/updates if already there
        index = hash(key) % self.array_length
        item = Item(key, data)
        if not self[key]:
            self.item_count += 1
        self.hash_table[index].append(item)

    def __getitem__(self, key): # returns data - returns None if nothing there
        index = hash(key) % self.array_length
        for item in self.hash_table[index]:
            if item.key == key:
                return item.data
        return None

    def __len__(self):
        return self.item_count


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    # tm = LRCMap()
    # tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    # tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    # print(tm.get_data("lrl"))
    # print(tm.get_data("lrcclc"))
    # print(tm.get_data("lc"))

    # tm = LRCMap(True)
    # tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    # tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    # print(tm.get_data("lrlrcclc"))
    # print(tm.get_data("lrlclc"))
    # print(tm.get_data("lrlrccr"))


    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
