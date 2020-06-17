try:
    a = int(input("Enter the value of a = "))
    b = int(input("Enter the value of b = "))
    print(a/b)
except:
    print("There's a bug in the input.")


try:
    a = int(input("Tell me one number = "))
    b = int(input("Tell me another number = "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Cannot divide the number with zero.")
except:
    print("something went terribly wrong.")
