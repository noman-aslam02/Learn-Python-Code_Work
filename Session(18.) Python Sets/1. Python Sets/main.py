# Python Sets

# ___Set___
# Python may 'sets' curly{} brackets k andr bndh kr k define kiye jaate hai as a Object
set_items = {"apple", "fruits", "cherry"}
print(set_items)

print("-----")

# ___Duplicates Not Allowed___
# sets may 2 items same name k nhi ho sakhte
set_items = {"apple", "fruits", "cherry", "fruits", "cherry"}
print(set_items)

# sets may 1 and True same value manay jate hai
# sets may 0 and False same value manay jate hai
set_items = {True,"Noman", 0, False, "Ahsan", 1, 1}
print(set_items)

print("-----")

# ___Get the Length of a Set___
# aghr hamay number of set items ki length maloom krni hai to len() method ka use kare
set_items = {"apple", "fruits", "cherry"}
print(len(set_items))

print("-----")

# ___Set Items - Data Types___
# sets kssi bhi data types ka ho sakhta hai
set_items1 = {"apple", "fruits", "cherry"}
print(set_items1)
set_items2 = {True, False, False, True}  # as we know we can't repeat same values in set
print(set_items2)
set_items3 = {2001, 11, 31, 0}
print(set_items3)


# Set mukhtalif data types ko shamil kar sakta hai
set_items = {"apple", "fruits", True, 0.13, "kiwi" }
print(set_items)

print("-----")

# ___type()___
# aghr hamay set ki type maloom krni hai to type() method ka use kare
set_items = {"apple", "fruits", "kiwi"}
print(type(set_items))

print("-----")

# ___The set() Constructor___
# hum set() constructor ka use kr k set bhi bana sakhte hai
set_items = set(("apple", "fruits", "kiwi"))
print(set_items)