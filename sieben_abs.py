def abs(x):
    """
    Assume x is an integer
    Returns x if x >= 0 otherwise -x"""

    if x < -1:
        return -x
    else:
        return x

print(abs(-56))
