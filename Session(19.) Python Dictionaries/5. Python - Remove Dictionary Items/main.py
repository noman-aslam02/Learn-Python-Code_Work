# Python - Remove Dictionary Items

# ___pop()___
# pop() method say hum kssi bhi khaas item(key and value) ko remove kr sakhte hai
this_dict = {"name": "noman", "semester": 4, "course": "python"}
this_dict.pop("semester")  # yaha humay "parentheses" may 'key' dena paray gha
print(this_dict)

print("-----")

# ___popitem()___
# popitem() method say dict k last item ko remove kiya jaa sakhta hai
this_dict = {"name": "noman", "semester": 4, "course": "python"}
this_dict.popitem()
print(this_dict)

print("-----")

# ___del___
# del yeh keyword hai jo dict may bhi use ki jati hai dict ko delete krne k liay completely
# del keyword say hum dict k kssi khaas item ko remove bhi kr sakhte hai

# yaha hum dict ko delete kr rahe hai
"""
this_dict = {"name": "noman", "semester": 4, "course": "python"}
del this_dict  # yeh ab delete ho chuka hai
print(this_dict)  # deleted dict ko print nhi kiya jaa sakhta error throw karegha yeh
"""

# yaha hum ek khaas item ko delete(yaani ek tareeqay say remove) kr rahe hai
this_dict = {"name": "noman", "semester": 4, "course": "python"}
del this_dict["name"]
print(this_dict)

print("-----")

# ___clear()___
# clear() method dict ko empty dict bana deta hai
this_dict = {"name": "noman", "semester": 4, "course": "python"}
this_dict.clear()
print(this_dict)