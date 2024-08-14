# Operator Precedence

# isska precedence sab say top say start hoti hai

# yeh sab say top pr hai
# 1st
# ___Parentheses()___
print((6-3)-(6+3))  # brackets will be done first "-3+9" = -6

# 2nd
# ___Exponentiation(**)___
print(100 - 3 ** 3)  #	Exponentiation will done first then we will subtract

# 3rd
# ___Unary plus, unary minus, and bitwise NOT(+x  -x  ~x)___
print(100 - ~3)  # phele yeh ~3 eveluate huwa phir add huwa 100 k saath

# 4th
# ___Multiplication, division, floor division, and modulus(*  /  //  %)___
print(100 + 5 * 3)  # first multiply(*) hogha phir plus 100 k saath

# 5th
# ___Addition and subtraction()___
print(100 - 5 * 3)  # first we will multiply(*) then we will subtract(-)

# 6th
# ___Bitwise left and right shifts(<< >>>)___
print(8 >> 4 - 2)  # first hum subtract(-) karenghay phir right shift(>>)

# 7th
# ___Bitwise AND(&)___
print(6 & 2 + 1)  # first hum add(+) karenghay phir bitwise AND(&)

# 8th
# ___Bitwise XOR(^)___
print(6 ^ 2 + 1)  # first yaha addition(+) hoghi phir Bitwise XOR(^)

# 9th
# ___Bitwise OR(|)___
print(6 | 2 + 1)  # first yaha addition(+) phir Bitwise OR(|)

# 10th
# ___Comparisons, identity, and membership operators(==  !=  >  >=  <  <=  is  is not  in  not in)___
print(5 == 4 + 1)  # yaha phele addition(+) phir check karenghay equal hai dono ya nhi

# 11th
# ___Logical NOT(not)___
print(not 5 == 5)  # yeh check kregha 5 aur 5 k barabr nhi hona chaeye returns(false)

# 12th
# ___Logical AND(and)___
print(1 or 2 and 3)
"""
The calculation:
1 or 3 = 1 <---output
"""

# 13th
# ___Logical OR(or)___
print(4 or 5 + 10 or 8)  # addition(+) first then Logical OR(or)
"""
The calculation:
4 or 15 or 8 = 4 <---output
"""

# Bonus
print(5 + 4 - 7 + 3)
"""
Note:
If two operators have the same precedence, the expression is evaluated from
left to right

The calculation:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5 <---output
"""