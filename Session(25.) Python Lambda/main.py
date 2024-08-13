# Python lambda

# ___lambda___
# lamda ek keyword hai jo as a short function use kiya jata hai without defining name

# abhi yeh simple ek function hai
def my_fun(f_name, l_name):
    print(f_name, l_name)

my_fun("noman", "aslam")


# ab isska short tareeqa yeh hai k hum lambda function use kre
# setting lambda function
full_name = lambda f_naam, l_naam : f_naam + " " + l_naam
# giving argument in lambda function
print(full_name("Muhammad", "Noman"))

print("-----")

# ___hum lambda function kssi aur function may bhi use kr sakhte hai___
def add(n):  # add function k andr lambda function return ho raha hai
    return lambda x : x + n

#  yaha ab "my_lambda_func" ek lambda function bn chuka hai
my_lambda_func = add(15)  # yeh "def func" ka argument store krta hai taa ka add kiya jaa sakhe
my_second_lambda = add(19)  # hum multiple times lambda return kr sakhte hai
print(my_lambda_func(12))  # calling lambda function
print(my_second_lambda(15))  # calling lambda function

print("-----")

# ___sorted() and filter() function___

# hum sorted() funtion use kr rahe hai
# without lambda function

# creating list
num_list = [10, 2, 5, 7, 9, 7, 4]
def chk_even(n):
    return n % 2 == 0
# issko list format may convert krna zahroori hai wrna yeh "filter object" k form may aeygha
filter_list = filter(chk_even, num_list)
print(list(filter_list), "<-----filter()")

# ab hum lambda ka use karenghay
# creating list
num_list = [10, 2, 5, 7, 9, 7, 4]
filter_list1 = list(filter(lambda x: x % 2 == 0, num_list))
print(filter_list1, "as you can see both are same ways and we got same result<-----filter()")

# here we used sorted function
# simple example
student = [('Ibrahim', 19), ('Aliza', 16), ('Farhan', 22)]
# yeh sort kr raha hai " student 'list of tuple' " ko unn k age k according
sorted_students = sorted(student, key= lambda x: x[1])
print(sorted_students, "<-----sorted()")

# ab hum sorted() function apnay filter list pr bhi aplly karenghay
sorted_filter_list = sorted(filter_list1, reverse=False)  # hum nay list reverse nahi kiya
print(sorted_filter_list, "<-----sorted()")

print("-----")

# ___map()___
# iss map() function ka use kr k ek iterable object k hr elements pr function apply kr sakhte hai
# yeh ek best tareeqa ho sakhta hai aghr hamay hr elements pr function use krna hai
num_list = [10, 2, 5, 7, 9, 7, 4]
me_lambda = lambda x: x * 2

map_lambda = list(map(me_lambda, num_list))
print(map_lambda)

print("we can do same thing in list comprehension but map() function is more useful")

# hum kuch iss tareeqay say bhi hr element pr operation kr sakhte hai
# but
# map() function zada useful hai
num_list = [10, 2, 5, 7, 9, 7, '4']  # creating list
# yeh hr element pr *2 operation kr k new "i" list may daaly gha likn sirif ussko jo integer honghay
mul_list = [i*2 for i in num_list if i == int(i)]
print(mul_list)  # yaha hum nay new list print krdi

print("-----")

# ___reduce()___
# Python mein `reduce` function ek sequence ke elements ko ek initial value ke sath
# iteratively combine karke ek single value mein reduce karta hai

# Code ko dekh kr samjhne ki koshish krte hai

# first we to import reduce function from functools module without this we can't use reduce function

from functools import reduce
num_list_1 = [10, 3, 5, 7, 9, 7, 4]  # creating list
comb_lambda = lambda x, y: x + y
new_red_list = reduce(comb_lambda, num_list_1, 20)
print(new_red_list)

print("-----")

print("some code's practice and it will help you to understand")
# yeh tareeqa kaafi mushkil hai
my_lambda = lambda x: x % 2 == 0
new_list = []
num_list = [10, 2, 5, 7, 9, 7, 4]  # creating list
for i in num_list:
    if my_lambda(i):
        new_list.append(i)
print(new_list, "7 lines code, yaha hum nay kaafi time spend kiya")

# yeh short tareeqa hai
my_lambda1 = lambda x: x % 2 == 0
num_list_1 = [10, 2, 5, 7, 9, 7, 4]  # creating list
new_list_1 = list(filter(my_lambda, num_list_1))
print(new_list_1, "4 lines code, yaha hum nay kmm time may task complete krliya")

print("-----")

# here we did function inside function for better understanding
def cube_and_add(a):
    return lambda c : c*c*c + a

lambda_c_a = cube_and_add(11)
print(lambda_c_a(3))

# aghr hamay list k hr element pr cube astmaal krna hai aur add bhi krna hai to kuch aysay hogha
def cube_and_add(a):
    return lambda c : c*c*c + a

lambda_c_a = cube_and_add(11)

num_list_1 = [10, 3, 5, 7, 9, 7, 4]  # creating list
new_c_a_list = list(map(lambda_c_a, num_list_1))
print(new_c_a_list)