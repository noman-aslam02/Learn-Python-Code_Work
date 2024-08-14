#Assign Multiple Values

#Many Values to Multiple Variables
x,y,z= "Muhammad Ali","Muhammad Noman","Muhammad Adil"
print(x + " \"x\"")
print(y + " \"y\"")
print(z + " \"z\"")

"""
Note: Make sure the number of variables matches the number of values, or else you will
get an error.
"""

#One Value to Multiple Variables
#yaha hum nay ek hi value ko assign kra hai alagh alagh variables say
x = y = z = "Hello World"
print(x)
print(y)
print(z)

#Unpack a Collection
"""
yaha hum collection of values ko tuple ya list say nikal kr alagh alagh variables say
assign krenghay
"""
cars = ("Margalla","Supra","Suzuki")
a,b,c = cars
print(a) #yaha "a" variable first element(Margalla) k barabr ho gaya
print(b) #yaha "b" variable second element(Supra) k barabr ho gaya
print(c) #yaha "c" variable third element(Suzuki) k barabr ho gaya
