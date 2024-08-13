# Enumerate Function in Python

fruits = ["apple", "orange", "kiwi", "orange", "avocado", "pineapple"]
index = 0
for fruit in fruits:
    print(fruit)
    if index == 3:
        print("Yes index has been reached")
        break
    index += 1

print("____or____")

# ya phir kuch iss tareeqay say bhi kr sakhte hai
fruits = ["apple", "orange", "kiwi", "orange", "avocado", "pineapple"]
for fruit in range(len(fruits)):
    print(fruits[fruit])
    if fruit == 3:
        print("Yes index has been reached")
        break

print("-----")

# isska asaan tareeqa yeh hai k hum "enumerate" function ka use karen

# ___enumerate()____
# enumerate() function hamay hr element k saath saath usska index bhi nikal kr deti hai
fruits = ["apple", "orange", "kiwi", "orange", "avocado", "pineapple"]
for index, fruit in enumerate(fruits):
    print(fruit)
    if index == 3:
        print("Yes index has been reached")
        break