# Change List Items in Python
# Rule: last index required nhi hota

# ___Change the value___
# yeh just current item ki value change kregha using index
list_items = ["apple", "banana", "cherry"]
list_items[1] = "mango","ali"
print(list_items)

print("---------")

# ___Change a Range of Item Values___
# yeh range of items ki value ko change karegha iss may starting and ending index deni hoti hai
list_items = ["apple", "banana", "cherry"]
list_items[1:2] = ["mango"]
print(list_items)  # single value insert kri
list_items[1:3] = ["mango", "strawberry"]
print(list_items)  # yaha 2 items insert kri hai

"""
if we insert more items than replace, to phir yeh new items insert kareghi but baaki k remain-
ing items hai wo bhi print ho jatay hai iss may if we insert more items than replace
"""
list_items = ["apple", "banana", "cherry"]
list_items[1:2] = ["mango", "strawberry", "orange"]
print(list_items)  # "cherry" index[2] is required in this example

"""
if we insert less items than replace, isska bhi same wohi kaam hai but ho sakhta hai
replacement zada aur items km hone ki wajah say list short ho jaey
"""
list_items = ["apple", "banana", "cherry", "mango", "strawberry", "orange"]
list_items[1:5] = ["kiwi"]
print(list_items)

print("-----")

# ___Insert Items___
# yeh insert() method list item may ek new item add krta hai jss say list ki length bhr jati hai
this_items = ["apple", "banana", "cherry"]
this_items.insert(2, "strawberry")
print(this_items)
# another more example
this_items = ["apple", "banana", "cherry"]
this_items.insert(2, "strawberry")
this_items.insert(4, "strawberry")
print(this_items)