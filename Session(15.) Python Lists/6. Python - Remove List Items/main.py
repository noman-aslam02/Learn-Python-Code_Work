# Python - Remove List Items

# ___Remove Specified Item___
# remove() method kssi specified item ko remove krta hai
this_list = ["Ali", "Noman", "Asad", "Raza"]
this_list.remove("Raza")
print(this_list)

# aghr list may 2 dafa specified item majood hai to remove() method first element ko remove kr degha
this_list = ["Ali", "Noman", "Asad", "Raza", "Ali"]
this_list.remove("Ali")
print(this_list)

print("-----")


# ___Remove Specified Index___
# kssi specified index say list item ko remove krne k liay pop() method ka use hota hai
this_list = ["Ali", "Noman", "Asad", "Raza"]
this_list.pop(1)
print(this_list)

# aghr hum pop() method k andr koi index number na de to yeh last item ko remove karegha
this_list = ["Ali", "Noman", "Asad", "Raza"]
this_list.pop()
print(this_list)

# hum items ko del keyword ka use kr k bhi remove kr sakhte hai
this_list = ["Ali", "Noman", "Asad", "Raza"]
del this_list[0]
print(this_list)

# yeh range of list items ko delete kr raha hai
this_list = ["Ali", "Noman", "Asad", "Raza"]
del this_list[0:2]
print(this_list)

# aghr hum koi specified index na de to yeh list delete kr deta hai successfully
"""
this_list = ["Ali", "Noman", "Asad", "Raza"]
del this_list[]
print(this_list)
"""

print("-----")

# ___Clear the List___
# clear() method list ko empty krne k liay use hota hai
this_list = ["Ali", "Noman", "Asad", "Raza"]
this_list.clear()
print(this_list)