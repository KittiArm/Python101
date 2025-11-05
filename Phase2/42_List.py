# List

# Primitive data type
a, b, c, d, e = 1, 2, 3, 4, 5

# Non-primitive data type
number = []
number = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Access data in list
print(number[0:3])
print(number[-1])
print(len(number)) # count number of member in list


# Edit data in list
print("Edit data in list >>>")
print(f"Before : {number}")
number[2] = 9
print(f"Before : {number}")

# Loop
print("Loop >>>")
for x in number:
    print(x)

print("Sum >>>")
sum=0
for x in number:
    sum+=x
    print(sum)

# Check data in list
print("Check data in list >>>")
if 9 in number:
    print("Yes")
else:
    print("No")

# Add data to list
print("Add data to list >>>")
print(f"Before : {number}")
number.append(99) # list_name.append(data) : add "data" append to list "list_name"
print(f"Append : {number}")
number.insert(0, 99) # list_name.insert(index, data) : add "data" to list "list_name" at "index"
print(f"Insert : {number}")

# Remove data to list
print("Remove data to list >>>")
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
print(f"Before : {number}")

number.remove(99) # list_name.remove(data) : remove "data" from list "list_name"
print(f"Remove : {number}")

number.pop() # list_name.pop() : remove last index of "data" from list "list_name"
print(f"Pop : {number}")

number.clear() # li_name.clear() : clear all data from list "list_name"
print(f"Clear : {number}")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before : {number}")
del number[1] # list_name.remove(data) : remove "data" from list "list_name"
print(f"Del : {number}")


# Copy data from list1 to list2
_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_list2 = []
print(f"_list1 = {_list1}, Before")
print(f"_list2 = {_list2}, Before")

_list2 = _list1.copy() # _list2 = _list1.copy(dta) : copy "data" from _list1 to _list2
print(f"_list2 = {_list2}, After")

_alllist = _list1 + _list2 # use + for concat data from 2 lists
print(_alllist)

# count number of data
_count_data = _alllist.count(5)
print(f"Count data = {_count_data}")

# Extend
_alllist.extend(number)
print(f"Extend = {_alllist}")