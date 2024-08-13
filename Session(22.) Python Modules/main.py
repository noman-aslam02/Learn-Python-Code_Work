# Python Modules

# ___how to import module___
# hum "import" keyword ka use kr k module ko import krte hai
"""
import math  # to yaha hum nay ek module import kiya hai jss ka name "math" hai
"""

# ___Access Functions___
# import keyword k baad uss k function ko use krne k liay (.) notation ka use kare

# yeh hum built-in module ka function use kr rahe hai
import math
x = math.sqrt(9) * 3  # "9" ka square root '3.0' hota hai, float isski default type hai
print(x)

print("----")

# ___Module Aliases---
# Module Aliases yaani "as" keyword ka use kr k hum module ko chota naam de sakhte hai
# "as" keyword module k saath saath class, function aur variable pr bhi astamaal hota hai

import math as m
x = m.sqrt(9) * m.pi
print(x)

# we can also change the function's name
from math import sqrt as square_root, pi
x = square_root(9) * pi
print(x)



print("----")

# ___Create Module___
# hum kudh ka module bhi create kr sakhte hai
# just hamay ek separate file bana ni paray ghi
# then hum ussko as a module use kr sakhte hai

import mymodule  # yaha hum nay file import kari hai

result = mymodule.sum_num(10, 25)  # print function
print(result)

print(mymodule.per_name)  # print variable

print(mymodule.buildings["build2"])  # print dict

print("-----")

# ___from keyword___
# from keyword ka use kr k hum koi bhi specific part print kara sakhte hai
# iss say hamay module ka name likhne ki zahroorat nahi padti bar bar

from mymodule import per_name

print(per_name)

print("-----")

# ___dir() Function___
# dir() function say hum maujooda module k saray functoins, variables aur classes maloom kr sakte hai
import datetime
print(dir(datetime))