list = [1048,1255,2125,1050,2506,1236,2010,1055]

min_number = list[0] #1048

# for i in range(len(list)): # 7
#     if list[i] < min_number:
#         min_number = list[i]
for i in list:
    if i < min_number:
        min_number = i
print("Min Number : ", min_number)
