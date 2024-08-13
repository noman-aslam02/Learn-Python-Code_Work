# Python - Access Set Items

# ___Access Set Items___
# hum set k items ko access nahi kr sakhte direct index say, they are unindexed
"""
fruit = {"apple", "cherry", "avocado"}
print(fruit[0:1])  # yeh error throw karegha q k items unordered hote hai sets may
"""

# but hum set k items ko access kr sakte hai for loop ka astamaal kr kr
# aur yeh kssi bhi order may print ho sakhte hai
fruit = {"apple", "cherry", "avocado"}
for i in fruit:
    print(i)

print("-----")

# ___in___
# in keyword ka use kr hum check kr sakhte hai k yeh item majood hai ya nahi set may
fruit = {"apple", "cherry", "avocado"}
print("banana" in fruit)  # yeh as a boolean return karegha

fruit = {"apple", "cherry", "avocado"}
print("banana" not in fruit)  # yeh as a boolean return karegha