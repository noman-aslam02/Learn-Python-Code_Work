# Format - Strings in Python

# As know we can't add string with integer like that
"""
string_value = "The person age is"
integer_value = 20
print(string_value + integer_value)  # Wrong Way
"""

# here we will use format() method to combine string with number
string_value1 = "The person age is {}"
integer_value1 = 20
print(format(string_value1.format(integer_value1)))  # return The person age is 20

#another good way to use f before ""
#yeh 'f' bhi same yehi kaam krta hai argument paas krwana
# f means formatting
integer_value2 = 24
print(f"The other person age is {integer_value2}")

# ___correct placeholders___
"""
in case aghr hum galat placholder bana kr bhet jate hai yaani agay peechay variable
to phir hum index [0] ka astamaal krte hai
#### isska use kren kaa faida yeh haai aapko yaad rehta hai k placeholder kss index may majood hai
#Example
index [0]
quantity = 3 index [0]  yeh wala data store krdegha argument may
itemno = 567 index [1]
price = 49.95 index [2]
"""
age = 99
my_name = "Muhammad Noman"
myorder = "My name is {1} and i am {0} years old"
print(myorder.format(age,my_name))
"""
(age{0},my_name{1}))  # exactly yeh tuple brackets ko dekhta hai
aghr hum issko switch krdenghay
(my_name{0},age{1}))  # return My name is 99 and i am Muhammad Noman years old
"""
print(myorder.format(my_name,age))



# another easy way to combine string with number is..... use comma","  :)
string_1 = "may ek string ho"
number_1 = 20
print(string_1, number_1)  # here we used comma(,) to combine string with number