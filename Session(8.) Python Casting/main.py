# Python Casting

# Types of Python Casting
# ___Implicit Casting___
# Python kudh data tpye ko convert kr k deta hai
x = 1.20
y = 2
print(x + y)

# ___Explicit Casting___
# humay kudh say data type ko convert krna padhta hai like int(),str()
#Example
"""
x1 = "1.20"
y2 = 2                        # Before(Wrong way) # hum nay data type convert nhi kri 
print(x1 + y2)  #  yaha error hai string(x1 = "1.20") k saath integer(y2 = 2) nhi ho sakhta 
"""

x1 = "1.20"
y2 = 2                        # After(Right way)
print(float(x1) + y2)

# Methods or functions to convert data type to other data type
# ___int()___
x2 = "10"
y2 = int(x2)
print(y2)  # Output: 10

# ___float()___
x3 = "3.14"
y3 = float(x3)
print(y3)  # Output: 3.14

# ___str()___
# Example of str()
x4 = 123
y4 = str(x4)
print(y4)  # Output: '123'

# ___bool()___
x5 = 0  # In Python 0 value = False
y5 = bool(x5)
print(y5)  # Output: False
x55 = 1
print(bool(x55))  # see the value of x55(1) is True

# ___list()___
x6 = (3.5, 2, 3, 4, 4)
y6 = list(x6)
print(y6)  # Output: [3, 2, 3, 4, 4]

# ___tuple()___
x7 = [3.5, 2, 3, 4, 4]
y7 = tuple(x7)
print(y7)  # Output: (3, 2, 3, 4, 4)

# ___set()___
x8 = [3.5, 2, 3, 4, 4]
y8 = set(x8)
print(y8)  # Output: {2, 3, 4}
# as we know in 'set' the "elements" can't be repeat

# ___dict()___
x9 = [("Name", "Muhammad Noman Aslam"), ("Age", 21), ("Gender", "Male")]
y9 = dict(x9)
print(y9)  # Output: {'Name': 'Muhammad Noman Aslam', 'Age': 21, 'Gender': 'Male'}

# ___chr()___
x11 = 65
y11 = chr(x11)
print(y)  # Output: 'A' # yeh 'unicode' ko 'character' may convert kr raha hai

# ___ord()___
x22 = 'A'
y22 = ord(x22)
print(y)  # Output: 65 # yeh 'character' ko 'unicode'  may convert kr raha hai
