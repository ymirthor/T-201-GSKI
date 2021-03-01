import random

# def power(a, b):
#     temp = 1
#     for i in range(b):
#         temp *= a
#     return temp


# print(power(2, 3))


# def multiple(a, b):
#     temp = 0
#     for i in range(b):
#         temp += a
#     return temp

# print(multiple(2, 3))

# def random_number(size):
#     lis = [0] * size
#     for i in range(size):
#         lis[i] = random.randint(1,6)
#     return lis

# print(random_number(4))

# def print_list(lis):
#     temp = ""
#     for i in lis:
#         if i != lis[-1]:
#             temp += str(i) + ", "
#         else:
#             temp += str(i)
#     return temp

# print(print_list([3,4,5,6,7]))

# def random_index(lis):
#     random_num = random.randint(0, len(lis) -1)
#     lis[random_num] += 1
#     return lis
    
# print(random_index([0,1,2,3,4,5]))
        

# def switch_location(lis, location):
#     temp = lis[location + 1]
#     lis[location + 1] = lis[location]
#     lis[location] = temp
#     return lis

# print(switch_location([1,2,3,4,5,6], 2))

def switch_location_random(lis):
    location1 = random.randint(0, len(lis) - 1)
    location2 = random.randint(0, len(lis) - 1)
    print(location1)
    print(location2)
    temp = lis[location1]
    lis[location1] = lis[location2]
    lis[location2] = temp
    return lis

print(switch_location_random([0,1,2,3,4,5]))



def ordered_inserstion(lis):
    for i in range(len(lis)):
        if num > lis[i]:
            if num < lis[i+1]:
                
