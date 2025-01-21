start = False

while start == True:
    #0 -> 9
    value = input("Enter the number between 0 and 9 : ")

    try:
        res = int(value)
        if res > 9 : 
            print("Your value is over 9")
        elif res < 0 :
            print("Your value is under 0")
        else :
            print("Your value is ,", res)   
            start = False
    except ValueError:
        print(ValueError)    