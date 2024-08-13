# While loops in Python

# ___Simple example___
i = 0  # name should assign before running while loop
while i < 6:
    print(i)
    i += 1  # increment dena zahroori hai while loop may manually
# aghr hum increment nhi krte use to yeh infinite chalta rehta loop

# ___break statement___
x = 0
while x < 8:
    print(x)
    if x == 3:
        break
    x += 1
# how it works
# break statement loop ko stop krdegha
# iss may value phele print ho rahi phir condition check hoghi k value 3 k barabar hai k nhi, aghr barabr ho jati hai to loop break yaani stop hoo jaeyghi

print("-----")

# ___The continue Statement___
# continiue statement current itertion ko skip kr k next iteration may chala jaeygha
x1 = 0
while x1 < 6:
  x1 += 1
  if x1 == 3:
    continue
  print(x1)

print("-----")

# ___The else Statement___
# yeh else statement may block of code tab execute hota hai jab loop pura end ya false hoo jata hai
# else statement ka code kabhi bhi execute nhi hota aghr hum break statement ka astamaal kr k chalte loop ko stop krde(if its possible)

# without break statement with else statement
x2 = 0
while x2 < 6:
    print(x2)
    x2 += 1
else:
    print("Finally loop of 'x2' is end")

print("----")

# break statement with else statement
x3 = 0
while x3 < 6:
  x3 += 1
  if x3 == 3:  # here is the reason why the else block of code does not execute
    break
  print(x3)
else:
    print("Finally loop of 'x3' is end")

print("----")

# ___do while loop in python?___
# as we know k do while loop python may nhi hota likn hum do while jaisa logic bana sakhte hai
a = 10
while True:
    print(a)
    a = a + 1
    if(a >= 10):
        break
# yeh loop condition false hone pr bhi kam say kam ek bar to zahroor chalta hai jaise do while loop chalta hai

