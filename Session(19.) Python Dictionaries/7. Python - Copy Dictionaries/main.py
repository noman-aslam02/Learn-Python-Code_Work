# Python - Copy Dictionaries

# ___Copy a Dictionary___

# yaha dict ko copy krne k 2 methods hai
# copy()
# dict()

# copy()
# copy() method say hum ek original dict ki ek fake copy bana sakhte hai
# iss method say original dict pr koi asar nahi padegha
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(this_dict)  # before
new_dict = this_dict.copy()
del new_dict["brand"]
print(new_dict)  # after

print("-----")

# dict()
# dict() method say bhi dict ki copy banaee jaa sakhti hai
# iss method say original dict pr koi asar nahi padegha
this_dict = {"name": "noman", "gender": "male", "course": "python"}
print(this_dict)  # before
new_dict = dict(this_dict)
del new_dict["gender"]
print(new_dict)  # after
