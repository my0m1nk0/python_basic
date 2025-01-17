first_number=input("Enter first number :")
second_number=input("Enter second number :")
try:
    first = int(first_number)
    second = int(second_number)
    if second <= 0:
        print("Second number must be greater than zero")   
    else:
        divide = first / second
        print("Divide of ",first ,"and",second,"is",divide)
except ValueError:
    print("Enter Number Only!!")   