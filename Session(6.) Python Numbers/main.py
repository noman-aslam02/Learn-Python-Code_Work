#Python Numbers

#___integer Type(int)___
#yaha hum positive,negative aur whole numbers de sakhte hai with unlimited of length
int_positive = 1200 #yeh ek whole aur positive number
int_negative = -61 #yeh ek negative number
#whole number zero(o) say start hota hai jab k positive(1) say start hota hai

print(type(int_positive))
print(type(int_negative))

#___Float Type(float)___
"""
float or floating point number ek number,negative or positive aur point(.) k baad ek decimal number
ya uss say zada ho sakhta hai numbers
"""
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# Float scientific numbers 'e' OR 'E' jo k 10 ki power hai
x_sci = 1.25E4 # phele yeh 10x4 huwa jsska calculation(10,000) aya phir 1.25x10,000 kiya
Y_sci = -8.77E100 # same yaha bhi yehi huwa hai
print(x_sci)
print(Y_sci)



#___Complex Type(complex)___
#Complex numbers are written with a "j" as the imaginary part
a = complex(3+5j) #isska phela number real part hota hai aur dusra number imaginary hota hai
b = complex(5j)
c = complex(-5j)
d = complex(1)
print(a)
print(b)
print(c)
print(d)

#___Conversion Type___

x1 = 1    # int
y1 = 2.8  # float
z1 = 1j   # complex

#convert from int to float:
a1 = float(x1)

#convert from float to int:
b1 = int(y1)

#convert from int to complex:
c1 = complex(x1)

print(a1)
print(b1)
print(c1)

print(type(a1))
print(type(b1))
print(type(c1))


#___Random Number___

import random

print(random.randrange(1, 10)) #yeh 1 say 10 k beech ka random number generate kregha