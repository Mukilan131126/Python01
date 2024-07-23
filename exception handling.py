#Exception handling:

#1.Reciprocal the number:

try:
    num=float(input("Enter a number"))
    reciprocal=1/num
    print(f"The reciprocal of {number} is {reciprocal}")
except ZeroDivisionError:
    print("Error: cannot divide by zero")
