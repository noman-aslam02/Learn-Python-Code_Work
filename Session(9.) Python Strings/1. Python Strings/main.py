# Python Strings

# ___String Literal___
print("Hi, My name is Muhammad Noman Aslam")

# ___Non String Literal___
person = "Hi, My name is Muhammad Noman Aslam"
print(person)

print("----------")
# Multiple line of Strings
# ___Triple Single or Double Quote String___
para = """Musk joined the social media service Twitter in 2009,
and, as @elonmusk, he became one of the most popular
accounts on the site, with more than 85 million
followers as of 2022."""
print(para)
print("----------")

# ___String Arrays___
x = "Nomi"
# how it looks in index
# N [0]
# o [1]
# m [2]
# i [3]
print(x[0])  # index 0 will print N

# ___Looping Through a String___
# "loop" use krne ka faida yeh hai k hum ek hi bar may sab index ko print kr sakhte hai
# Example
for z in "banana":
    print(z)
print("and")
# another way
aa = "apple"
for z1 in aa:
    print(z1)

# ___String Length___
# use len() function to know the length of string
info = "i am length of string"
print(len(info))

# ___String Count___
#yeh numbers of values ko return kr k bateygha k kitni bar repeat ho raha hai
count_test = "I am man man and superman"
print(count_test.count("man"))  # return 3

# Check String
# "in" keyword maujoodgi ya na hona check karne ke liye istemal hota hai
# ___in___
exist = "Python is free"
print("free" in exist)
# another way
exist1 = "Python is free"
if "free" in exist1:
    print("Yes, free word exist krta hai")
else:
    print("Doesn't exist")

# ___not in___
# isska result hota hai
not_exist = "Python is free"
print("free" not in not_exist)
# another way
not_exist1 = "Python is free"
if "free" not in not_exist1:
    print("Yes, free word exist krta hai")
else:
    print("Doesn't exist")