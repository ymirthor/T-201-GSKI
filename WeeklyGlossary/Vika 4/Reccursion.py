def factorial(n):
    if n == 1 :
        return 1
    return factorial(n - 1) * n

print(factorial(5))

def power(base, exp):
    if exp == 0:
        return 1
    
    return base * power(base, exp-1)

print(power(5, 5))

def multiply(a, b):
    if b == 1:
        return 1
    return a + multiply(a, b-1) 

print(multiply(5, 5))

def natural_numbers(n):
    if n == 0:
        return 1
    natural_numbers(n-1)
    print(n, end = ", ")

natural_numbers(5)
print()

def sum_of_digits(x):
    if x//10 == 0:
        return x

    return x % 10 + sum_of_digits(x//10)

print(sum_of_digits(254))


def fibonacci(x):
    if x <= 1:
        return (x,0)
    else:
        (a, b) = fibonacci(x-1)
        return a+b, a

print(fibonacci(100))

def prefix_parser8