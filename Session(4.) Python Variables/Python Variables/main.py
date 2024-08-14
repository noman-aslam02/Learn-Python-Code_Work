#Variables

# Creating Variables
x = 21
y = "Noman Aslam"
print(x)
print(y)

"""
Python may hamay kssi bhi variable ko data type dene ki zahroorat nhi prti aur jo last variable
declare hoghi wohi variable print hoghi
"""
# For Example
noman_age = 21
noman_age = 22  # last variable jo k overwrite kri hai hum nay
print(noman_age)

# Case Sensitive
"""
Python mein “case sensitive” ka matlab hai ki ‘A’ aur ‘a’ alag hain. Yani, apple aur Apple do
alag cheezein hongi.
"""
Apple = "Red"
apple = "Yellow"
print(apple) # too yaha yellow print hogha because yaha humnay lowercase wala apple delcare kiya

# Get the Type
# yaha hum hr define variable ki type maloom kr sakhte hai using type() function
x = 20
y = True
d = None
z = "Nomi"
print(type(x))
print(type(y))
print(type(d))
print(type(z))

# Casting
"""
jab hamay kssi variable ko kssi specific data type may dekhana ho to hum str, int , float
or etc ka use krte hai 
"""
# example
x = str(21)
x1 = float(21)
x2 = float(21.4)
x3 = 21.1
y = "Noman"
z = bool(1 > 2)
print(x)
print(x1)
print(x2)
print(x3)
print(y)
print(z)

# Single or Double Quotes
"""
Python may aap single ya double quotes dono may variables decalre kro, python dono hi
execute kr sakhta hai 
"""
v = "Noman"  # double quotes
print(v)
v = 'Nomi'  # single quotes
print(v)
