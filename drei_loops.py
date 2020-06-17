s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print('There is an i or u')
    else:
        print("There's no i or u")
        break

for char in s:
    if char == 'i' or char == 'u':
        print("There's an i or u.")
