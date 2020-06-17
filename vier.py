def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise false.
    """

    #print("inside is_even")
    return i % 2 == 0

is_even(3)


print("All the numbers between 0 to 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
