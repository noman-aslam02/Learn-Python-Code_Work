# List Comprehension in Python

# ___Without List Comprehension___

# yeh just normal list hai jss may hum nay koi changes nhi kri hai
# maynay just list print krdi for understanding
fruits = ["apple", "Cherry", "banana", "Mango", "Kiwi", "avocado"]
print(fruits)

print("----------------------------------------------------------")

# here we will do "Without List Comprehension"
fruits = ["apple", "Cherry", "banana", "Mango", "Kiwi", "avocado"]
new_fruits_list = []
for x in fruits:
    if x != "apple":
        new_fruits_list.append(x)
print(new_fruits_list)

print("----------------------------------------------------------")

# ___List Comprehension___
# yaha hum List Comprehension ka use karenghay
# without if statement k bhi ho sakhta hai yeh "List Comprehension"

fruits = ["apple", "Cherry", "banana", "Mango", "Kiwi", "avocado"]
# yeh syntax hai list comprehension ka jo one line statement may khatam hoti hai
new_fruit = [x for x in fruits if len(x) > 5 and x[0].islower()]
print(new_fruit)

print("----------------------------------------------------------")

# without if statement
fruits = ["apple", "Cherry", "banana", "Mango", "Kiwi", "avocado"]
# yeh syntax hai list comprehension ka jo one line statement may khatam hoti hai
new_fruit = [x for x in fruits]
print(*new_fruit, "<--------- Without if statement")

print("----------------------------------------------------------")

# lets make it complex

s = ["apple", "Cherry", "banana", "Mango", "Kiwi", "avocado"]
# first iss nay shuru hr work k first letter ko upper case pr kara
print(s)
"""
phir iss k baad hr string may majood hr k word k shuru k 1st letter ko lower case kr k agay k 
sab characters ko same wohi rehne diya
"""
new_s = [word[0].lower() + word[1:] for word in s]
print(*new_s)  # Output: "hello world"

print("----------------------------------------------------------")

s = "hello world Old"
# first iss nay shuru hr work k first letter ko upper case pr kara
s = s.title()  # Convert to title case first
print(s)
print(s.split())
new_s = [word[0].lower() + word[1:] for word in s.split()]  # to basically yeh "s.split()" string say hr words ko alagh alagh strings may nikal kr ek naeyi list may daal raha hai
print(*new_s)  # Output: "hello world"


print("----------------------------------------------------------")
#little bit more complex
s = "Billo raaani"
# first iss nay shuru hr work k first letter ko upper case pr kara
print(s.split())
new_s = " " .join(word[0].lower() + word[1:] for word in s.split())
print(new_s)  # Output: "hello world"

print("----------------------------------------------------------")
# simple and better understanding
print("simple and better understanding")
newlist = [x for x in range(10)]
print(newlist)
newlist = [x*2 for x in range(10)]  # multiply of each iteration into new list
print(newlist)
newlist = [x**2 for x in range(10)] # square of each iteration into new list
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x for x in range(10) if x > 5]
print(newlist)

print("----------------------------------------------------------")
#complex
newlist = [x for x in range(10) if x < 5]
# aghr yeh "if x < 5" less than 6 naa hota to yeh else pr chala jata
if len(newlist) < 6:
    print('Yes length is lower than 6')
else:
    print("NO, :(")

print("----------------------------------------------------------")
# Bonus code
print("Bonus code")

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = ["orange" if x == "banana" else x for x in fruits1]
print(newlist1)

print("or")

print("we switched object, banana ko change kr k orange pr set krdiya")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


