# Python - Access Tuple Items

# ___Access Tuple Items___
"""
Python mein, jab hum kisi tuple ke item ko access karte hain to hum uska index number use
karte hain. Default taur par, Python positive index position leta hai.
"""
tuple_fruits = ["apple", "banana", "kiwi"]
print(tuple_fruits[1])

print("-----")

# ___Negative Indexing___
# aghr hamay tuple k akhri item say access krna hai to negative index ka use hota hai
tuple_fruits = ["apple", "banana", "kiwi"]
print(tuple_fruits[-1])

print("-----")

# ___Range of Indexes___
# Index ki range batane se, hum tuple ke kuch khaas hisse ko utha sakte hai
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[1:4])  # index[4] "avocado" is not included

"""
aghr hum starting value ya ending value nhi dete to python kudh ba kudh bilkul start"[:4]"
ya end"[1:]" value say index ko return krta hai
"""
# here we leave out start value
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[:3])  # index[3] "strawberry" is not included

# here we leave out end value
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[2:])

print("-----")

# ___Range of Negative Indexes___
# tuple range ke end say shuruwaat krne k liay, to aap negative index ka istemal kar sakte hai

tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[-4:-1])  # index[-1] "avocado" is not included

# yaha hum nay negative(-) end value nhi diya to yeh index[-4] say end takh items return karegha
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[-4:])

# yaha hum nay negative(-) start value nhi diya to yeh 0, 1, 2, 3 return karegha index
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
print(tuple_fruits[:-1])  # index[-1] "avocado" is not included

print("-----")

# ___Check if Item Exists___
# aghr hamay check krna hai k koi bhi khaas item tuple may majood hai ya nahi to "in" keyword ka use kare
tuple_fruits = ["apple", "banana", "kiwi", "strawberry", "avocado"]
if "kiwi" in tuple_fruits:
    print(tuple_fruits, "<------ je majood hai 'kiwi' is tuple collection may")