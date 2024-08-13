# Identity Operators

# ___is Identity Operators(is)___
x = ["apple", "banana"]  # mutable list
y = ["apple", "banana"]  # mutable list
z = x
print(x is z)  # returns true because 'x' and 'z' are pointing to the same list
print(x is y)  # returns false because 'x' and 'y' are not pointing to the same list
print(x == z)  # returns true because 'x' is equals to 'z'
print(x == y)  # returns true because 'x' is equals to 'y'
"""
mutable list '[ ]' may different memory location point hoti rehti hai
but
baaki immutable list may '()' may ya phir 'str' or 'int' ya koi bhi data type
may same memory location rehti hai
"""

print("----------")

# ___is not Identity Operators(is not)___
x = ["apple", "banana"]  # mutable list
y = ["apple", "banana"]  # mutable list
z = x
print(x is not z)
print(x is not y)
print(x != z)
print(x != y)
# yaha reverse hai aghr andr ki condition true huwi to "false" return karegha