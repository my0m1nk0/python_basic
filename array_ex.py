#mutable => can be changed
#immutable => cannot be changed #Tuple
# data types  => int , str , float , boolean 
#array [int , str , float , boolean]
arr = [1, "Hello", 2.5, True]
arr2 = (1, "Hello", 2.5, True)

arr2.insert(1,"Hello world")
print(arr2)
# print(arr[0]) #index number 0
# print(arr[1])
# print(arr[2])
# print(arr[3])
# comment 
# this variable is used to get the length of the array
arrLength = len(arr)  
# print(arrLength)

newArr = ["Orange", "Apple", "Banana", "Mango","Apple"]

# append() => add new element to the end of the array
newArr.append("Grapes") #add new element to the end of the array
# insert() => add new element to the array at a specific index
newArr.insert(1,"Pineapple")
#remove() => remove an element from the array
newArr.remove("Banana")
#pop() => remove the last element from the array
# data = newArr.pop()
# print(data)
#clear() => remove all elements from the array
# newArr.clear()
#extend() => add multiple elements to the array
# newArr.extend(["Grapes", "Pineapple", "Mango"])
#sort() => sort the array
# newArr.sort()
#reverse() => reverse the array
# newArr.reverse()
#count() => count the number of elements in the array
# print(newArr.count("Apple"))
#index() => get the index of the element
print(newArr.index("Mango"))
#copy() => copy the array
newArr2 = newArr.copy()
print("newArr 2 : ",newArr2)
print("newArr  1 : ",newArr)
