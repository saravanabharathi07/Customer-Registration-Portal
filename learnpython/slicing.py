#To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:
'''a=[1,2,3,4,5,6]
a[0:3] = [7,8,9]
print(a)'''

#If you insert more items than you replace,
# the new items will be inserted where you specified, and the remaining items will move accordingly:
'''a=[1,2,3,4,5,6]
a[1:2]=[7,8,9]
print(a)'''

#If you insert less items than you replace,
# the new items will be inserted where you specified, and the remaining items will move accordingly:
'''this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)'''

'''n1list = [1,2,3,4,5,6]
n2list=[7,8,9]
n1list.insert(3, n2list)
print(n1list)'''


#THIS EXTEND METHOD CAN BE USED TO APPEND NOT ONLY LIST ELEMENTS, BUT ANY OTHER ITERABLE (like a string, tuple, etc.)
'''n1list = [1,2,3,4,5,6]
n2list=[7,8,9]
n1list.extend(n2list)
print(n1list)'''


#THIS CLEAR METHOD CAN BE USED TO REMOVE ALL ELEMENTS FROM A LIST
'''fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)'''

'''fruits = ["apple", "banana", "cherry"]
fruits.pop(0)
print(fruits)'''

'''fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)'''

'''fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)'''

'''fruits = ["apple", "banana", "cherry"]
del fruits'''
