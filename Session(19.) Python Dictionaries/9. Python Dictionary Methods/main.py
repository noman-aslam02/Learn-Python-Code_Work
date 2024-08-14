# Python Dictionary Methods

# ___clear()___
# clear() method dict ko empty dict bana deta hai
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)

print("-----")


# ___copy()___
# copy() method ek original dict ki fake copy bana deta hai, yeh original dict may koi changes nahi lata

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)  # original dict
car.copy()
car.update({"color": "red"})
print(car)  # fake(copy of original dict) dict

print("-----")

# ___fromkeys()___
# fromkeys() method dictionary create karne k liye use hota hai, iss may sab keys ki value same hoti hai
# list, tuple and strings pr fromkeys() use kiya ja sakhta hai

# list
list_fruit = ["apple", "cherry", "avocado"]
value = "abc"
fk_dict = dict.fromkeys(list_fruit, value)
print(fk_dict)

# tuple
tuple_fruit = ("apple", "cherry", "avocado")
value = "abc"
fk_dict = dict.fromkeys(tuple_fruit, value)
print(fk_dict)

# string
string_fruit = "apple"
value = "abc"
fk_dict = dict.fromkeys(string_fruit, value)
print(fk_dict)

print("-----")

# ___get()___
# get() method say hum kssi bhi khaas dict item k value ko access kr sakhte hai without getting error aghr item na mile to
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))

print("-----")

# ___items()___
# Returns **tuples** of key-value pairs.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.items())

print("-----")

# ___keys()___
# Returns all keys. Convert to list if needed.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.keys())

print("-----")

# ___values()___
# Returns all values. Convert to list if needed.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.values())

print("-----")

# ___pop()___
# pop() method ka istemal karke hum dictionary se kisi specific item ko remove kar sakte hai
# Iske liye, hume us item ki key ko pop() method ke argument ke taur par dena hota hai
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
removed_value = car.pop("model")
# Yeh method removed item ki value ko return karta hai
print(removed_value)
print(car)

print("-----")

# ___popitem()___
# popitem() say hum dict k last item ko remove kr sakhte hai
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()
print(car)

print("-----")

# ___setdefault()___
"""
Python ka `setdefault()` method dictionary mein specified key ki value return karta hai,
ya phir agar woh key nahi hoti to us key ko specified default value ke saath add kar deta hai.
"""
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.setdefault("brand", "abc")  # before
print(car)
car.setdefault("course", "python")  # after
print(car)

print("-----")

# ___update()___
# update() method dict k items ko update kr deta hai kssi khaas key and value k saath
# aghr wo key exist nahi krti to yeh ek new key and value add krdeta hai
# ya phir yeh dict to dict bhi add kr sakhta hai

# update exist key's value
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"brand": "abc"})
print(car)

# add a new key and value
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "blue"})
print(car)

# add dict to dict
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car1 = {"brand1": "abc", "model1": "xyz", "year1": 9999}
car.update(car1)
print(car)