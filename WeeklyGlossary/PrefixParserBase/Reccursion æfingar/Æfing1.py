def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x - 1)

def bad_fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    return bad_fibonacci(x - 1) + bad_fibonacci(x - 2)


# 1 2 3 5 8 13 21 34

def how_many_digits(x):
    if x < 10:
        return 1
    else:
        return 1 + how_many_digits(x // 10)

def find_maximum(lis, m=0):
    if not lis:
        return m
    if lis[0] > m:
        m = lis[0]  
    return find_maximum(lis[1:], m)

def reccur_multiple(a, b):
    if b == 0:
        return 0
    else:
        return a + reccur_multiple(a, b -1)

def reccur_power(a, b):
    if b == 0:
        return 0
    else:
        return a * reccur_multiple(a, b-1)

def print_reccur(x):
    if x == 0:
        None
    else:
        print_reccur(x - 1)
        print(x)

def print_string(x, counter = 4):
    if counter == 0:
        None
    else:
        print_string(x, counter - 1)
        print(x[counter -1])

def print_string2(string):
    if string == "":
        pass
    else:
        print(string[0])
        print_string2(string[1:])
        print(string[0])

def check_if_prime(x, counter = 2):
    if counter == x:
        return True

    if x % counter == 0:
        return False

    return check_if_prime(x, counter + 1)


def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1) 

def natural_number(x):
    sting = ""
    if x == 0:
        pass

    else:
        sting = str(x)
        natural_number(x-1)
        print(sting, end=" ")


def sum_of_digits(x):
    if x == 0:
        return 0
    return x % 10 + sum_of_digits(x // 10)

def length_of_string(x):
    if x == "":
        return 0
    else:
        return 1 + length_of_string(x[1:])

def find_value(lis, x):
    if lis == []:
        return False
    
    if lis[0] == x:
        return True

    else:
        return find_value(lis[1:], x)

def count_instances(lis, x):
    if lis == []:
        return 0
    
    if lis[0] == x:
        return 1 + count_instances(lis[1:], x)

    else:
        return count_instances(lis[1:], x)


def any_dub(lis):
    if lis == []:
        return False
    
    if find_value(lis[1:], lis[0]) == True:
        return True

    else:
        return any_dub(lis[1:])


def remove_dub(lis1, lis2 = []):
    if lis1 == []:
        return lis2

    if lis1[0] in lis2:
        return remove_dub(lis1[1:], lis2)

    else:
        lis2.append(lis1[0])
        return remove_dub(lis1[1:], lis2)



def binary_search(lis, value, start, end):
    middle = start + ((end - start) // 2)

    if lis[middle] == value:
        return middle

    if lis[middle] < value:
        return binary_search(lis, value, middle + 1, end)
         
    else:
        return binary_search(lis, value, start, middle - 1)

def substring(lis, sublis, counter = 0):
    if len(sublis) == counter:
        return True
    
    if lis == "":
        return False

    if lis[0] == sublis[counter]:
        return substring(lis[1:], sublis, counter + 1)

    else:
        return substring(lis[1:], sublis)

def substring_kristo(substring, a_str):
    if substring == "":
        return True
    if a_str == "":
        return False
    if substring[0] == a_str[0]:
        return substring_kristo(substring[1:], a_str[1:])
    else:
        return substring_kristo(substring, a_str[1:])


def hash_hish(sting,sub_string, counter = 0):
    if counter == len(sub_string):
        return True

    if sub_string == "":
        return False

    if sub_string[0] == sting[counter]:
        return hash_hish(sting, sub_string[1:], counter + 1,)
    
    else:

        return hash_hish(sting, sub_string[1:])

def modulous(a, b, counter = 0):
    if a < b:
        return counter
    else:
        return modulous(a - b, b, counter + 1)

def multiply(a, b, counter = 1):
    if b == counter:
        return a
    else:
        return a - multiply(a, b, counter + 1)


def division(a, b):
    if b == 0:
        return True
    
    if b < 0:
        return False
    
    else:
        return a - (division(a, b - a))



def main():
    # print(sum(3))
    # print(bad_fibonacci(3))
    # print(how_many_digits(15105))
    # print(find_maximum([0,1,2,3,4,5]))
    # print(reccur_multiple(4, 3))
    # print(reccur_power(2,3))
    # print_reccur(10)
    # print_string2("Anal")
    # print(check_if_prime(18))
    # print(factorial(5))
    # natural_number(5)
    # print(sum_of_digits(254))   
    # print(length_of_string("Anal"))
    # print(find_value([3,4,5,6], 4))
    # print(count_instances([2,3,3,3,4,5,6,7], 3))
    # print(any_dub([1,2,3,4,5,6,7,7]))
    # print(remove_dub([2,3,3,4,5]))
    # print(binary_search([1,2,3,4,7,12,17,20], 20, 0, 8))
    # print(substring("gagnaskipan", "gagnas"))
    # print(substring_kristo("gagnaskipan", "gagnas"))
    # print(modulous(4, 2))
    # print(multiply(4, 2))
    print(division(4, 2))
main()