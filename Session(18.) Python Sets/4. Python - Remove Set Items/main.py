# Python - Remove Set Items

# ___Remove Item___
# set k item ko remove krne k liay hum remove() ya discard() method ka use kr sakhte hai

# remove()
this_set = {"apple", "cherry", 100, False}
this_set.remove(False)
print(this_set)

# aghr remove kiya huwa item exist nahi krta, remove() error throw karegha
# this_set = {"apple", "cherry", 100, False}
# this_set.remove("Kiwi")
# print(this_set)

# discard()
this_set = {"apple", "cherry", 100, False}
this_set.discard(100)
print(this_set)

# aghr remove kiya huwa item exist nahi krta, discard() error throw nahi karegha
# yeh set items ko same wohi rehne deta hai koi changes nahi ati
this_set = {"apple", "cherry", 100, False}
this_set.discard("Kiwi")
print(this_set)

print("-----")

# ___pop()___
# pop method ka bhi use kr k items ko remove kr sakhte hai
# yaad rakhe pop() method "set" may kssi bhi random item ko remove kr sakhta hai
this_set = {"apple", "cherry", "lemon"}
x = this_set.pop()
print(x, "<------Removed Item from set")  # yeh just remove kiya huwa item bata raha hai
print(this_set)  # ab yeh new set bn jaey ghi

print("-----")

# ___clear()___
# clear() method say set ek empty set bn jata hai
this_set = {"apple", "cherry", "lemon"}
this_set.clear()
print(this_set)

print("-----")

# ___del___
# "del" keyword ka use kr set delete ho jata hai completely
this_set = {"apple", "cherry", "lemon"}
del this_set
# ab error show hogha "name 'this_set' is not defined"
# yeh issliay huwa q k ab 'this_set' object name ka set delete ho chuka hai
# print(this_set)
