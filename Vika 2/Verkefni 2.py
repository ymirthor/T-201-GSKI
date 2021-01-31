import random
# Time copmlexity: O(n)
def power(first, second):
    return_value = 1
    for i in range(second):
        return_value *= first
    return return_value

# Time complexity O(n)
def Multiplication_of_positive_integers(first, second):
    return_value = 0
    for i in range(second):
        return_value += first
    return return_value

# Time copmlexity O(n)
def Random_number_insertion(size):
    lis = [0] * size
    for i in range(size):
        lis[i] = random.randint(1,6)
    return lis

# Time complexity O(n)
def print_list(lis):
    for i, x in enumerate(lis):
        if i == len(lis) - 1:
            print(x)
        else:
            print(x, end=", ")

# Time complexity O(1)
def random_index(lis):
    lis_size = len(lis)
    rand_num = random.randint(0, lis_size - 1)
    lis[rand_num] += 1
    print(lis)

# Time complexity O(1)
def switch_location(lis, loc):
    if loc + 1 >= len(lis) or loc < 0:
        return lis
    lis[loc+1], lis[loc] = lis[loc], lis[loc+1]
    print(lis)  

# Time copmlexity O(n)
def ordered_inserstion(lis):
    for element in lis:
        if num <= element:
            if num <= element:
                lis.insert(lis.index(element), num)
                break
        elif num > lis[-1]:
            lis.append(num)
            break            

def main():
    lis = Random_number_insertion(6)
    print_list(lis)
    #print(Multiplication_of_positive_integers(4, 4))
    #print(power(4,4))
    print(lis)
    #random_index(lis)
    switch_location(lis, 3)

main()