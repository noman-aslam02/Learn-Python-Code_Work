# Booleans in Python

# ___Boolean on Expression___
# yaani hum check kr sakhte hai k expressions true hai yaa nhi values pr
# Example
print(2 == 4)  # return false because 2 is not equals to 4
print(4 > 11)
print(5 != 4)
# we can also use if statement to check the condtion is 'True' or 'False'
# it will execute code!!! not True and False
a = 22
b = 10
if a > b:
    print("Yes, a is greater than b")
else:
    print("No, a is not greater than b")


# remember in Python 0 are false and 1 is true
print(bool(0))
print(bool(1))

# ___Evaluate Values and Variables___
x = 20
y = "Noman"
print(bool(x))
print(bool(y))


# ___Some Values are False___
# Example
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# ___Bool in Functions___

"""
yaad rakhe "obj" python may hamesha true hota hai, aghr hum __len__ ya __bool__ ya kuch bhi ka use
karenghay to yeh false return karegha '0' pr.
"""
class myclass():
  def __len__(self):  # its checking length of number
    return 0
  def myfun(self):
    return 0

myobj = myclass()
print(bool(myobj.__len__()))  # return false
print(bool(myobj.myfun()))  # return false
print(bool(myobj.__len__))  # return true
print(bool(myobj.myfun))  # return true


# ___Functions can Return a Boolean___
# hum sirif functions create kr sakhte hai boolean return krne k liay
def myFunction() :
  return True

print(myFunction())
# yeh kuch if and else statement pr bhi hai
def myFunction1() :
  return True
if myFunction1() == False:
    print("Function False return kr raha hai")
else:
    print("Function True return kr raha hai")

# ab hum built functions ki masaal le lete hai k built in functions pr kaysay kaam krta hai boolean
#Example
x11 = "may ek string ho"
y11 = 141
z11 = 34.0
print(isinstance(x11, str))
print(isinstance(y11, float))  # return False q k yeh 'float' nhi hai, yeh 'int' hai
print(isinstance(z11, float))