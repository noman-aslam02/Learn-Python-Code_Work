# Python Match Case Statement

# ___Match Case Statement___

# yeh ek new statement hai python 3.10 may, isska use multiple conditions ko handle karne ke liye
# yeh kaafi similar hai (if ... else) say
# here we did simple code to understand how 'match case statement' works

a = "Python"
match a:
    case "C#":
        print("C# is good langauge")
    case "JS":
        print("JS is good langauge")
    case "Python":
        print("Python is good langauge")
    case "React":
        print("React is good langauge")
    case _:
        print("Language shaat hai ustaad")

# lets make it complex
import datetime  # Python built-in module
# 'date' is class of module 'datetime' jo date related operations provide karta hai
# 'today()' ---> 'date' class ka method hai jo cuurent date ko return krta hai
today = datetime.date.today()
day = today.strftime("%A")  # strftime is  function to return date and time
match day:
    case "Monday":
        print("Today is Monday")
    case "Tuesday":
        print("Today is Tuesday")
    case "Wednesday":
        print("Today is Wednesday")
    case "Thursday":
        print("Today is Thursday")
    case "Friday":
        print("Today is Friday")
    case _:
        print("Day not found")
"""
Some Explanation
explain what is "_" underscore
"_" yeh underscore ek default case hai match case statement may
how it works
yeh tabhi execute krta hai aghr koi bhi case match na ho rahe ho

What is 'match' keyword
'match' keyword: Yeh keyword match case statement ki shuruaat karta hai.

What is 'case' keyword
'case' keyword: Yeh keyword har case ko define karta hai.
"""

# hum if statement ka bhi astamaal kr sakhte hai
age = 61
match age:
        case 0:
            print("Bhai paida to hoja sahi say")
        case age if age < 18:
            print("No, You are too young, turn to 18 plus")
        case age if age >= 18 and age <= 60:
            print("Yes, You are a teenager, you can work with us")
        case _:  # Default case hai, aghr 60 say greater age huwi to default case match ho jaeygha
            print("You are too old, rest nigga")