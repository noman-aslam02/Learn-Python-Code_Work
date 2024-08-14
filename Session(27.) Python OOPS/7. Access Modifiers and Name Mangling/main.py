# Access Modifiers and Name Mangling

# ___Public Variables___
# yeh kahi kahi bhi access kiye jaa sakhte hai, freely accessable hai
class PublicExample:
    def __init__(self, value):
        self.public_var = value  # Public variable, jo kahin bhi freely access ho sakta hai

    def get_public_var(self):
        return self.public_var  # Public variable ka value return karta hai

example = PublicExample(30)
print(example.get_public_var())

# Direct access possible aur recommended hai
print(example.public_var)

print("-----")

# ___Protected Variables___
class BaseProtected:
    def __init__(self, value):
        self._protected_var = value  # Protected variable, jo derived classes mein access ho sakta hai

class DerivedProtected(BaseProtected):
    def __init__(self, value):
        super().__init__(value)

    def get_protected_var(self):
        return self._protected_var  # Base class ke protected variable ko access kar raha hai

example = DerivedProtected(20)
print(example.get_protected_var())

# Direct access possible hai lekin recommended nahi hai
print(example._protected_var)

print("-----")

# ___Private Variables___
class PrivateExample:
    def __init__(self, value):
        self.__private_var = value  # Private variable, jo sirf class ke andar access hota hai

    def get_private_var(self):
        return self.__private_var  # Private variable ka value return karta hai

example = PrivateExample(10)
print(example.get_private_var())

# yeh hum nay "name mangling" k tareeaay say private variable ko access kiya hai
# <-------------------!!! not recommended !!!------------------->
print(example._PrivateExample__private_var)  # name mangling allow us to access variable

# Direct access nahi ho sakta
# print(example.__private_var)  # Yeh AttributeError dega
