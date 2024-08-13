# Python - Access Dictionary Items

# ___Accessing Items___
# kssi bhi khaas item ko access krne k liay usska key mention kre square bracket may
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict["teacher"])

print("-----")

# ___get()___
# get() method say bhi hum kssi bhi khaas item ko access kr sakhte hai
# get() method ka apna faida yeh hai k yeh error throw nahi krta aghr item nahi mile
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict.get("teacher"))
# ab hum get() method uss key pr apply karenghay jo iss dict may maujood nahi hai
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict.get("version"))

print("-----")

# ___Get Keys___
# keys() method dictionary ki tamam keys ki ek list wapis krta hai
# iss may hum item add aur update bhi kr sakhte hai

this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict.keys())

# add an new item
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict["android"] = "samsung"
print(this_dict.keys())

print("-----")

# ___Get Values___
# values() method dictionary ki tamam values ki ek list wapis krta hai
# iss may hum item add aur update bhi kr sakhte hai
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict.values())

# update existing item corresponding key's value
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict["student"] = "asad"
print(this_dict.values())

# add an new item
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict["android"] = "iphone"
print(this_dict.values())

print("-----")

# ___Get Items___
# items() method k zariay hum dict k hr key and value ko print krwa sakhte hai
# yeh as a list of tuples display karegha
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
print(this_dict.items())

# update values in item
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict["student"] = "junaid"
print(this_dict.items())

# add an new item
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict["android"] = "infinix"
print(this_dict.items())

# add dict to dict using update() method
# yeh original dict ko badal deta hai
this_dict1 = {"teacher": "nusrat", "student": "noman", "course": "python"}
this_dict2 = {"model": "ferrari", "color": "red"}
this_dict1.update(this_dict2)
print(this_dict1)

print("-----")

# ___Check if Key, Value, Key and Value  Exists___
# checking is key exist in this dict
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
if "course" in this_dict:
    print("yes 'course' key present in this dict")
# ya kuch iss tareeqay say bhi key maloom kiya jaa sakhta hai
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
if "course" in this_dict.keys():
    print("yes 'course' key present in this dict")

# checking is value exist in this dict
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
if "python" in this_dict.values():
    print("yes 'python' value present in this dict")

# checking is key and value exist in this dict
this_dict = {"teacher": "nusrat", "student": "noman", "course": "python"}
if ("student", "noman") in this_dict.items():
    print("yes 'student' key and its value 'noman' present in this dict")