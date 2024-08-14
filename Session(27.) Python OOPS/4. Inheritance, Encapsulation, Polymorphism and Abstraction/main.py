# Inheritance, Encapsulation, Polymorphism and Abstraction

# ___Inheritance___
# Inheritance wo process hai jahan ek child class (subclass) parent class ki properties
# aur methods ko leti hai. Lekin agar humne child class may parent class ke kisi method ko
# modify kiya, toh yeh process "overriding" kehlata hai, aur isse inheritance nahi kehte.

# Python ki built-in class object hai. Jab hum koi class banate hain, wo object se inherit hoti hai
class Parent:  # Yeh Parent class hai
    def introduce(self):
        return "Vehicle is moving"  # Yeh Parent class ka method hai
class Child(Parent):  # Yeh Child class hai jo Parent class se inherit ho rahi hai
    pass  # Yahan humne koi method override nahi kiya, sirf Parent class ka method inherit kiya hai

my_obj = Child()  # Child class ka object banaya
print(my_obj.introduce())  # Child class ke object se Parent class ka method call kiya

# ab hum dono classes (Parent aur Child) ka constructor create kar rahe hain
# Constructor ko inherit nahi kar rahe
# yaha pr hum Child class k andar Parent class k constructor ko call nahi kar rahe
class Parent_WoClass:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Child_WoClass(Parent_WoClass):
    def __init__(self, name, age):  # modifying constructor
        self._name = name
        self._age = age

obj_Wo = Child_WoClass("raza", 99)
print(f"Name: {obj_Wo._name}", f"Age: {obj_Wo._age}")  # Child class

# Constructor ko inherit kar rahe hain
# yaha pr hum Child class k andar Parent class k constructor ko call kar rahe hain
class Parent_Class:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Child_Class(Parent_Class):
    def __init__(self, name, age):  # overriding constructor
        Parent_Class.__init__(self, name, age)  # calling parent constructor

Obj = Child_Class("NOMAN", 120)
print(f"Name: {Obj._name}", f"Age: {Obj._age}")  # Parent Class

# <><>super method<><>
# super method ka use kr k hum child class ka obj bana kr parent class ko call kar sakhte hai
# iskso hum child class may use krte hai
class Parent_Super:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Child_Super(Parent_Super):
    def __init__(self, name, age):  # overriding constructor
        super().__init__(name, age)  # calling parent constructor

obj_PS = Child_Super("Noman", 21)
print(f"The name of person is {obj_PS._name} and his age {obj_PS._age}")

# super and his mro method

class A:
    def __init__(self):
        print("A's constructor called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's constructor called")

class C(A):
    def __init__(self):
        super().__init__()
        print("C's constructor called")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D's constructor called")

obj = D()
# Yeh line Python ki MRO (Method Resolution Order) ko follow karti hai
print(D.__mro__)  # Yeh line saari classes ki MRO ko print karti hai

print("-----")

# ___Encapsulation___
# encapsulation say hum class k andr maujooda variables ko private rakh sakhte hai aur
# ussko sirif methods k zariay hi access kr sakhte hai

class MyVehicle:
    def __init__(self):
        self.__car_speed = 0  # yeh ek private attribute hai
        self.__bike_speed = 0  # yeh ek private attribute hai

    def car(self):
        print(f"The car speed is \"{self.__car_speed}\" ")  # accessing attribute through method

    def bike(self):
        print(f"The bike speed is \"{self.__bike_speed}\" ")  # accessing attribute through method

    def speed_up(self, c_speed=None, b_speed=None):  # speed booster method
        if c_speed is not None:
            self.__car_speed += c_speed
        if b_speed is not None:
            self.__bike_speed += b_speed

obj = MyVehicle()
# Directly accessing private attributes will raise an AttributeError
# print(obj.__car_speed)  # Yeh error cause karega q k hum directly access nahi kr sakhte
obj.car()  # abhi car ki speed 0 hai
obj.bike()  # abhi bike ki speed 0 hai
print(">>>Updated<<<")
# now we are updating speed of both vehicles
obj.speed_up(b_speed=120, c_speed=40)
obj.car()  # abhi car ki speed 40 hai
obj.bike()  # abhi bike ki speed 120 hai


print("-----")

# ___Polymorphism___
# Polymorphism wo concept hai jahan hum ek hi interface ya method ka use karke
# different types ke objects par operate kar sakte hain
class Mathematics:
    def math(self, a, b):
        print(a, b)
class Add(Mathematics):
    def math(self, a, b):
        print(a + b)
class Sub(Mathematics):
    def math(self, a, b):
        print(a - b)
class Divide(Mathematics):
    def math(self, a, b):
        print(a / b)
class Mul(Mathematics):
    def math(self, a, b):
        print(a * b)
"""def cal(mat_cal):
    mat_cal.math(15, 40)
cal(Addition)
cal(Subtraction)    # mrzi hai yeh bhi use kr sakhte hai but not good idea q k yeh kaafi bada hai
cal(Division)
cal(Multiply)"""

Addition = Add()
Subtraction = Sub()
Division = Divide()
Multiply = Mul()
# easiest way
for i in (Addition, Subtraction, Division, Multiply):
    i.math(15, 40)


print("____\nlets make polymorphism complex\n____")

# ___but hum short code likh rahe hai in "complex way" taa k samajh may bhi aey___
# k kiya ho raha hai code may
class Add():  # 'Add' class
    def operate(self, a, b):  # Addition ka method
        print(a + b)

class Sub():  # 'Sub' class
    def operate(self, a, b):  # Subtraction ka method
        print(a - b)

class Math_Operator:  # 'Math_Operator' class
    def __init__(self, class_name):  # Constructor
        self._operation = class_name  # Class object store kar raha hai
    def operating(self, a, b):  # Stored class ka 'operate' method call kar raha hai
       return self._operation.operate(a, b)

Addition = Add()  # 'Add' class ka object
Subtraction = Sub()  # 'Sub' class ka object

result_math = Math_Operator(Addition)  # 'Math_Operator' ka object 'Addition' object ke sath
result_math.operating(10,12)  # 'operating' method call kar raha hai

result_math = Math_Operator(Subtraction)  # 'Math_Operator' ka object 'Subtraction' object ke sath
result_math.operating(10,12)  # 'operating' method call kar raha hai

print("-----")

# ___Abstraction___
# 'abc' module hai, 'ABC' class hai aur 'abstractmethod' abstract method hai
# @abstractmethod ek decorator method bhi hai not just abstract method
from abc import ABC, abstractmethod

class CarInfo(ABC):
    @abstractmethod  # yeh abstract method hai class ka
    def c_name(self):  # Mercedes
        pass

    @abstractmethod  # yeh abstract method hai class k
    def c_color(self):  # Grey
        pass

    @abstractmethod  # yeh abstract method hai class k
    def c_body(self):  # AHSS
        pass
class CarDetails(CarInfo):
    # yaha saaray methods ki implementation ki gaey hai
    def c_name(self):
        return "Mercedes"
    def c_color(self):
        return "Grey"
    def c_body(self):
        return "AHSS"


car = CarDetails()
print("The name of car is", car.c_name())
print("Body color:", car.c_color())
print("Body Type:", car.c_body())