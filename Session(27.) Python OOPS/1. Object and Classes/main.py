# Python OOPS

# ___class__
# python may "class" use kr k hum objects bana sakhte hain
class MyClass:  # yeh class hai
    my_name = "Muhammad Noman Aslam"
    my_age = 99


# `"<class '__main__.MyClass'>"` ka matlab hai ke yeh class wahi define hui hai jahan se yeh code chal raha hai
print(MyClass)  # output : <class '__main__.MyClass'>

print("-----")


# __object__
# python may hum "object" jo k class ka instance hote hai, isski madad say hum properties aur
# method ko call kr sakhte hai

class MyClass:
    my_name = "Muhammad Noman Aslam"
    my_age = 99


per1 = MyClass()
print(per1.my_name, per1.my_age)
per2 = MyClass()
per2.my_name = "Ahsan CR"
per2.my_age = 90
print(per2.my_name, per2.my_age)

print("-----")


# __method and 'self' keyword
# method hum class k andr define krte hai aur self instance ko refer krta hai
# code ko dekh kr hum saari cheezay samjhe ghay

class MyClass:
    my_car = "BMW"  # yeh attribute hai, attribute matlab kssi name k corresponding value ho
    house_color = "Orange"  # attribute

    def my_method(self):  # yeh method hai
        print(f"my car name is {self.my_car} and his color is {self.house_color}")


# creating object (instance)
my_obj = MyClass()
my_obj.my_method()

# ab hum yaha pr new cars add kr sakhte hai yeh (yeh isska main faida hai)
my_obj1 = MyClass()
my_obj1.my_car = "Toyota"  # hum nay just value replace kri
my_obj1.house_color = "Blue"  # hum nay just value replace kri
my_obj1.my_method()  # ab yeh full line likh degha value replacement k saath
