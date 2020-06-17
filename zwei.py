'''hi = "hello there"
name = " yash"

greet = hi + name

print(greet)

name = "yash"
greeting = hi + " " + name
print(greeting)

silly = hi + (" " + name)*3
print(silly)


x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
print("my fav number is" + x_str + "." + "x=" + x_str)

# taking input from the user
text = input("type anything... ")
print(5*text)
num = int(input("type anything... "))
print(5*num)


#branching
x = float(input("Enter the number for x: "))
y = float(input("Enter the number for y: "))
if x == y:
    print("x and y are equal.")
    if y != 0:
        print("Therefore, x/y is", x/y)
elif x < y:
    print("x is smaller than y.")
else:
    print("y is smaller than x.")
print("thanks!")'''

#iteration: legend of zelda
'''n = input("You are lost in the forest \n **************** \n **************** \n :)")
while n == right or n == left:
    input("You are lost in the forest \n **************** \n **************** \n :)")
print("thanks for playing the game")'''

"""mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

nums = []
for i in range(0, 11, 2):
    print(f"Adding {i} to the nums.")
    nums.append(i)

for i in nums:
    print(f"nums was: {i}")

print(nums)"""

###########
# using the range
###########
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)
