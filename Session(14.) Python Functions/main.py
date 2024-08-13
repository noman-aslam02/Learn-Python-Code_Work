# Python Functions

# User defined funtions rule
"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

# ___how to create function and call function to get result___
# create function
def sum(a, b):  # parenthesis k andr variable paas kiya huwa hai
    # 'def' keyword bata raha hai k hum function bana rahe hai
    print(f"Sum of {a} and {b} is: ", a + b)  # yaha hum apna code modify kr sakhte hai
# call function
sum(4,4)  # call function to get result
# '4,4' yahan ek argument hai

# yeh kuch aur simple example
# create function
def mul_num(x, y,z):
    return x * y + z + x
# call function inside print() function
print(mul_num(4,4, 1))  # numbers of values required as per we write in function parenthesis
# hum jitna chaa hay arguments paas kr sakhte hai

"""
aghr hum nay function may 2 values di aur neechay function call kr k sirif 1 yaa 2 say zada
arguments paas kri to yeh error throw karegha
"""
# def full_name(fisrt_name, last_name):
#     return fisrt_name + last_name
#
# print(full_name("Noman"))  # error throw karegha q k sirif ek hi argument paas huwa hai

# ___Arbitrary Arguments, *args___
"""
If you do not know how many arguments that will be passed into your function, add a '*' 
before the parameter name in the function definition.

Remember yeh tuple k format may receive krta hai jab hum arguments paas krte hai function may 
"""
def employees(*names):
    print("Best employer of the year: " + (names[3]))

employees("Noman", "Asad", "Ahsan", "Junaid", "Ubaid")

# hum numbers ki bhi masaal le sakhte hai
# yaha hum may loop ka astamaal kiya hai for sum
def sum_numbers(*num):
    sum_num = 0  # aghr 1 say start karoghay to yeh 1 say add krna start karegha
    for x in num:
        sum_num += x  # yaha yeh hr iteration pr ek k baad ek value ko add krta hai
        # print(sum_num)
    print("The sum of all numbers: " + str(sum_num))

sum_numbers(1, 4, 7, 10)

# ___Keyword Arguments___
# Keyword Arguments ka matlab hai ke hum function ko arguments key=value syntax ke zariye send kar sakte hain
def info(child_1, child_2, child_3):
    print("The youngest child is: ", child_3)

info(child_1 = "Noman", child_2 = "Asad", child_3 = "Ahsan")


# ___Arbitrary Keyword Arguments, **kwargs___
# **kwargs ka istemal tab hota hai jab humein function ko variable number of keyword arguments pass karne hote hain
# ** ka use hota hai dictionary ko unpack krna
# yeh best tareeeqa hai loop ka use kr k sabka result ek saath nikal sakte hai
def fun_student(**para_students):
    for name, marks in para_students.items():
        print(f"Congrats! {name}, You got {marks} marks")
fun_student(Noman = 85, Asad = 85, Ahsan = 80, Mustafa = 80)

# if we want to get one student result use this method
def fun_student1(**para_students11):
    name1 = "Noman"
    marks1 = para_students11[name1]  # yaha pr '**' use issliay nhi kiya q k yeh unpack nhi kr raha seedha ek key and value utha raha hai
    print(f"Shabash {name1}, aap nay {marks1} marks haasil kare")
fun_student1(Noman = 85, Asad = 85, Ahsan = 80, Mustafa = 80)

# another example
def employees(**names):
    print("Names of the students: " + names["names"] , names["names1"], names["names3"])

employees(names= "Noman", names1= "Asad", names3= "Ahsan")

# another best example of it
def employees(**names):
    for name, actual_name in names.items():
        print("name of the students: ", actual_name)
employees(names= "Noman", names1= "Asad", names3= "Ahsan")

# ___Default Parameter Value___
def welcome_(name="World"):
    # print("Hello", name)
    print(f"Hello {name}")  # both way is right

welcome_("Noman")
welcome_()
welcome_("Nusrat")

# let make it complex little bit
# likn yeh exactly default value k thara kaam krta hai, its not default parameter value
def res_stud(**prep_student):
    for students, grade in  prep_student.items():
        if grade == "A" or grade == "B":
            result = "Pass"
        elif grade == " " or grade == "":
            result = "Pending"
        else:
            result = "Fail"
        print(f" {students}, result is {result}")

res_stud(Noman = "A", Asad = "B", Ahsan = "C", Junaid = "", Ubaid = " ")

# ___Passing a list as an Argument___
def my_cart(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
vegetables = ["Bhindi", "Kheera", "Payaas"]
my_cart(fruits)
my_cart(vegetables)

# ___Return Values___
# aghr humay koi value return krni hai to hum return value ka astamaal karenghay
def number_101(x,y):
    return x / y

print(number_101(24,8))  # output  3.0

# ___The pass Statement___
def my_ran():
    pass  # the 'pass' keyword avoid getting error, if we don't have content to write


# ___Positional-Only and Keyword-Only Arguments___
# Positional-Only Arguments (, /)
# yeh sirif position k base pr hi arguments paas honghay
def my_pos(x, y, z, /):
    print(x, y, z)
my_pos(2, 5, 7)

# without ", /" this, we are allowed to use keyword-only arguments
def my_pos(x, y, z):
    print(x, y, z)
my_pos(x = 44, y = 50, z = 11)

# Keyword-Only Arguments (*,)
# Yeh sirf `key=value` ke base par kaam karte hain
def my_key(*, x, y, z):
    print(x, y, z)
my_key(x = 1.0, y = 0.3, z = 30)

# without "*," this, we are allowed to use positional-only arguments
def my_key(x, y, z):
    print(x, y, z)
my_key(1.0,0.3,30)

# Combine Positional-Only and Keyword-Only
# Any argument before the "/ ," are positional-only, and any argument after the "*,"s are keyword-only
def pos_key(a, b, /, *, c, d):
  print(a + b + c + d)
  print(a, b, c, d)
pos_key(5, 6, c = 7, d = 8)

# ___Recursion___
def tri_recursion(k):
  if(k > 3):
    result = k + tri_recursion(k - 1)  # function recall kr raha hai apnay aap ko
    # print(result)  # uncomment this to see the full result
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)
# Answer
print("Final Answer is:", tri_recursion(6))

# Explanation
"""
Pehle, function check karega ke kya 6 > 3 hai? Jee haan, to function 6 + tri_recursion(5) return karega.
Ab function tri_recursion(5) ko call karega. Yahan pe function check karega ke kya 5 > 3 hai? Jee haan, to function 5 + tri_recursion(4) return karega.
Ab function tri_recursion(4) ko call karega. Yahan pe function check karega ke kya 4 > 3 hai? Jee haan, to function 4 + tri_recursion(3) return karega.
Ab function tri_recursion(3) ko call karega. Yahan pe function check karega ke kya 3 > 3 hai? Nahi, to function 0 return karega.
Ab function wapis point 4 pe jayega, jahan se usne tri_recursion(3) ko call kiya tha. Yahan pe function 4 + 0 calculate karega, jo ke 4 hota hai.
Ab function wapis point 3 pe jayega, jahan se usne tri_recursion(4) ko call kiya tha. Yahan pe function 5 + 4 calculate karega, jo ke 9 hota hai.
Ab function wapis point 2 pe jayega, jahan se usne tri_recursion(5) ko call kiya tha. Yahan pe function 6 + 9 calculate karega, jo ke 15 hota hai.
Yeh 15 value function return kar dega.
"""