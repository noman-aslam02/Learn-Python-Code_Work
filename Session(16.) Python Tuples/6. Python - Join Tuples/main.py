# Python - Join Tuples

# ___Join Two Tuples___
# Tuples mein extend() aur append() methods nahi hote. Tuples immutable hote hain

# hum 2 tuples ko jhodne k liay + operator ka astamaal karenghay
tuple_items = ("apple", "banana", "cherry")
tuple_items_1 = ("kiwi","avocado", "lemon")
new_tuple_items = tuple_items + tuple_items_1
print(new_tuple_items)

print("-----")

# ___Multiply Tuples___
# multiply * operator ka astamaal kr k hum tuple of number of times join kr sakhte hai
tuple_items = ("apple", "banana", "cherry")
mul_tuple = tuple_items * 2  # number of 2 times use kara hai to tuple 2 dafa print hogha
print(mul_tuple)

print("-----")

# hum tuple par seedha slice method istemal nahi kar sakte, lekin hum alag variable bana kar index slicing se wohi kaam kar sakte hain
tuple_items = ("apple", "banana", "cherry")
x = slice(0, 2)
print(tuple_items[x])

# or we can do like this
tuple_items = ("apple", "banana", "cherry")
x = tuple_items[0:2]
print(x)