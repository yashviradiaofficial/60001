def is_even_with_return(i):
    """
    Input i, a positiv int
    Returns True if even, otherwise False.
    """

    print("with return")
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(i):
    """
    Input i, a positiv int
    Returns True if even, otherwise False.
    """

    print("without return")
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3))
