"""def mult_iter(a, b):
    for a in range(a, b+1):
        result = 0
        result += a
        print(result)

print(mult_iter(4, 4))"""

# iterative solution
"""def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(4, 4))"""

# recursive solution
"""def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, (b-1))

print(mult(4, 4))"""

# factorial of the number
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))

def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

print(fact_iter(5))
