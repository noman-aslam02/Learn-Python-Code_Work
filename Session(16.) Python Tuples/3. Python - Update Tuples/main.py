# Python - Update Tuples

# ___Change Tuple Values___
# jaise k hamay maloom hai hum tuple unchangeable hai
# but hum ek tareeqay say issko change kr sakhte hai as a 'list' bana kr
tuple_items = ("Karachi", "Lahore", "Islamabad", "Multan", "Quetta", "Peshawar")
list_items = list(tuple_items)
list_items[2] = "Sukkur"
tuple_items = tuple(list_items)
print(tuple_items)

print("-----")

# ___Add Items___
# tuple may hum items add nhi kr sakhte
# but hum tuple ko list may convert krne k baad append() method ka use kr k apni mrzi k mutabiq items adds kr sakhte hai
tuple_fruits = ("apple", "banana", "cherry")
list_fruits = list(tuple_fruits)
list_fruits.append("avocado")
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)

# or we can do like this, add tuple to tuple
tuple_fruits = ("apple", "banana", "cherry")
add_new_fruits = ("orange",)
add_new_fruits += tuple_fruits
print(add_new_fruits)
print(tuple_fruits)  # as we can see original list ko koi asar nhi huwa hai just new list bani hai

print("-----")

# ___Remove Items___
# tuple cannot remove items
# but can can remove it after converting tuple into list :)
tuple_fruits = ("apple", "banana", "cherry")
list_fruits = list(tuple_fruits)
list_fruits.remove("cherry")
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)

# or we can delete the tuple completely
# yeh error degha aghr hum "del" keyword ka use kr k deleted tuple ko print kareghay
tuple_fruits = ("apple", "banana", "cherry")
del tuple_fruits
# print(tuple_fruits)
try:  # Yahan pe woh code likha jata hai jahan pe error ho sakta hai
    print(tuple_fruits)
except:  # Agar upar wale code mein koi error aata hai toh yeh code execute hota hai
    print("tuple_fruits delete ho gaya hai succesfully")

# we will learn more about 'try' and 'except'