def minus(first,second):
    return first - second

result = minus(10,5) #5
print("Result : ", result)

def calculate(first,second,operator):
    if operator == "-":
        return first - second
    elif operator == "+":
        return first + second
    elif operator == "*":
        return first * second # 50
    elif operator == "/":
        return first / second
    else:
        return "Invalid operator"

result = minus(10,5,"*") #50
print("Result : ", result)