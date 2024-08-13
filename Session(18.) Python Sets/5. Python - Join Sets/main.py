# Python - Join Sets

# ___Union___
# union() method 2 sets ko jhod deta hai
union_set1 = {"noman", "asad", "hassan"}
union_set2 = {"ubaid", "junaid", "idrees"}
print(union_set1.union(union_set2))

# union use krne ka ek shortcut tareeqa hai aur wo shortcut '|' operator hai
union_set1 = {"noman", "asad", "hassan"}
union_set2 = {"ubaid", "junaid", "idrees"}
print(union_set1 | union_set2)

print("-----")

# ___Join Multiple Sets___
# multiple sets ko join krne k liay union() method ka use kar k parentheses mein commas se alag alag sets daalein

union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "lemon", "avocado"}
union_set3 = {"mango", "banana", "grapes"}
union_set4 = {"coconut", "orange", "dates"}
result = union_set1.union(union_set2, union_set3, union_set4)
print(result)

# bss same "|" operator ka bhi use kr k multiple sets ko join kr sakhte hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "lemon", "avocado"}
union_set3 = {"mango", "banana", "grapes"}
union_set4 = {"coconut", "orange", "dates"}
result = union_set1.union(union_set2 | union_set3 | union_set4)
print(result)

print("-----")

# ___Join a Set and a Tuple___
# union() method ki madad say hum set ko inn dusray data types k saath join krwa sakhte hai like (tuple and list)
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = ("blueberry", "lemon", "avocado")
print(union_set1.union(union_set2))

union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = ["blueberry", "lemon", "avocado"]
print(union_set1.union(union_set2))

# union() method say hum set ko dict k saath join krwa sakhte hai but kuch different tareeqay say

union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"fruit_names": ["mango", "banana", "grapes"]}
union_set3 = set()
for key, value in union_set2.items():
    union_set3.add((key, tuple(value)))  # convert list into tuple because list is not hashable
result = union_set1.union(*union_set3)
print(result)

# isska dusra tareeqa yeh bhi hai
# yeh tareeqa best way ho jata hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"fruit_names": ["mango", "banana", "grapes"]}
result = union_set1.union(union_set2)
for value in union_set2.values():  # yaha hum nay sirif values li hai q k set automatically keys le leta hai
    print(result.union(value))

# ________Important Note________
"""
‘|’ operator sirf sets ko sets ke saath jodne ki ijazat deta hai, likn union() method kssi bhi
data types k saath join ho sakhta hai.
"""

print("-----")

# ___update___
# update() method bhi union ki thara kaam krta hai bss yeh original set ko badal deta hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "lemon", "avocado"}
union_set1.update(union_set2)
print(union_set1)

# update() method pr bhi hum multiple sets ko jhod sakhte hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "lemon", "avocado"}
union_set3 = {"mango", "banana", "grapes"}
union_set4 = {"coconut", "orange", "dates"}
union_set1.update(union_set2, union_set3, union_set4)
print(union_set1)

print("-----")

# ___Intersection___
# intersection() method just duplicate values ko return krta hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1.intersection(union_set2)
print(result)

# as we know k True aur 1 ek hi value samjha jata hai, False aur 0 bhi same value samjhe jate hai
union_set1 = {"apple", "cherry", 0, True}
union_set2 = [False, 1, "kiwi", "apple"]
result = union_set1.intersection(union_set2)
print(result)

print("-----")

# intersection_update() method bhi duplicate items ko return krta hai but yeh original set ko badal deta hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
union_set1.intersection_update(union_set2)
print(union_set1)

print("-----")

# intersection() method ka ek shortcut key hai "&" operator
# hum intersection() method k bajaey "&" operator ka bhi use kr sakhte hai
# but "&" operator may sirif set ko set k saath hi join kr sakhte hai (disadvantage)
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1 & union_set2
print(result)

print("-----")

# ___Difference___
# difference() method sirif wohi items return krta hai jo phele set hai may, second set may nahi hote
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1.difference(union_set2)
print(result)

# difference_update() method bhi same yehi kaam krta hai bs yeh original set ko badal deta hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
union_set1.difference_update(union_set2)
print(union_set1)

# hum difference() k bajaey hum "-" operator ka bhi astamaal kr sakhte hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1 - union_set2
print(result)

print("-----")

# ___Symmetric Differences___
# symmetric_difference() method sirf un elements ko rakhta hai jo sirf ek set mein hain, dono mein nahi
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1.symmetric_difference(union_set2)
print(result)

# symmetric_difference_update() method bhi same yehi kaam krta hai bs original set ko badal deta hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
union_set1.symmetric_difference_update(union_set2)
print(union_set1)

# symmetric_difference() k bajaey "^" operator ka bhi astamaal kr sakhte hai
union_set1 = {"apple", "cherry", "kiwi"}
union_set2 = {"blueberry", "kiwi", "apple"}
result = union_set1 ^ union_set2
print(result)