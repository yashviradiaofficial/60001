#lists
L = [2, 'a', 4, [1, 2]]
print(len(L))
print(L[2] + 1)
L.append(5)
print(L)
L.extend([21, 25])
print(L)

list = [2, 1, 3, 6, 3, 7, 0]
list.remove(2)
list.remove(3)
del(list[1])
list.pop()
print(list)
