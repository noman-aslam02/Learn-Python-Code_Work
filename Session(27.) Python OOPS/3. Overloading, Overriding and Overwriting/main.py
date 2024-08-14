# Overloading, Overriding and Overwriting


# ___Overloading___
# overloading python may support nahi hai but hum different arguments k
# saath same function use kr sakhte hai

def sum_numbers(x, y, z = None):
    if z == None:  # aghr "z" value nahi di to yeh "None" value degha
        print(x + y)
    else:
        print(x , y , z)  # Agar 3 values di gayi hain to yeh teeno print karega, add nahi
# use function multiple times
sum_numbers(1,2)  # here we gives two arguments "output: (3)"
sum_numbers(1,2,4)  # here we gives three arguments "output: (1 2 4)"

print("-----")

# ___Overriding___
# overriding python may parent class ka structure child class may use krne k liay kaam ata hai
# taa k hum uss code ko modidy kr sakhe

class Parent:
    def __init__(self):
        print("hey, I am parent class")
    def numbers(self):
        print(2 + 4)

class Child(Parent):  # Child class Parent class se inherit kar rahi hai
    def __init__(self):
        print("hey, I am child class")
    def numbers(self):  # Parent class ke numbers method ko override kar rahi hai
        print(2 * 4)

obj_overrides = Parent()  # yeh call karte hi constructor ka block of code execute ho jayega
obj_overrides.numbers()   # Output: 6

obj_overrides = Child()   # yeh call karte hi constructor ka block of code execute ho jayega
obj_overrides.numbers()   # Output: 8

print("-----")

# ___Overwriting___
# overwriting ek variable ki value ko update krta hai
my_name = "Noman"
my_name = "Ali"  # updated
print(my_name)  # Output: Ali