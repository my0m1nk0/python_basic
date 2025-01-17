#Calculator 

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
op = input("Enter Operator: ")
result = ""
if op == "+":
    result = first_number + second_number
else: 
    result = "WRONG OPERATOR"
  
print("Result is: ", result)