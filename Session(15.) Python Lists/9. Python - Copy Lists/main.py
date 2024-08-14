# Python - Copy Lists

# ___Copy a List___

"""
hum python may copy() aur list() ka astamaal issliay krte hai taa k yeh hum avoid kr sakhe
apnay peechlay list ko tabdeel hone say
"""

# copy() method wahid method hai jo kssi bhi collection of arrays ko copy kr deta hai
# example on list
this_list = ["apple", "banana", "cherry"]
new_list = this_list.copy()
print(new_list)

print("------")

# or second way but yeh sirif list k liay kaam karay gha
this_list1 = ["apple", "banana", "cherry"]  # old list
new_list = list(this_list1)  # copy of old list, "becomes new list"
new_list.append("avocado")  # we add new element in the object(new_list)
print(new_list)  # ab iss list ki length increase hogaey q k hum nay ek new element add kiya
print(this_list1)  # as we can see, there is no changes in previous list
