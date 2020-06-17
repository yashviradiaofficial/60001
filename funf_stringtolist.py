s = "I<3 cs"
print(list(s))
print(s.split("<"))

L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))

L = [9, 6, 0, 3]
L.sort()
print(L)
L.reverse()
print(L)

#cloning
cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(cool)
print(chill)

#sort and sorted
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cold = ['grey', 'green', 'blue']
sortedcold = sorted(cold)
print(cold)
print(sortedcold)
