# Python - Add List Items

# ___Append Items___
# append() method list k end of list pr item add krta hai just 'single item'
fruits = ["apple", "blueberry", "orange"]
fruits.append("cherry")
print(fruits)

print("-------")


# ___Insert Items___
# insert method ka use kr k hum list k kssi specific index pr list add kr sakhte hai
fruits = ["apple", "blueberry", "orange"]
fruits.insert(1, "kiwi")
print(fruits)

print("-------")

# ___Extend List___
# extend() method ka use kr k hum new list ko apnay current list may add kr sakhte hai
# aur yeh kssi bhi type of list ko add kr sakhta hai current list pr

# add list to list
fruits = ["apple", "blueberry", "orange"]
new_fruits = ["fig", "grape", "avocado"]
fruits.extend(new_fruits)
print(fruits)

# add dict to list
info = ["the details of the person"]
dict_list = {"Name": "Noman", "Age": 21, "Gender": "Male"}
info.extend(dict_list.items())
print(info)

# add set to list
fruits = ["apple", "blueberry", "orange"]
new_fruits = {"fig", "grape", "avocado"}
fruits.extend(new_fruits)
print(fruits)