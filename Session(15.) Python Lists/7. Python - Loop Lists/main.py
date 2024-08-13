# Python - Loop Lists

# ___Loop Through a List___
# hum for loop ka bhi astamaal kr k list k hr elements ko print kr sakhte hai
fruits = ["apple", "pineapple", "kiwi", "strawberry"]
for i in fruits:
    print(i)

print("-----")

# ___Loop Through the Index Numbers___
# hum for loop say list items ko print kr sakhte hai using index
fruits = ["apple", "pineapple", "kiwi", "strawberry"]
for i in range(len(fruits)):
    print(fruits[i])

print("-----")

# ___Using a While Loop___
"""
yeh while loop hr list items ko print kr raha hai aur jab takh kregha jab takh
isski value satisfy na ho jaey k yeh "i" less than iss list ki length k hai yaa nhi
"""
fruits = ["apple", "pineapple", "kiwi", "strawberry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print("-----")

# ___Looping Using List Comprehension___
# yeh one line statement hai jssko hum List Comprehension kehte hai
# yeh easily one line may for loop ka use kr k hr items ko print kr deta hai
fruits = ["apple", "pineapple", "kiwi", "strawberry"]
[print(x) for x in fruits]