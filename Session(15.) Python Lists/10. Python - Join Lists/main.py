# Python - Join Lists

# ___+ Operator___
# + operator ka use kr hum simplest way may 2 list ko jhod sakhte hai
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
join_list = list1 + list2
print(join_list)

print("-----")

# ___Append List items (loop)___
# hum list1 k elements ko one by one append kr sakhte hai list2 may using loop to make new list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for i in list1:
    list2.append(i)
print(list2)

print("-----")

# ___extend() method___
# extend() method ek list k elements ko dusray list may add kr deta ha list k end may
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)