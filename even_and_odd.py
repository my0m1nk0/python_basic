# 1  is Odd
# 2  is Even
# 3  is Odd
# 4  is Even
# 5  is Odd

num = input("Enter Number : ")
try:
    user_number = int(num)
    for i in range(user_number):
        j = i + 1
        if(j % 2 == 0):
            print(j,"is Even.")
        else:
            print(j, "is Odd.")        
except ValueError:
    print("Enter Number Only!")    