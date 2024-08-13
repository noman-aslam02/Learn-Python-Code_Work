# # Operator Overloading (__sub__)
#
# # __sub__
# # __sub__ method ka use do instance objects ko sub karne ke liye kiya jata hai
# # jab aap - operator ka istemal karte hain
#
class SubClass:
    def __init__(self, x, y, z):
        self.__x = x  # Private variable
        self.__y = y  # Private variable
        self.__z = z  # Private variable

    def __str__(self):
        return f"{self.__x} {self.__y}, {self.__z}"  # Private variables ko display karne

    def __sub__(self, other):
        return SubClass(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)  # naya SubClass object return karta hai

# v1 aur v2 ke instances SubClass class ke __init__ method se banaye gaye hain
v1 = SubClass(11, 20, 33)
v2 = SubClass(3, 4, 5)
print(v1)
print(v2)
# v3 object v1 aur v2 ko sub "__sub__" method ka astamaal karke banaya gaya hai
v3 = v1 - v2
print(v3)