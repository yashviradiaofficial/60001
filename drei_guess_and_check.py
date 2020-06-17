#But this is not the complete code and also not user friendly
"""cube = 8
for guess in range(cube + 1):
    if guess**3 == 8:
        print("Cube root of", cube, "is", guess)"""

#Here's a new code and also a proper one
cube = 8

for guess in range(abs(cube) + 1): #abs is absolute value
    if guess**3 >= abs(cube):
        break

if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube.')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+str(cube)+' is '+str(guess))
