# Static Method and cls

# Static Method
# Static Method method instance variables aur class variables pr independent hote hai bilkul
# issko hum instance ya class name dono k naam say call kr sakhte hai


class StaticClass:
    # mera_naam_dude = "noman" issko access nahi kr sakhte hai Static class may
    @staticmethod
    def static_method():  # yeh ek static method hai
        return "This is static method"

    @staticmethod
    def add(x, y):  # yeh ek static method hai
        return x + y


# yaha hum nay class ka reference banaya hai jss ka naam "sm_reference"
sm_reference = StaticClass
print("---> static method reference<---")
# iss method ko class reference ke zariye access kiya hai
# ya phir class ka naam de kr bhi access kr sakhte hai
print("With_Reference:", sm_reference.static_method())
# iss method ko seedha class naam ke zariye access kiya hai
print("With_Reference:", StaticClass.add(10, 110))

print("\n---> static method object<---")
# yaha hum nay instance say bhi access kiya hai jss ka naam hai "obj_sm"
obj_sm = StaticClass()
print("With_Object:", obj_sm.static_method())
print("With_Object:", obj_sm.add(10, 110))

print("\n-----\n")

# ___Class Method (cls)___
# class method say hum class variables aur class method ko call kr sakhte hai
# issko hum instance ya class name dono k naam say call kr sakhte hai


class ClassMethod:
    mera_naam = "Muhammad Noman Aslam"  # yeh ek 'class variable' hai

    @classmethod
    def myname(cls):
        return cls.mera_naam

    @classmethod
    def class_method(cls):  # yeh ek 'class method' hai
        return "This is class method"

    @classmethod
    def add(cls, x, y):  # yeh ek 'class method' hai
        return x + y


# yaha hum nay class ka reference banaya hai jss ka naam "cm_reference"
cm_reference = ClassMethod
print("---> class method reference<---")
# iss method ko class reference ke zariye access kiya hai
# ya phir class ka naam de kr bhi access kr sakhte hai
print("With_Reference:", cm_reference.myname())
# iss method ko seedha class naam ke zariye access kiya hai
print("With_Reference:", ClassMethod.class_method())
print("With_Reference:", ClassMethod.add(10, 110))

print("\n---> class method object<---")
# yaha hum nay instance say bhi access kiya hai jss ka naam hai "obj_cm"
obj_cm = ClassMethod()
print("With_Object:", obj_cm.myname())
print("With_Object:", obj_cm.class_method())
print("With_Object:", obj_cm.add(10, 110))

print("\n-----\n")


# __instance variables (self)___
class InstanceClass:
    amount = 111000  # class variable
    def __init__(self):
        self.amount = 1000  # instance variable
    def instance_method(self):
        print(f"This is an instance method {self.amount}")

print("---> instance method object<---")
# Object bana rahe hain
inst_obj = InstanceClass()

# Instance method ko object ke through call kar rahe hain (auto self)
inst_obj.instance_method()

print("\n---> instance method reference<---")
# Instance method ko class ke through call kar rahe hain (manual self)
InstanceClass.instance_method(inst_obj)