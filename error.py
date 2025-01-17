first_number=input("Enter first number :")
second_number=input("Enter second number :")
try:
    first = int(first_number)
    second = int(second_number)
    sum = first + second
    print("Sum of ",first ,"and",second,"is",sum)
except ValueError:
    print("Enter Number Only!!")   