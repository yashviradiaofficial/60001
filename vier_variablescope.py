# linear function
def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = int(input("Value of x = "))
z = f(x)

# quadratic function
def f(y):
    y = y**2 + 2*y + 10
    print('in f(y): y = ', y)
    return y

nums = int(input("Enter the value = "))
c = f(nums)
