list = [1,5,2,7,8,9,200,155,100,1000] #immutable
list2 = (1,5,2,7,8,9,200,155,100,1000) #mutable
# [0,1,2,3,4,5,6,7,8,9]
# range(10)

arr_len = len(list) - 1
print("Array Length : ", list[arr_len])
for i in range(arr_len):
    print("Value : ", list[i])
