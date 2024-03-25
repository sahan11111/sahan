# simple calculator using conditional statement

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("**Choose an Operator**\n")
print("Enter '1' for Addition")
print("Enter '2' for Subtraction")
print("Enter '3' for Multiplication")
print("Enter '4' for Division")

operator = int(input("Enter an operator: "))
if operator == 1:
    c = a + b
    print(f"The addition of {a} and {b} is {c}")
elif operator == 2:
    c = a - b
    print(f"The subtraction of {a} and {b} is {c}")
elif operator == 3:
    c = a * b
    print(f"The Multiplication of {a} and {b} is {c}")
elif operator == 4:
    if b==0:
     print("cannot divid by 0")
    else :
        c = a / b
    print(f"The division of {a} and {b} is {c}")
else :
    print("invalid operator")
    