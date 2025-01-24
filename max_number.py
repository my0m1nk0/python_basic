list = [1048,1255,2125,1050,2506,1236,2010,1055]

max_number = list[0] #2506

# for i in range(len(list)): # 7
#     if list[i] > max_number:
#         max_number = list[i]
for i in list:
    if i > max_number:
        max_number = i
print("Max Number : ", max_number)






