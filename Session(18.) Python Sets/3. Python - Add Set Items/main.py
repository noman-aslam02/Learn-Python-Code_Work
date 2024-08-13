# Python - Add Set Items

# ___Add Items___
# set may items add krne k liay add() method ka use kare
numbers = {2212,112, 33, 11, 3}
numbers.add("hello")
print(numbers)

print("-----")

# ___Add Sets___
# we can add items from another set to current set using update() method
employees = {"noman", "asad", "junaid"}
new_employee = {"ahsan"}
employees.update(new_employee)
print(employees)

print("-----")

# ___Add Any Iterable___
# set may hum kssi bhi types k iterable ko add kr sakhte hai
employees = {"noman", "asad", "junaid"}
new_employee = ["abdul", "ubaid"]
employees.update(new_employee)
print(employees)