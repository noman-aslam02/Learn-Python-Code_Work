# Python dir, __dict__ and help method

# ___dir()___
# dir method use hota hai obj k method aur attribute dekhne k liay

class MyClassDir:
    def __init__(self):
        self.name = "Muhammad Noman Aslam"
        self.age = 22

    def info(self):
        self.skill = "Python Programmer"
        return f"I am Professional {self.skill}"

obj_dir = MyClassDir()
print(dir(obj_dir), "- Before")  # yeh class k  saaray method aur attributes bataey gha
print(obj_dir.info())  # called "info" method
print(dir(obj_dir), "- After")  # yeh class k  saaray method aur attributes bataey gha

print("-----")

# ___(__dict__)___
# __dict__ use hota hai obj k attributes ko dekhne k liay
class MyClassDict:
    def __init__(self):
        self.name = "Muhammad Noman Aslam"
        self.age = 22

    def info(self):
        self.skill = "Python Programmer"
        return f"I am Professional {self.skill}"

obj_dict = MyClassDict()
print(obj_dict.__dict__, "- before")
print(obj_dict.info())  # called "info" method
print(obj_dict.__dict__, "- after")

print("-----")

# ___help()___
# help method sirif class aur instance k liay hota hai usski documentation phrne k liay

class MyClassHelp:
    def __init__(self):
        self.name = "Muhammad Noman Aslam"
        self.age = 22

    def info(self):
        self.skill = "Python Programmer"
        return f"I am Professional {self.skill}"

obj_help = MyClassDict()
help(list)  # no need to call help method
print("- class")
help(obj_help)  # no need to call help method
print("- instance")