# __str__,  __repr__ etc, dunder function and eval function

# ___(__repr__ and __str__)___

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return str(f"Car name: \"{self.name}\", color: \"{self.color}\"")

    def __repr__(self):
        return f"Car(\'{self.name}\', \'{self.color}\')"

Toyota = Car("Toyota", "Yellow")
# print(Toyota)  # yeh by default str ko hi print karegha
print(str(Toyota))  # yeh string representation k liay hai (print)
e = repr(Toyota)  # yeh debugging representation k liay hai (Developers)
print(e)
# print(eval(e))  # yeh object ko recreate karega

print("-----")

# ___main difference yaha dekhne ko milegha___
import datetime

date_time = datetime.datetime.now().astimezone()

print(str(date_time))  # str se datetime ko string mein convert kiya
print(repr(date_time))  # repr se datetime ka detailed output mila

print("-----")

# ___eval function___
# eval function se hum kisi bhi string expression ko evaluate karke execute kar sakte hain

# Example 1: Mathematical expression
expression = "2 + 4 * 4"
print(expression)  # normal execution (string output)
print(eval(expression))  # eval execution (result output: 18)

# Example 2: Function call
my_name = "Muhammad Noman Aslam"

def greet():
    print("Hello {}!     Have a great day today.".format(my_name))

fun_expression = "greet()"
eval(fun_expression)  # eval execution (calls the greet function)

print("-----")

# yeh code dekh kr aap apni basic understanding theek kare k yeh class method
# self, cls yeh sab kaysay kaam krte hai

class Employee:
    company = "Apple"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

# Creating two instances
e1 = Employee("Harry")
e2 = Employee("Tom")

# Showing the company for both instances
e1.show()  # Output: The name is Harry and company is Apple
e2.show()  # Output: The name is Tom and company is Apple

# Changing company using class method
Employee.changeCompany("Tesla")

# Showing the company for both instances after change
e1.show()  # Output: The name is Harry and company is Tesla
e2.show()  # Output: The name is Tom and company is Tesla

print("-----")

# ___(__len__)___

"""
class LenClass:
    def __init__(self, data):
        self.data = data
        self.name = "Muhammad Noman Aslam"
        # yaha hum nay length method nahi banaya issliay yeh error throw huwa hai

obj_len_try = LenClass("Employee")
print(len(obj_len_try))  # TypeError: object of type 'LenClass' has no len()
"""
class LenClass:
    def __init__(self, data):
        self.data = data
        self.name = "Muhammad Noman Aslam"

    def __len__(self):  # here we created length method
        return len(self.data)

obj_len = LenClass([1,2,3,4,5,6])  # integer list (elements)
print(obj_len, "- printed object's memory address")
print("the length of object is: ",len(obj_len))  # calling len function
obj_len1 = LenClass("Nomi")  # string value
print("the length of object is: ",len(obj_len1))  # calling len function

print("-----")

# ___(__call__)___

class CallClass:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __call__(self):  # here we created call method
        print("i am callable object")

obj_call = CallClass("Muhammad Noman Aslam", 1429309)
obj_call()  # yaha hum nay obj ko as function ki thara call kiya () use kr k
# yeh commas k andr name ko print karegha with single {} curly bracket
print(f"The student id of { {obj_call.name} } is :{obj_call.id}")
# aur yeh without commas with single {} curly bracket
print(f"The student id of {{ {obj_call.name} }} is :{obj_call.id}")