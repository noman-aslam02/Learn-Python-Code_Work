# Modify Strings in Python

# Case in strings

# ___Upper Case___
x = "Hello World!"
print(x.upper())

# ___Lower Case___
x1 = "Hello World!"
print(x1.lower())

# ___Remove WhiteSpace___
# yeh remove krdeta hai space from starting and ending
x2b = " Hello World! "
print(x2b)  # before

x2a = " Hello World! "
print(x2a.strip())  # after

# ___Replace String___
# yeh data sequence ko replace krdeta hai
x3 = "Hello Jorld!"
print(x3.replace("J", "W"))

# ___Split String___
# Split string ko kaat kar alag alag words ki list bana deti hai
x4 = "Hello, World!"
print(x4.split(", "))  # return ['Hello', 'World!']