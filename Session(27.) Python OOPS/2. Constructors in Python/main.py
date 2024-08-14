# Constructors in Python

# ___"__init__"___
# __init__ class ka "constructor" hota hai jisse hum attributes ko arguments ke roop mein
# pass kar sakte hain, yeh dynamically attributes bn jate matlab bar hr object k liay
# alag alag value rakh sakhte hai

# "class k attribute" jo by default rakhe jate hai wo static hote hai yaani sab obj k liay
#  same hote hai

class MyClass:  # Class create karna
    gender = "prefer not to say gender"  # yeh class k attribute hote hai
    def __init__(self, name, age):  # yeh constructor hai
        print("this is default constructor")  # aghr method na bhi call ho to yeh print hogha
        self._name = name  # Yeh attribute hai jis mein 'name' variable pass kiya gaya hai
        self._age = age    # Yeh attribute hai jis mein 'age' variable pass kiya gaya hai
        # yeh "self._name" aur "self._age" instance attribute hote hai

    def info(self):
        # Yeh method class ke attributes ko print karta hai
        print(f"The person name is {self._name} and age is {self._age} and gender is \"{self.gender}\" ")

# Object creation aur uske attributes ko initialize karna
obj = MyClass("Muhamad Noman Aslam", 21)
print("Person 1")
obj.info()
obj1 = MyClass("Syed Noor", 19)  # yeh dusra percent bn gaya
# Object ke 'info' method ko call karna taake attributes print ho jaye
obj1._name = "Noor Noman"  # hum update bhi kr sakhte hai
print("Person 2")
obj1.info()
# now we edit gender of both person, person 1 is "obj" and person 2 is "obj1"
print("\n----->we revealed gender<-----")
m = MyClass.gender = "Male"  # yeh gender sab object(instance) pr same rahegha
print("Person 1")
obj.info()
obj1.gender = "Female" # yaha hum nay person 2 k liay female rakh diya "wrna yeh male ho jata"
print("Person 2")
obj1.info()