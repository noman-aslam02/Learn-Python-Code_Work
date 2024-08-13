# # Operator Overloading (__mul__)
#
# # __mul__
# __eq__ method ka use do instance objects ko compare karne ke liye kiya jata hai
# jab aap == operator ka istemal karte hain
#
class EqClass:
    def __init__(self, x, y, z):
        self.__x = x  # Private variable
        self.__y = y  # Private variable
        self.__z = z  # Private variable

    def __str__(self):
        return f"{self.__x} {self.__y}, {self.__z}"  # Private variables ko display karne

    def __eq__(self, other):
        return (self.__x == other.__x and self.__y == other.__y and self.__z == other.__z)  # Objects ko compare karta hai
    # Aghr yaha Class ka use krte hai to humay 3 positional argument dene parenghay aur phir "and" k jagha comma (,) ka use hogha

# v1 aur v2 ke instances EqClass class ke __init__ method se banaye gaye hain
v1 = EqClass(10, 20, 9)
v2 = EqClass(10, 20, 9)
v3 = EqClass(3, 2, 3)
print(v1)  # (10, 20, 9)
print(v2)  # (10, 20, 9)
print(v3)  # (3, 2, 3)

# v1, v2 aur v3 objects ko compare "__eq__" method ka astamaal karke
print(v1 == v2)  # (10, 20, 9) == (10, 20, 9) Output: True
print(v1 == v3)  # (10, 20, 9) == (3, 2, 3) Output: False
