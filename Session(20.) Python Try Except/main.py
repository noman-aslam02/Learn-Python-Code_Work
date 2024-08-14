# Python Try Except

# ___Exception Handling___
# Exception Handling matlab error handle krna, "try" statement ka use kr k error handle kr sakhte hai
x = 11
try:
    print(x1)
except:
    print("exception error aya hai")

print("-----")

# Exception as e
# Exception almost all types ki errors ko handle karta hai
# "e" ek variable hai jss may error ki details jama hoti hai
x = 2
y = "hello"
try:
    print(x + y)
except Exception as e:
    print(e)



# ___Many Exceptions___
# hum bohut saray exception bana sakhte hai error ko handle krne k liay
# but hamay yaha pr ek special error bana rahe hai jo bata ta hai k varaible define hai ya nhi
try:
    print(xx)
except NameError:
     print(f"varaibel 'xx' is not defined")
except:
    print("something else went wrong")

print("-----")

# ___Else___
# else keyword ek block of code ko execute krta hai aghr koi bhi errors na aey
x = 2
y = "hello"
try:
    print(x , y)
except Exception as e:
    print(e)
else:
    print("koi bhi error nahi aya hai :)")

print("-----")

# ___Finally___
# Finally apna block of code kssi bhi situation may execute krti hai, chahay code may error ho ya nahi
try:
    print(x1)
except:
    print("exception error aya hai")
finally:
    print("try-except complete ho gaya")

# Yeh cheezain band karne aur resources ko saaf karne ke liye mufeed ho sakti hai
try:
    f = open("demofile.txt")
    try:
        f.write("Python is the best")
    except:
        print("kuch to galat hai text lines nahi likha raha .txt file may")
    finally:
        f.close()
except:
    print(".txt file open nahi ho rahi kuch masla aa raha hai")

# another example of finally keyword
def func1():
    try:
        num_list = [1, 3, 5, 50]
        user_inp = int(input("enter the index to print element: "))
        return num_list[user_inp]
    except ValueError:
        print("string value is not allowed")
    except:
        print("the index is not in the list")
        return 0

print(func1())

print("-----")

# ___Raise an exception___
# yeh "raise" program ko stop kr k error throw kreghi
"""
x = -1
if x < 0:  # to yeh true q k -1 less than 0 hai
  raise Exception("Sorry, no numbers below zero")
"""
# issko avoid krne k liay yeh "try-except" ka tareeqa apnaey
x1 = 1
try:
    if not x1 < 0:  # to yeh False hai q k 1 less than 0 k nahi hai
        raise Exception(f"Sorry, {x1} is not below zero")
except Exception as e:
    print(e)

print("-----")

# ___TypeError___
# Yeh tab raise hota hai jab aap kisi object ko uske unsupported operation ke liye use
# karne ki koshish karte hai
try:
    result = "age" + 21
except TypeError:
    print("string value concat nahi ho sakhta integer value k saath")

print("-----")

# ___ValueError___
# jab operation ya function ki expectation ke mutabiq argument ki value galat ho,
# tab ValueError raise hota hai.
# type match hona zahroori hai
try:
    user_input = int(input("enter your age: "))
    print(user_input)
except ValueError:
    print("string value allow nahi hai, age as a integer value daleghi")
