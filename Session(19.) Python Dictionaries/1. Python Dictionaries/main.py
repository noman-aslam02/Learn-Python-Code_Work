# Python Dictionaries

# ___how Python Dictionaries looks___
this_dict = {"name": "noman", "age": 99, "gender": "Male"}
print(this_dict)

print("-----")

# ___Dictionary Items___
# dict items k values ko hum directly access kr sakhte hai uss ka name( yaani key) dee kr
this_dict = {"name": "noman", "age": 99, "gender": "Male"}
print(this_dict["name"])

print("-----")

# ___Duplicates Not Allowed___
# dict may duplicates items same key k saath allow nahi hai
this_dict = {"name": "noman", "gender": 99, "gender": "Male"}
print(this_dict)  # yeh overwrite kr raha hai gender"key" k value ko q k gender"key" 2 times aya hai

print("-----")

# ___Dictionary Length___
# dict ki length maloom krne k liay len() function ka use kre
this_dict = {"name": "noman", "age": 99, "gender": "Male"}
print(len(this_dict))

print("-----")

# ___Dictionary Items - Data Types___
# dict items kssi bhi data type k ho sakhte hai
this_dict = {"mouse": "Bloody", "age": 99, "IsPythonGood": True}
print(this_dict)

print("-----")

# ___type()___
# dict ki type maloom krne k liay type() method ka use kre
this_dict = {"mouse": "Bloody", "age": 99, "IsPythonGood": True}
print(type(this_dict))

print("-----")

# ___The dict() Constructor___
# dict() constructor ka use kr k hum kssi bhi data type ko dict type may badal sakhte hai

# yeh list of tuples hai jssko dict may convert kiya gaya hai
this_list = dict([("name", "noman"), ("android", "samsung"), ("car", "audi")])
print(this_list)

# yeh tuple of tuples hai jssko dict may convert kiya gaya hai
this_list = dict((("name", "noman"), ("android", "samsung"), ("car", "audi")))
print(this_list)

# yeh set of tuples hai jssko dict may convert kiya gaya hai
this_list = dict({("name", "noman"), ("android", "samsung"), ("car", "audi")})
print(this_list)

#  hr variable may value assign kr k ussko as a dict contructor bhi bana sakhte hai
this_list = dict(
    name="noman",
    android="samsung",
    car="audi")
print(this_list)