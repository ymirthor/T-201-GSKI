# def count_values(lis): 
#     dictionary = {} 
#     for i in lis: 
#         if i in dictionary: 
#             dictionary[i] += 1 #counter for each element
#         else: 
#             dictionary[i] = 1 
  
#     for key, value in dictionary.items(): 
#         print("{}: {}".format(key, value)) 

# count_values(["Hekla","Hekla","Hekla","Hekla","Hekla","Garðar","Garðar","Garðar","Garðar", "Hommi","Hommi", "Saga"])


class ValueCounter:
    def __init__(self):
        self.dictionary = {}

    def set_items(self, lis):
        for i in lis: 
            if i in self.dictionary: 
                self.dictionary[i] += 1 #counter for each element
            else: 
                self.dictionary[i] = 1

    def print_count(self):
        for key, value in self.dictionary.items(): 
            print("{}: {}".format(key, value)) 


value_counter = ValueCounter()
value_counter.set_items(["Hekla","Hekla","Hekla","Hekla","Hekla","Garðar","Garðar","Garðar","Garðar", "Hommi","Hommi", "Saga"])
value_counter.print_count()