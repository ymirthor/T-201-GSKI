def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    if a < b:
        return a
    else:
        return modulus(a - b, b)


def how_many(lis1, lis2, index = 0):
    if lis1 == []:
        return 0
    elif index == len(lis2):
        return how_many(lis1[:-1], lis2, 0)
    elif lis1[-1] == lis2[index]:
        return 1 + how_many(lis1[:-1], lis2, 0)
    else:
        index += 1
        return how_many(lis1, lis2, index)

# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])

 

if __name__ == "__main__":
    run_recursion_program()