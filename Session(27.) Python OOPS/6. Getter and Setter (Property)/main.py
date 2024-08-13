# # Getter and Setter (Property)
#
# # ___Without getter and setter method
# # yeh kuch normal code hai jo hum krte hai (its not getter and setter)
# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def get_value(self):
#         print(f"Getter: I am {self._value} Coder")
#
#     def set_value(self, name):
#         self._value = name
#         print(f"Setter: My name is {self._value}")
#
# obj = MyClass("Pro")
# obj.get_value()
# # jab aap obj.get_value = "Hello" likhte hain, to aap actually get_value method ko overwrite kar
# # rahe hain ek nayi value “Hello” ke sath.Ab get_value ek string hai, na ke method
# obj.get_value = "Getter: Hello <----- Getter value has been updated"
# print(obj.get_value)
# obj.set_value("Muhammad Noman Aslam")
#
# print("\n-----\n")
# # ___Getter and Setter using @property___
# class MyGetterSetter:  # class
#     def __init__(self, value):
#         self.__value = value
#
#     @property  # Yeh decorator private variables ko access karne ke liye istemal hota hai
#     def get_value(self):  # Yeh getter method hai jo "self._value" ki value return karta hai
#         return f"Getter: I am {self.__value} Memer"
#
#     # yeh override kregha Property method "get_value" ko, yeh bhi getter jaisa kaam krta hai
#     # we did just for knowledge
#     """
#     @get_value.getter
#     def get_value(self):
#         return f"Getter to Getter: I am {self.__value} Memer"
#     # override method bs modify kregha old property method ko, wrna yeh zada kaam nahi ata
#     """
#
#     @get_value.setter  # Yeh decorator variable ki value set karne ke liye istemal hota hai
#     def get_value(self, value):  # Yeh setter method hai jo "self._value" ki value set karta hai
#         self.__value = value
#         print(f"Setter: I am {self.__value} Memer <----- Getter value has been updated through setter method")
#
#     @get_value.deleter
#     def get_value(self):  # Yeh deleter method hai jo "self._value" ki value delete karta hai
#         print(f"Deleter: I am {self.__value} Memer <----- Getter value has been deleted through deleter method")
#         del self.__value
#
# # "MyGetterSetter" class ka object banaya gaya
# obj_GS = MyGetterSetter("PRO")  # "PRO" value ko "self._value" variable mein set kiya gaya
# # getter method ko call kiya hai
# print(obj_GS.get_value)  # yeh override method ko call kregha q k "@get_value.getter" use kiya hai
# # setter method ko call kiya hai
# obj_GS.get_value = "Professional"
# # deleter method ko call kiya hai
# del obj_GS.get_value
#
# # checking, is "obj_GS" exist or not
# try:
#     if obj_GS.get_value is not None:
#         print(obj_GS.get_value)
# except:
#     print("Object \"obj_GS\" has been deleted through deleter method")

class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def area(self):
        return self._x * self._y
class Circle(Shape):
    def __init__(self, x, y, radius):
        print("start")
        self.radius = radius
        super().__init__(x, y)
        print("end")

    def area(self):
        return 3.14 * super().area() + self.radius

obj_circle = Circle(10, 10, 10)
print(obj_circle.area())