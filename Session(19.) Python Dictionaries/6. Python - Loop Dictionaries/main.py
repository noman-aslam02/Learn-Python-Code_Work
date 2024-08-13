# Python - Loop Dictionaries

# ___Loop Through a Dictionary___
# loop ka use kr k hum dictionary k hr key and value may say ghuzr sakhte hai

# ___Printing Keys through loop___
# for loop ka simple way may use kr k hum dict k hr keys ko print krte hai
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
"""
yeh for loop statement may hum-nay just example k tor pr "key" name use kiya hai
kuch iss thara "for key in iterable_object:"
"""
for key in this_dict:
    print(key)

print("-----")

# ___Printing Values through loop___
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for value in this_dict:
    print(this_dict[value])

print("-----")

# ___values()___
# values() method ka use kr k hum dict k saraay values print kr sakhte hai
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for value in this_dict.values():
    print(value)

print("-----")

# ___keys()___
# keys() method ka use kr k hum dict k saraay keys print kr sakhte hai
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in this_dict.keys():
    print(key)

print("-----")

# ___items()___
# items() method ka use kr k hum dict k saraay key and value print kr sakhte hai
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key, value in this_dict.items():
    print(key, value)