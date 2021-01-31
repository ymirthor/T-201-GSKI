"""
Autor: Ýmir Þórleifsson
Date: 30 Jan 2020
"""

# Part A
def count_values(lis):
    a_dict = {}
    for i in lis:
        if i not in a_dict:
            a_dict[i] = 1
        else:
            a_dict[i] += 1
    return print_dict(a_dict)

def print_dict(dic):
    string = ""
    for k, v in dic.items():
        string += "{}: {}\n".format(k,v)
    print(string)

# Part B
class ValueCounter():
    def __init__(self):
        self.counter = dict()
    
    def set_items(self, lis):
        a_dict = {}
        for i in lis:
            if i not in a_dict:
                a_dict[i] = 1
            else:
                a_dict[i] += 1
        self.counter = a_dict

    def print_count(self):
        string = ""
        for k, v in self.counter.items():
            string += "{}: {}\n".format(k,v)
        print(string)
    
if __name__ == "__main__":
    count_values(["a","b","a","d","c","d","c","c","f","b","a","a"])
    count_values([])
    value_counter = ValueCounter()
    value_counter.set_items(["a","b","a","d","c","d","c","c","f","b","a","a"])
    value_counter.print_count()