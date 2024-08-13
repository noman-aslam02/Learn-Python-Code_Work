# Class Methods as Alternative Constructors in Python
# Class methods as alternative constructors banane ka maqsad different inputs ya logic
# se instances create karna hai


class Student:  # Student class banai hai
    def __init__(self, name, age):  # constructor method  (Primary Constructor)
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    @classmethod  # class method decorator, yeh class method hai
    def finding_age(cls, p_name, birth_year):  #
        person_age = 2024 - birth_year
        return cls(p_name, person_age)  # new instance create kiya hai class ka
# Ye cls(p_name, person_age) actually Student(p_name, person_age) ke barabar hai,
# jo __init__ method ko call karta hai

# Normal constructor se instance banaya
student1 = Student("Asad", 20)

# Alternative constructor se instance banaya
student2 = Student.finding_age("Noman", 2002)

print(student1.name, student1.age)
print(student2.name, student2.age)