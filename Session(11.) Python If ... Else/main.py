# If ... Else

# ___If Statement___
# yeh just specific condition ko check kr raha hai
x = 200
y = 40
if x > y:
    print("Yes 'x' is is greater than 'y'")

print("-----")

# ___Indentation___
# yeh ek basic behaviour hai python ka
# iss may space ya tab ka use hona zahroori hai
# ---------------------- It just rule, first focus on statement then read this (Its up to you)------
apple = 40
budget = 200
if budget >= apple * 4:
    print(f"Add 4 kg in the cart")
else:
    print("Your budget is low")
# yaha bs single space tha jo k indentation k according nhi tha tha
# aur yeh if and else k statement may nhi ja raha issliay error throw kiya
 # print("Mujhey bhi print krdo :(") so this is wrong, space or tab should be given


# likn aghr hum without space likhenghay to obviously wo direct print hogha
# depend nhi rehta yeh kssi pr bhi
# Example
print("May to hamesha print ho jata ho")

print("-----")

# ___Elif Statement___
# aghr 'if' statement false ho jaey to 'elif' print hoo jaeygha
x1 = 200
y1 = 200
if x1 > y1:
    print("Yes, 'x1' is is greater than 'y1'")
elif x1 == y1:
    print("No, 'y1' is equal to 'x1'")

print("-----")

# ___Else Statement___
# aghr 'if' ya 'elif' statement false ho jaey to 'else' print ho jaeygha
x2 = 200
y2 = 400
if x2 > y2:
    print("Yes, 'x2' is is greater than 'y2'")
elif x2 == y2:
    print("No, 'y2' is equal to 'x2'")
else:
    print("No Bro, 'y2' is greater than 'x2'")

print("-----")

# ___else without elif___
x3 = 200
y3 = 400
if x3 > y3:
    print("Yes, 'x3' is is greater than 'y3'")
else:
    print("No, 'y3' is greater than 'x3'")

print("-----")

# ___Short Hand If___
# ___One Line Statement___
# aghr hamaray paas sirif ek hi statement ho likhen k liay to hum yeh step karenghay
aa = 10
bb = 20
if aa < bb: print("'bb' is greater than 'aa'")

print("-----")

# ___Short Hand If ... Else___
aa1 = 10
bb1 = 20
print("aa1 is greater number") if aa1 > bb1 else print("bb1 is greater number")
# This technique is known as Ternary Operators, or Conditional Expressions
# You can also have multiple else statements on the same line
a = 10
b = 20
print("A is best") if a > b else print("B is best") if a < b else print("'a' is equal to 'b'")

print("-----")

# ___and logical Operator____
# dono conditions ka True hona zahroori hai tabhi code execute hogha
# yaani 'and' say phele (abc > cba) aur 'and' k baad wale (cba < xyz) dono True zahroor ho
abc = 45
cba = 30
xyz = 60
if abc > cba and cba < xyz:
    print("Both conditions are True")

print("-----")

# ___or logical Operator____
# iss may sirif ek condition ka True hona zahroori hai
abc1 = 45
cba1 = 30
xyz1 = 60
if abc1 > cba1 or cba1 > xyz1:
    print("At least one condition is True")

print("-----")

# ___not logical Operator____
# yeh ulta faisla leta hai true ko false ya false ko true krdegha
abc3 = 45
cba3 = 30
xyz3 = 60
if not (abc3 < cba3 and cba3 > xyz3):
    print("Both conditions are True")

# or simple way

abc4 = 30
cba4 = 40
if not abc4 > cba4:
    print("Yes, condition is true :)")

print("-----")

# ___Nested If___
# Nested if ka matlab if k andr if statement dena

num = 0

if num >= 0:
    print("number is above 0")
    if num == 0:
        print("Paida to hogha sahi say")
    elif num < 18:
        print("You are too young")
    elif (num >= 18) and (num <= 70):
        print("You are 18 plus")
    else:
        print("You are very old")
else:
    print("Number is negative")

print("-----")

# ___The pass Statement___
# aghr if statement may koi content majood nhi to pass ka use kr k error say bach sakhte hai
var_1 = 33
var_2 = 200

if var_1 > var_2:
  pass  # throw an error without the pass statement
else:
    print("bach gaya may 'pass' statement ki wajah say")
