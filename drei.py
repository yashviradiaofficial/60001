#know the length of the string
s = "abc"
print(len(s))

#index in the string
greet = 'hello'
print(greet[0])
print(greet[1])
print(greet[2])
print(greet[3])
print(greet[4])
print(greet[-1])
print(greet[-2])
print(greet[-3])
print(greet[-4])
print(greet[-5])

#slicing the string
s = 'abcdefgh'
print(s[3:6])
print(s[3:6:2])
print(s[::]) #same as s[0:len(s):0]
print(s[0:-1:])
print(s[::-1])
print(s[4:1:-2])

#reverse the string
script = "Das Essen und Trinken ist ein wichtigster Bestandteil der Gesundheit einer Nation."
print(script[::-1])

#strings are immutable
s = 'hello'
#s[0] = 'y' will give you an error, but you can concate
s = 'y' + s[1:len(s)]
print(s)
