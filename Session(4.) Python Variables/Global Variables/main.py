# Global Variables in Python

# How to create a global variable and use it inside a function
greeting = "Love"  # This is a global variable

def print_greeting():
    # Here we use the global variable inside the function
    print("Python is " + greeting)

print_greeting()
print("Python is " + greeting)  # Outside of the function

# How to create a local variable inside a function
adjective = "awesome"

def print_adjective():
    local_var = "wow"  # This is a local variable
    print("Python is " + local_var)

print_adjective()
print("Python is " + adjective)

# How to use a global variable from a function for both inside and outside of the function
def set_global_var():
    global x  # Here we declare x as a global variable
    x = "fantastic"
    print("Python is " + x)

set_global_var()
print("Python is " + x)

# How to update a global variable
material = "gold"
print("Python is " + material)  # Before update

def update_material():
    global material  # Here we modify the global variable
    material = "diamond"  # And change its value

update_material()
print("Python is " + material)  # After update
