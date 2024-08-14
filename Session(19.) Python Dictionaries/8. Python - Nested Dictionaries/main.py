# Python - Nested Dictionaries

# ___Nested Dictionaries___
# Nested Dictionaries ka matlab hai dictionary k andr dictionary

# abhi hum ek dictionary k andr 3 dictionary hold krwa rahe hai
# "stud_bio" yeh ek dictionary hai jss nay 3 dictionary hold kiye huwe hai
# "child1" yeh ek dictionary
# "child2" yeh ek dictionary
# "child3" yeh ek dictionary
stud_bio = {
    "child1": {"name": "noman", "gender": "male"},
    "child2": {"name": "asad", "gender": "male"},
    "child3": {"name": "ubaid", "gender": "male"}
}
print(stud_bio)

print("-----")

# hum 3 dictionaries ko add krwa rahe hai ek new dictionary pr
child1 = {"name": "zain", "gender": "male"}  # dictionary 1
child2 = {"name": "ali", "gender": "male"}  # dictionary 2
child3 = {"name": "ahsan", "gender": "male"}  # dictionary 3
# yeh ek new dictionary hai
class_room = {
    "child1": child1,  # adding dictionary 1
    "child2": child2,  # adding dictionary 2
    "child3": child3  # adding dictionary 3
}
print(class_room)

print("-----")

# ___access nested dictionary item___
stud_bio = {
    "child1": {"name": "noman", "gender": "male"},
    "child2": {"name": "asad", "gender": "male"},
    "child3": {"name": "ubaid", "gender": "male"}
}
print(stud_bio["child1"]["name"])

print("-----")

# ___Loop Through Nested Dictionaries___
# hum loop ka use kr k nested dictionaries say ghuzr-renghay
stud_bio = {
    "child1": {"name": "noman", "gender": "male"},
    "child2": {"name": "asad", "gender": "male"},
    "child3": {"name": "ubaid", "gender": "male"}
}
# yaha pr "x" 'inner_dict' name represent kr raha hai
# dusri taraf "y" uss 'inner_dict' k key and value ko represent kr raha hai
for x, y in stud_bio.items():
    print(x)
# yaha key li jaa rahi hai jo "z" represent kr raha hai
    for z in y:
        print(z, ":", y[z])  # yaha "z" key aur dusri taraf "y[z]" iss key ka corresponding value print kr raha hai

print("-----")

# bonus code
# yaha hum nay ek new nested dict add kari hai
stud_bio = {
    "child1": {"name": "noman", "gender": "male"},
    "child2": {"name": "asad", "gender": "male"},
    "child3": {"name": "ubaid", "gender": "male"}
}
stud_bio["child4"] = {"name": "idrees", "gender": "male"}
print(stud_bio)

print("adding new key and value")
# yaha hum nay nested dictionary may ek new key and valye add kari hai
stud_bio = {
    "child1": {"name": "noman", "gender": "male"},
    "child2": {"name": "asad", "gender": "male"},
    "child3": {"name": "ubaid", "gender": "male"}
}
stud_bio["child1"]["course"] = "python"
print(stud_bio)