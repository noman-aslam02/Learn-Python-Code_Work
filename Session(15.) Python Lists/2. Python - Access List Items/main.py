# Access List Items in Python

# ___Access Items___

# Positive Indexing
# Items ko list say access kren k liay hum index[] ka use krte hai
# indexing 0 se start hoti hai, doosri item ka index 1 hota hai aur issi thara agay badhta hai
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print("-----")

# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print("-----")

# ___Range of Indexes___
"""
aghr hamay kissi specific range say items ko bahir nikalana hai list say to hum kuch iss
tareeqay say likh sakhte hai like [0: 3] yaani 0 index say lekr 3 index(not included) takh
ka items lekr aoo.
neechay example may aapko samajh may aa jaey gha
"""
# Positive Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[0:2])

print("-----")

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-2:-1])  # the last item index[-1] "cherry" not included

print("-----")

# ___Jump from Index___
"""
aghr hamay kissi specific range k saath ek ek kr k yaa uss say zada ka jump laga kr item chaeye
to hum kuch iss tareeqay say likhenghay [0: 3:2] <----- yeh ek ek kr k jump lagaey gha
"1" to default value hota hai jss pr already python ek k baad ek object pr iterate krta hai
"""

thislist = ["apple", "banana", "cherry", "cheez", "mickey", "Strawberry", "Gala"]
print(thislist[0:5:2])

print("        or this way")

# ab yehi same behaviour slice() method bhi krta hai

thislist = ["apple", "banana", "cherry", "cheez", "mickey", "Strawberry", "Gala"]
slice_thislist = slice(0, 5, 2)
print(thislist[slice_thislist])

# both way is same
# thislist = ["apple", "banana", "cherry", "cheez", "mickey", "Strawberry", "Gala"]
# print(thislist[slice(0, 5, 2)])
