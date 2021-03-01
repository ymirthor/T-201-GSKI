def length_of_string(string):
    if len(string) == 0:
        return 1

    return len(string)
    length_of_string(string[1:])

print(length_of_string("Hello world"))


def linear_search(lis, value):
    if lis == []:
        return False
    
    if lis[0] == value:
        return True
    return linear_search(lis[1:], value)
    


#print(linear_search([1,2,3], 2))

# def count_instances(lis, value):
#     if lis == []:
#         return 0
     
#     if lis[0] == value:
#         return 1 + count_instances(lis[1:], value)
#     return 0 + count_instances(lis[1:], value)
    

# print(count_instances([1,2,3,3,3,5], 6))

def check_dub(lis):
    if lis == []:
        return False
    
    if linear_search(lis[1:], lis[0]) == True:
        return True

    else:
        return check_dub(lis[1:])

                    

print(check_dub([1, 3, 3]))

