# Python Tuples

# ___Tuple___
# to python may tuple round brackets may bndh rehti hai
# aur yeh immutable hote hai yaani unchangeable hai
# we can not remove and add in tuple
tuple_items = ("apple", "banana", "cherry")
print(tuple_items)

print("-----")

# ___Allow Duplicates___
# tuple multiple same name k elements ko allow krti hai apne majooda collection may
tuple_items = ("apple", "banana", "cherry", "apple", "banana", "cherry")
print(tuple_items)

print("-----")

# ___Tuple Length___
# aghr hamay tuple may check krna hai k kitne items majood hai to len() method use kare
tuple_items = ("apple", "banana", "cherry", "apple", "banana", "cherry")
print(len(tuple_items))

print("-----")

# ___Create Tuple With One Item___
"""
tuple banatay waqt aghr hum sirif ek value de rahe hai to yaad rakhe comma lagana zahroori hai
ek value k baad wrna python samjhe yeh int, str, ya boolean value hai
"""
this_tuple = ("apple",)
print(type(this_tuple))
# NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))

print("-----")

# ___Tuple Items - Data Types___
# Tuple items kssi bhi data types k hoo sakhte hai
tuple_string = ("apple", "banana", "cherry")
tuple_integer = (1, 5, 7, 9, 3)
tuple_boolean = (True, False, False)
print(tuple_string)
print(tuple_integer)
print(tuple_boolean)

print("-----")

# tuple store kr sakhta hai multiple data types k items ko
# A tuple with strings, integers and boolean values
tuple_types = ("noman", 21, "Ali", True, "ABC", False, 0.11)
print(tuple_types)

print("-----")

# ___type()___
# tuple ki type maloom krne k liay type() method ka use kare
tuple_types = ("noman", 21, "Ali", True, "ABC", False, 0.11)
print(type(tuple_types))

print("-----")

# ___The tuple() Constructor___
# kssi bhi collection of items ko tuple bana ne k liay tuple() contructor ka use kro
# iss say aapki data type tuple bn jaeyghi
fruits_list = tuple(["apple", "banana", "kiwi", "strawberry"])  # tuple may convert kiya hai
print(fruits_list)  # yeh ab tuple k shakal may display kregha items ko