# Dæmi um O(1)
def big_o_of_one(value):
    return value * 5

#Dæmi um O(log(n))
def big_o_of_log_n(value):
    n = 1
    while n != value:
        n *= 2

#Dæmi um O(n)
def big_o_of_n(value, target):
    for _ in list:
        if _ == target:
            return True

# Dæmi um O(n^2)
def big_o_of_n_second(lis, lis2, target):
    for x in lis:
        for y in lis2:
            if y == target:
                return True

# Dæmi um O(n^3)
def big_o_of_n_third(lis, lis2, lis3, target):
    for x in lis:
        for y in lis2:
            for z in lis3:
                if z == target:
                    return True

# Dæmi um O(2^n)
def big_o_of_2_nth(value):
    