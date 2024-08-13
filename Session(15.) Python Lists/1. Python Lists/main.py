# Lists in Python

# ___How to create list___
# list create hote hai using [] aur uss may elements majood hote hai kssi bhi data type k with commas (,)
# Example
employees = ["Noman", "Jhonny", "Donald Trump"]
print(employees)

# ___Unpack List "*"___
# we can unpack list using "*", yeh sirif list k liay astmaal hota hai baaki
print(*employees)

# ___list duplicate items___
# list items duplicate items ko hold kr saktha hai
employees = ["Noman", "Jhonny", "Donald Trump", "Donald Trump"]
print(employees)

# ___list length len()___
# hum list ki number of objects(elements) ko maloom krne k liay len() method ka use karenghay
employees = ["Noman", "Jhonny", "Donald Trump"]
print(len(employees))  # len() method ka starting count 1 say hota hai, its not like index[0]

# ___List Items - Data Types___
# hum list may kssi bhi data type ko store kr sakhte hai
fruit_list = ["apple", "cherry", "banana"]
num_number = [20, 1, 0.1, 145]
boolean_bool = [True, False, True, True, False]
print(fruit_list)
print(num_number)
print(boolean_bool)

# hum ek hi list k andr different data type bhi hold kr sakhte hai
mixer = ["Noman", 21, True, False, 00.1, "Father"]
print(mixer)

# __Type type()___
# aghr hamay kssi list ki data type maloon krni hai to type() ka astamaal kre
mixer = ["Noman", 21, True, False, 00.1, "Father"]
print(type(mixer))

# ___The list() Constructor list()___
# aghr hamay kssi collection of data type ko list may display krwana hai to list() use krte hai
# here how we will use list()
its_tuple_type = ("Noman", 21, True, False, 00.1, "Father")
print("Yeh \"tuple\" data type hai: ", its_tuple_type)
# here we used 'list()' method on tuple and enclosed inside 'list()'
its_list_type = list(("Noman", 21, True, False, 00.1, "Father"))
print("Yeh \"list\" data type hai: ", its_list_type)
