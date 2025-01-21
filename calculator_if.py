# PRINT Enter First Nubmer ? :
# READ first_number

# PRINT Enter Operator ? : *
# READ operator  = "*"

# PRINT Enter Second Number ? :
# READ second_number
# output = true 

# If operator is + then 
#   result = first_number + second_number
# Else if operator is - then
#   result = first_number - second_number
# Else if operator is * then 
#   result = first_number * second_number
# Else if operator is / then 
#   result = first_number / second_number
# Else 
#   PRINT "Invalid operator"
#   output = false

# If output is true then 
#   PRINT result
# Comment 

first_number = input("Enter First Number : ")
operator= input("Enter Operator (+ , - , * , /) : ")
second_number = input("Enter Second Number : ")

try: 
    #change to int
    first = int(first_number)
    second = int(second_number)
    output = True

    if operator == "+":
        result = first + second
    elif operator == "-": 
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/" :
        result = first / second
    else: 
        print("Invalid Operator") 
        output = False   

    if output == True: 
        print("Result : ", result)

except ValueError:
    print("Invalid input")