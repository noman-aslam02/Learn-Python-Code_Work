# Python - Unpack Tuples

# ___Unpacking a Tuple___
# unpacking a tuple means hum python may tuple ko ek ek kr unpack kr sakhte hai through variables

# here is simple looks of tuple items
tuple_items = ("apple", "banana", "cherry")
print(tuple_items)

# ab hum iss tuple ko unpack karenghay
tuple_items = ("apple", "banana", "cherry")
(red, yellow, green ) = tuple_items
print(red)
print(yellow)
print(green)
# yaa iss tareeqay say print krdo mrzi hai but yeh ek line may print krdegha
print(red, yellow, green)

print("-----")

# ___Using Asterisk*___
"""
asterisk ka astamaal tab use hota hai jab hamaray paas number of variables say zada number
of values zada use ho to hum asterisk "*" ka use krte hai aur yeh as a list bn jati hai
"""
tuple_items = ("apple", "banana", "cucumber", "avocado")
(red, yellow, *green) = tuple_items
print(red)
print(yellow)
print(green)
# or like this way
print(red, yellow, green)

"""
aghr hum asterisk "*" last variable k bajey kssi aur varaible ko de dete hai to yeh numbers of
values apnay andr hold krleta hai aur at least one value uss variable k liay chor deta hai
<<<see example for better understanding>>>
"""
tuple_items = ("apple", "banana", "lemon", "avocado")
(red, *yellow, green) = tuple_items
print(red)
print(yellow)
print(green)