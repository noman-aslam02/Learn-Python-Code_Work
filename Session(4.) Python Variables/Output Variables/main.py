# Output Variables in Python

# First Way
# here we just output from one variable
x = "Python is love"
print(x)  # here we pass variable inside the print() funtion to output string value

# Second Way
# Print multiple variable using comma
a = "Python"
b = "is"
c = "love"
print(a, b, c)

# Third Way
# Print multiple variable using + operator
a1 = "Python "
b1 = "is "
c1 = "love"
print(a1 + b1 + c1)
"""
Note:
The space character after "Python " and "is ", without them the result would be
"Pythonisawesome"
"""

# Fourth Way
# yaha hum mathematical print karenghay using + operator
xx = 5
yy = 20
print(xx + yy)  # output : 25

# Wrong Way!
# yaha hum + operator ka use kr k string aur number ko add nhi kr sakhte
"""
aa = "Python"
bb = 20
print(aa +bb) #Python will give you an error
"""

# Best way to add string with number, we will use comma
aa = "Python"
bb = 20
print(aa, bb)  # yeh sahi tareeqa hai
