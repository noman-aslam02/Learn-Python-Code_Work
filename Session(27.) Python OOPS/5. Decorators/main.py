# Decorators

# Decorators, Python mein higher order functions hain jo doosre functions ya code ko wrap
# karke unhe modify ya extend karte hain, aur phir modified ya extended version ko return
# karte hain

# 'welcome_p' ek decorator function hai jo kisi aur function 'u' ko wrap kar raha hai.
def welcome_p(u):
    # 'wrapper' ek inner function hai jo pehle welcome message print karta hai, phir function 'u' ko call karta hai, aur akhir mein enjoy message print karta hai.
    def wrapper():
        print("....Welcome to our Hell Gamers Server....")  # Welcome message
        u()  # Function 'u' ko call kar raha hai
        print("Enjoy Dude! :)")  # Enjoy message
    return wrapper  # 'wrapper' function ka reference return kar raha hai

# 'user_name_p' function ko 'welcome_p' decorator ke saath define kar raha hai. Is se 'user_name_p' function 'wrapper' function ban jata hai
# q k hum nay "user_name_p" ko wrapper function may daal diya hai na issliay
# 'decorator' ka use aur 'wrapper function' k andr daalne k baad hi "user_name_p" wrapper
# function bn jata hai
@welcome_p
def user_name_p():
    print("Muhammad Noman Aslam")  # User ka naam print kar raha hai
# Yahan pe 'user_name_p' function call ho raha hai, jo ab 'wrapper' function hai.
user_name_p()

print("-----")

def welcome(u):
    print("....Welcome to our Hell Gamers Server....")
    u()
    print("Enjoy Dude! :)")

@welcome
def user_name():  # it will automatically call function when defining decorator with function
    print("Muhammad Noman Aslam")


print("\n--Or this way--  ( ...Both Are Same...)\n")

def welcome1(u):
    print("....Welcome to our Hell Gamers Server....")
    u()
    print("Enjoy Dude! :)")
def user_name1():
    print("Muhammad Noman Aslam")

welcome1(user_name1)

print("\nSome more practices for better understanding\n")

def greet(u):
    def wrapper(*args, **kwargs):  # waysay **kwargs required nahi tha calculation k liay
        print("....Welcome to our Hell Gamers Server....")
        u(*args, **kwargs)  # aur yaha bhi nahi thi zahroorat "**kwargs" ki
        print("Enjoy Dude! :)")
    return wrapper

@greet
def sum(a, b):
    print(a + b)

sum(5, 3)  # Yeh 8 print karega

print("-----")

# ab ek keyword argument dete hai

def greeting(i):
    def wrapper(*args, **kwargs):  # yaha hum nay wrapper ko argument paas kiye
        print("Assalam Alikum")
        i(*args, **kwargs)  # aur yaha bhi intro() function ko arugment pass kiye same
        print("Allah Hafiz")
    return wrapper
@greeting
def intro(name, age):
    print(f"The name of person is {name} and his age {age}")
    if age >= 18:
        print("You can work with us")
intro("Muhammad Noman Aslam", 21)
