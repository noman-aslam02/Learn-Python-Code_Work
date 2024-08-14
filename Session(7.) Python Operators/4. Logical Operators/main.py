# Logical Operators

# ___and Logical Operators(and)___
x = 5
print(x > 5 and x < 10)  # returns False because 5 is not greater than 5
# 'and' may both sides ka true hona zahroori hai

# ___or Logical Operators(or)___
x1 = 5
print(x1 > 5 or x1 < 10)  # returns True because 5 is less than 10
# 'or' may kssi ek side ka true hona zahroori hai

# ___not Logical Operators(not)___
x2 = 5
print(not(x2 > 5 and x2 < 10))  # returns True because 5 is not greater than 5 but 5 is less than 10
# ab iss nay true return q kara neechay comment padhe
# 'not' iss may reverse hai aghr andr ki condition false huwi to true hogha