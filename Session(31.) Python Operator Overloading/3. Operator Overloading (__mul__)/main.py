# # Operator Overloading (__mul__)
#
# # __mul__
# # __mul__ method ka use do instance objects ko mul karne ke liye kiya jata hai
# # jab aap - operator ka istemal karte hain
#
class MulClass:
    def __init__(self, x, y, z):
        self.__x = x  # Private variable
        self.__y = y  # Private variable
        self.__z = z  # Private variable

    def __str__(self):
        return f"{self.__x} {self.__y}, {self.__z}"  # Private variables ko display karne

    def __mul__(self, other):
        return MulClass(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)  # naya MulClass object return karta hai

# v1 aur v2 ke instances MulClass class ke __init__ method se banaye gaye hain
v1 = MulClass(10, 20, 9)
v2 = MulClass(3, 2, 3)
print(v1)
print(v2)
# v3 object v1 aur v2 ko mul "__mul__" method ka astamaal karke banaya gaya hai
v3 = v1 * v2
print(v3)