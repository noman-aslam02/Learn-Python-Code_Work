# Python - Set Methods

# ____set method____

# ___add()___
# add() method element add krta hai set may
fruits = {"apple", "cherry", "banana"}
fruits.add("avocado")
print(fruits)

print("-----")

# ___clear()___
# clear() method set ko empty set bana deti hai
fruits = {"apple", "cherry", "banana"}
fruits.clear()
print(fruits)

print("-----")

# ___copy()___
# copy() method current set ki copy bana deta hai taa k original set ko kuch na ho
fruits = {"apple", "cherry", "banana"}
print(fruits)
fruits.copy()
fruits.remove("cherry")
print(fruits)

print("-----")

# ___difference()___
# Shortut key of difference() is "-"
# difference() method first set k elements jo sencond set may maujood nahi hai ussko return krti hai
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1.difference(fruits2)
print(result)
# shortcut "-"
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1 - fruits2
print(result)

print("-----")

# ___difference_update()___
# Shortut key of difference_update() is "-="
# difference_update() method bhi difference() method ki thara kaam krti hai bss yeh original set ko badal deti hai
fruits1 = {"apple", "cherry1", "banana"}
fruits2 = {"mango", "cherry", "banana"}
fruits1.difference_update(fruits2)
print(fruits1)
# shortcut "-="
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
fruits1 -= fruits2
print(fruits1)

print("-----")

# ___discard()___
# discard() method kssi bhi khaas set k item ko remove kr deta hai
# aur aghr item maujood na ho to yeh discard() error throw nahi krta
fruits = {"apple", "cherry", "banana"}
fruits.discard("cherry")
print(fruits)

print("-----")

# ___intersection()___
# Shortut key of intersection() is "&"
# intersection() method duplicates items jo dono sets say match ho rahe ho unko print krdeta hai
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1.intersection(fruits2)
print(result)
# shortcut "&"
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1 & fruits2
print(result)

print("-----")

# ___intersection_update()___
# Shortut key of intersection_update() is "&="
# intersection_update() method bhi intersection() method ki thara kaam krti hai bss yeh original set ko badal deti hai
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
fruits1.intersection_update(fruits2)
print(fruits1)
# shortcut "&="
fruits1 = {"apple1", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
fruits1 &= fruits2
print(fruits1)

print("-----")

# ___isdisjoint()___
# isdisjoint() method True return karta hai jab do sets ke darmiyan koi common element nahi hota, warna False return karta hai

# iss may koi bhi element common nahi hai to yeh 'True' return karegha
fruits1 = {"apple1", "cherry1", "banana1"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1.isdisjoint(fruits2)
print(result)
# iss may 2 elements common hai to yeh 'False' return karegha
fruits1 = {"apple1", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana"}
result = fruits1.isdisjoint(fruits2)
print(result)

print("-----")

# ___issubset ("<=", <)___
# issubset() method check karta hai k ek set doosray set ka hissa (subset) hai ya nahi
# isska matlab hai phele "set k hr elements dusray set may maujood hai yaa nahi"

# Iss current set k sirif 2 elements dusray set may majood hai to yeh 'False' return karegha
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana", "kiwi", "avocado", "orange"}
result = fruits1.issubset(fruits2)
print(result)
# Iss current set k saaray elements dusray set may majood hai to yeh 'True' return karegha
fruits1 = {"apple", "cherry", "banana"}
fruits2 = {"mango", "cherry", "banana", "apple", "avocado", "orange"}
result = fruits1.issubset(fruits2)
print(result)

print("here we did issubset() with shortcut key")
# issko pura dekhe for better understanding

# Sets banatay hain
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2}

# `<=` operator ka istemal kar k check kartay hain k set3 set1 ka subset hai ya nahi
print(set3 <= set1)  # Yeh `True` return karega kyun k set3 set1 ka subset hai

# `<` operator ka istemal kar k check kartay hain k set3 set1 ka proper subset hai ya nahi
print(set3 < set1)  # Yeh bhi `True` return karega kyun k set3 set1 ka proper subset hai

# Ab `<=` operator ka istemal kar k check kartay hain k set2 set1 ka subset hai ya nahi
print(set2 <= set1)  # Yeh `True` return karega kyun k set2 set1 ka subset hai

# Ab `<` operator ka istemal kar k check kartay hain k set2 set1 ka proper subset hai ya nahi
print(set2 < set1)  # Yeh `False` return karega kyun k set2 set1 ka proper subset nahi hai, balkeh dono sets bilkul same hain

print("-----")

# ___issuperset() (">=", >)___
# issuperset() method check karta hai k aik set doosray set ka superset hai ya nahi
# isska matlab hai dusray "set k hr elements phele set may maujood hai yaa nahi"

# Iss current set may sirif 2 elements maujood hai dusray set k to yeh 'False' return karegha
fruits1 = {"mango", "cherry", "banana", "apple", "avocado", "orange"}
fruits2 = {"apple1", "cherry", "banana"}
result = fruits1.issuperset(fruits2)
print(result)
# Iss current set may saaray elements maujood hai dusray set k to yeh 'True' return karegha
fruits1 = {"mango", "cherry", "banana", "apple", "avocado", "orange"}
fruits2 = {"apple", "cherry", "banana"}
result = fruits1.issuperset(fruits2)
print(result)

print("here we did issuperset() with shortcut key")
# issko pura dekhe for better understanding

# Sets banatay hain
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2}

# `>=` operator ka istemal kar k check kartay hain k set1 set3 ka superset hai ya nahi
print(set1 >= set3)  # Yeh `True` return karega kyun k set1 set3 ka superset hai

# `>` operator ka istemal kar k check kartay hain k set1 set3 ka proper superset hai ya nahi
print(set1 > set3)  # Yeh bhi `True` return karega kyun k set1 set3 ka proper superset hai

# Ab `>=` operator ka istemal kar k check kartay hain k set1 set2 ka superset hai ya nahi
print(set1 >= set2)  # Yeh `True` return karega kyun k set1 set2 ka superset hai

# Ab `>` operator ka istemal kar k check kartay hain k set1 set2 ka proper superset hai ya nahi
print(set1 > set2)  # Yeh `False` return karega kyun k set1 set2 ka proper superset nahi hai, balkeh dono sets bilkul same hain


print("-----")

# ___pop()___
# pop() method set k kssi bhi random item ko remove kr deta hai
fruits = {"mango", "cherry", "banana", "apple", "avocado", "orange"}
x = fruits.pop()
print(x)
print(fruits)

print("-----")

# ___remove()___
# remove() method say hum kssi bhi khaas item ko remove kr sakhte hai
fruits = {"mango", "cherry", "banana", "apple", "avocado", "orange"}
fruits.remove("mango")
fruits.remove("apple")
print(fruits)

print("-----")

# ___union()___
# Shortut key of union() is "|" operator
# union() method, do ya zyada sets ke tamam unique elements ko ek naye set mein jama karta hai
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "avocado", "orange"}
result = fruits1.union(fruits2)
print(result)
 # "|" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "avocado", "orange"}
result = fruits1 | fruits2
print(result)

print("-----")

# ___update()___
# update() method, do ya zyada sets ke tamam unique elements ko ek naye set mein jama karta hai
# update() method original set ko badal det hai
# Shortut key of update() is "|=" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "avocado", "orange"}
fruits1.update(fruits2)
print(fruits1)
# "|=" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "avocado", "orange"}
fruits1 |= fruits2
print(fruits1)

print("-----")

# ___symmetric_difference()___
# symmetric_difference() may both sets may elements common nahi hone chaeye
# Shortut key of symmetric_difference() is "^" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "cherry", "banana"}
result = fruits1.symmetric_difference(fruits2)
print(result)
# "^" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "cherry", "banana"}
result = fruits1 ^ fruits2
print(result)

print("-----")

# ___symmetric_difference_update()___
# symmetric_difference_update() may both sets may elements common nahi hone chaeye
# yeh original set ko badal det hai
# Shortut key of symmetric_difference_update() is "^=" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "cherry", "banana"}
fruits1.symmetric_difference_update(fruits2)
print(fruits1)
# "^" operator
fruits1 = {"mango", "cherry", "banana"}
fruits2 = {"apple", "cherry", "banana"}
fruits1 ^= fruits2
print(fruits1)