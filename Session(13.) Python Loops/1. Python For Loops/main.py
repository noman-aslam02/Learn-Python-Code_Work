# Python For Loops

# ___Simple way of iterating on string using for loop___
# Looping Through a String
for i in "Noman":  # 'i' ek variable hai, 'in' jo k assign krwa raha hai sequence of characters ko 'i' say
    print(i)
# i in "Noman", yeh ek ek string character ko print karegha gha one by one

# ___Index in for loop___
# without index
fruits = ["Apple", "Banana", "Cherry"]
for a in fruits:  # yaha hamay index dene ki zahroorat nhi, yeh kudhi iterate krta hai saray sequence of elements ko
    print(a)

# with index
fruits1 = ["Apple", "Banana", "Cherry"]
for aa in range(len(fruits1)):  # yaha hum nay sequence of elements k range pr print kara hai yaani jitni length hoghi utna hi specific number of times pr print hogha
    print(fruits1[aa])  # here we used index taa k hum hr elemetns ko call kr sakhe
# 'range' wala topic aap neechay scroll kr k phr sakhte hai

# ___The break Statement___
# Break Before the print
cars = ["Toyota", "Suzuki", "LGBTQ", "Alto"]
for car in cars:
    if car == "LGBTQ":
        break
    print(car)

# Break After the print
cars1 = ["Toyota", "Suzuki", "LGBTQ", "Alto"]
for car1 in cars1:
    print(car1)
    if car1 == "LGBTQ":
        break

print("------")
# ___Continue Statement___
cars2 = ["Toyota", "Suzuki", "LGBTQ", "Alto"]
for car2 in cars2:
    if car2 == "LGBTQ":
        continue
    print(car2)
# rule : continue statement hamesha before print use hota hai wrna yeh skip nhi krta sequence of character ya elements ko


# ___range() function___
"""
yeh tab kaam ata hai jab aapko kssi range may numbers print krne ho ya phir aapko sequence of
elements ya characters ko iterate krwana ho aur kssi specific position say start ya end
krna ho to range() function ka use hota hai
Summarize:
Agar humein koi code bar bar chalana ho, toh hum range() ka istemal kar sakte hain
"""

# single value in range() function parameter
for xx in range(5):  # by default yeh 0 say hi start hota hai
    print(xx)
# remember last number kabhi bhi print nhi hota

print("------")

# double values in range() function parameter
# aghr humay kssi specific position say start krna hai to hum kuch yeh code likhenghay
for xx1 in range(2, 8):  # (2, 8) iss may '2' starting position hai aur '8' ending position
    print(xx1)

print("------")

# triple value in range() function parameter
"""
by default range() function may 1 say increment hoti hai jab iterate krta hai yeh sequence pr
to hum kudh say bhi changes kr sakhte hai
"""
for xx2 in range(1, 15, 3):  # (1, 15, 3) iss may '1' starting position hai aur '15' ending position aur '3' increment bata raha hai kitna rakhna hai iterate krte waqt
    print(xx2)

print("----")

# ___Else in For Loop___
# else without break in for Loop
for number in range(6):
    print(number)
else:
    print("Finally finished")
# Rule
# aghr 'for' loop pura run ho jaye bina kisi break statement ke to 'else' block run hoga

print("----")

# else with break in for Loop
for number1 in range(6):
    if number1 == 7:
        break
    print(number1)
else:
    print("Finally finished")

# another example
if 3 in range(6):
    for number1 in range(6):
        print(number1)
        if number1 == 3:
            break
else:
    print("huraaaa")

print("-----")

# ___Nested Loops___
adj = ["Small", "Medium", "Large"]  # outer loop's part
fruits = ["Apple", "Banana", "Cherry"]  # inner loop's part
for x111 in adj:  # outer loop
    for y111 in fruits:  # inner loop
        print("Size:", x111, y111)
# Rule
# inner loop one time execute krta ho for each outer loop

# ___pass Statement___
# aghr hamaray paas koi content nhi hai likhne ko for loop may to hum 'pass' keyword ka use krte hai to avoid getting errors
for x in range(10):
    pass
