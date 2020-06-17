def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers.
    Returns: a list containing L1[i]/ L2[i]"""
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))  # nan = not a number
        except:
            raise ValueError('get_ratios called with bad args.')
    return ratios

L1 = [2, 34, 21, 45, 54]
L2 = [21, 25, 23, 25, 44]
print(get_ratios(L1, L2))
