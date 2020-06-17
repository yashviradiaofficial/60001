#tuples, lists

t = (2, "mit", 3)
print(t)
print(t[0])
print(t[1:2])
print(len(t))


# quotient and remainder

def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return(q, r)
(quot, rem) = quotient_and_remainder(4, 5)
print((quot, rem))
