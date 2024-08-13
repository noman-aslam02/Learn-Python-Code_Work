#Assignment Operators in Python

# ___Assign Operator(=)___
x = 5
print(x)

# ___Add & Assign Operator(+=)___
x1 = 5
x1 += 4  # or x1 = x1 + 4 ---> #equivalent hai yaani yeh dono use kr sakhte hai same kaam hai dono ka
print(x1)

# ___Subtract & Assign Operator(-=)___
x2 = 5
x2 -= 4  # or x2 = x2 - 4 ---> #equivalent hai
print(x2)

# ___Multiply & Assign Operator(*=)___
x3 = 5
x3 *= 4  # or x3 = x3 * 4 ---> #equivalent hai
print(x3)

# ___Divide & Assign Operator(/=)___
x4 = 5
x4 /= 4  # or x4 = x4 / 4 ---> #equivalent hai
print(x4)

# ___Floor Division & Assign Operator(//=)___
x5 = 5
x5 //= 4  # or x5 = x5 // 4 ---> #equivalent hai
print(x5)
"""
isska result '1.25' jssko yeh '1' may convert krdegha yaani decimal_point(.) k baad
wala value nhi kregha show
"""

# ___Modulus & Assign Operator(%=)___
x6 = 5
x6 %= 4  # or x6 = x6 % 4 ---> #equivalent hai
print(x6)

# ___Exponentiation & Assign Operator(**=)___
x7 = 5
x7 **= 4  # or x7 = x7 ** 4 ---> #equivalent hai
print(x7)  # same as 5*5*5*5 = 625

# ___Bitwise AND & Assign Operator(&=)___
x8 = 5
x8 &= 4  # or x8 = x8 & 4  ---> #equivalent hai
print(x8)  # how it works
"""                  
    101  (x8 = 5)
  & 100  (4)
  ------
    100  (Result)
"""

# ___Bitwise OR & Assign Operator(|=)___
x9 = 5
x9 |= 4  # or x9 = x9 | 4 ---> #equivalent hai
print(x9)  # how it works
"""                  
    101  (x9 = 5)
  | 100  (4)
  ------
    101  (Result)
"""

# ___Bitwise XOR & Assign Operator(^=)___
x10 = 5
x10 ^= 4  # or x10 = x10 ^ 4 ---> #equivalent hai
print(x10)  # how it works
""" 
    101  (x10 = 5)
  ^ 100  (4)
  ------
    001  (Result)
"""

# ___Right Shift & Assign Operator(>>=)___
x11 = 10
x11 >>= 2  # ya x11 = x11 >> 2  ---> #Equivalent hai
print(x11)  # how it works
""" 
    1010  (x11 = 10)
>>  0010  (2 bits ke right shift)
------
    2     (Result)
"""

# ___Left Shift & Assign Operator(<<=)___
x11 = 10
x11 <<= 2  # ya x11 = x11 << 2  ---> #Equivalent hai
print(x11)  # kaise kaam karta hai
""" 
    1010  (x11 = 10)
<<  101000  (2 bit ke left shift)
------
    40     (Result)
"""
