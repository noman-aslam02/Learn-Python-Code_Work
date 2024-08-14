# Bitwise operators

# ___AND Bitwise operator(&)___
x = 6
y = 3
print(x & y)
print(6 & 3)  # both are same way but here we did not assign variable
"""
# & operator har bit ko barabar hone par 1 par set karta hai, warna 0 par set karta hai.

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
"""

# ___OR Bitwise operator(|)___
x1 = 6
y1 = 3
print(x1 | y1)
"""
# | operator har bit ko kam az kam ek bit 1 hone par 1 par set karta hai, agar dono bits 0 hain to 0 par set karta hai.

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================
"""

# ___XOR Bitwise operator(^)___
x2 = 6
y2 = 3
print(x2 ^ y2)
"""
# ^ operator jab sirf ek bit 1 hota hai, to result usi bit ko 1 par set karta hai, agar dono bits 0 hain ya dono 1 hain to 0 par set karta hai.

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""

# ___NOT Bitwise operator(~)___
x3 = 3
print(~x3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""

# ___Zero fill left shift operator(<<)___
print(3 << 2)
"""
# << operator bit ko specified number of times left side par shift karta hai.
Right side par khali jagaon ko 0's se bharta hai.

# If you move each bit 2 times to the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""

# ___Signed right shift operator(>>)___
print(3 >> 2)
"""
# >> operator bit ko specified number of times right side par shift karta hai.
Left side par khali jagaon ko 0's se bharta hai.

# If you move each bit 2 times to the right:
# 3 = 0000000000000011
# becomes
# 0 = 0000000000000000

"""