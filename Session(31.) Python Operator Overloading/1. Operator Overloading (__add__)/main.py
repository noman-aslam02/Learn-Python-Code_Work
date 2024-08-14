# # Operator Overloading (__add__)
#
# # __add__
# # __add__ method ka use do instance objects ko add karne ke liye kiya jata hai
# # jab aap + operator ka istemal karte hain
#
class AddClass:
    def __init__(self, x, y, z):
        self.__x = x  # Private variable
        self.__y = y  # Private variable
        self.__z = z  # Private variable

    def __str__(self):
        return f"{self.__x} {self.__y}, {self.__z}"  # Private variables ko display karne

    def __add__(self, other):
        return AddClass(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)  # naya AddClass object return karta hai

# v1 aur v2 ke instances AddClass class ke __init__ method se banaye gaye hain
v1 = AddClass(1, 2, 6)
v2 = AddClass(3, 4, 5)
print(v1)
print(v2)
# v3_1 object v1_1 aur v2_1 ko add "__add__" method ka astamaal karke banaya gaya hai
v3 = v1 + v2
print(v3)

print("-----")

# now we are doing without __str__ method just for practicing
class AddClass1:
    def __init__(self, x1, y1, z1):
        self.x1 = x1  # instance ka attribute
        self.y1 = y1  # instance ka attribute
        self.z1 = z1  # instance ka attribute

    def __add__(self, other):
        return AddClass1(self.x1 + other.x1, self.y1 + other.y1, self.z1 + other.z1)  # naya AddClass1 object return karta hai

# v1 aur v2 AddClass1 ke objects hain
v1_1 = AddClass1(1, 2, 6)
v2_1 = AddClass1(3, 4, 5)
print(v1_1.x1, v1_1.y1, v1_1.z1)
print(v2_1.x1, v2_1.y1, v2_1.z1)

# v3_1 object v1_1 aur v2_1 ko add "__add__" method ka astamaal karke banaya gaya hai
v3_1 = v1_1 + v2_1
print(v3_1.x1, v3_1.y1, v3_1.z1)


"""
good example hai k hum Class ka use q krte hai function may chaa hay wo koi sa bhi q na ho

    def add_n(self, other):
        return AddClass(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)  # naya AddClass object return karta hai
    
    print(v1.add_n(v2))
"""