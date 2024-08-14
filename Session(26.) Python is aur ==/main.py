# Python is aur ==

# ___is___
# "Is" Python mein object identity aur type comparison ke liye hota hai,
# Agar dono objects same type ke hain ya ek object us type ko represent karta hai,
# to "is" True return hota hai.
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, same memory address
print(a is c)  # False, different memory address

print("-----")

# ___==___
# "==" Python mein values ko compare karne ke liye hota hai, Agar dono values ek jaisi hain,
# to "==" True return karta hai, warna False.
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)  # True, same value
print(a == c)  # True, same value

print("-----")

# ab hum "==" aur "is" dono ko complex tareeqay say samjhe ghay
# yaha hum nay numbers aur strings dono ka example use kiya hai

print("___Integers___")
# numbers
x = 10
y = 10
z = 10.0
print(x is y)  # True, same memory address for small integers
print(x == y)  # True, same value
print(x is z)  # False, different memory address (integer vs float)
print(x == z)  # True, same value

print("___Strings___")
a = "hello"
b = "hello"
c = "".join(["he", "llo"])
print(a is b)  # True, same memory address (string interning)
print(a == b)  # True, same value
print(a is c)  # False, different memory address
print(a == c)  # True, same value

print("-----")

print("----->Bonus code<-----")
# Bonus code
a_list = ["apple", 1]
print(type(a_list))
if "apple" in a_list and isinstance(a_list[0], str) and type(a_list) is list:
    print("G Haa, apple is list may hai aur phela index string hai aur \"a_list\" list hai")
else:
    print("something wrong on this list")

print("-----")

# aghr hamay all elemetns pr apply krna hai isintance to kuch aysay hogha
a_list1 = ("apple", "1")
print(type(a_list1))
if "apple" in a_list1 and all(isinstance(elem, str) for elem in a_list1) and type(a_list1) is tuple:
    print("G Haa, apple is list may hai aur hr elements string hai aur \"a_list1\" list hai")
else:
    print("something wrong on this tuple")