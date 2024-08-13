# Python - Change Dictionary Items

# ___Change Values___
# hum value kssi bhi khaas item ka change kr sakhte hai usska key name de kr square[] bracket may
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
this_dict["model"] = "abc"
print(this_dict)

print("-----")

# ___update()___
# hum update() method say bhi dict k item value ko change kr sakhte hai
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
this_dict.update({"brand":"Ferrari"})
print(this_dict)
