# Python - Sort Lists

# ___Sort List Ascending Order___
# sort() method list ko alphanumerically order may krti hai by default:

# Sorting the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sorting the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sorting the list alphanumerically
# but remember, the integer and string objects can't sort together in the same list
# to phir hum str() ka method ya string "" laga sakhte hai taa k sort ho sakhe list
thislist = ["orange", str(110), "kiwi", "pineapple", str(21)]
thislist.sort()
print(thislist)

print("-----")

# ___ Sort List Descending Order___
# aghr descending order may list chaeye to reverse= True keyword ka astamaal kare
# yeh argument paas krti hai list k hr elements ko sort(descending) kr k liay
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse= True)
print(thislist)

print("-----")

# ___Customize Sort Function___
# hum apni mrzi ka function bana sakhte hai aur phir uss list ko sort krwa sakhte hai
# aur yeh kaam key = function ka use kr k argument paas kr sakhte hai
def my_func(n):
    return abs(n - 50)  # abs() method kssi bhi negative ya positive number ko positive way may display krti hai
num_list = [100, 23, 80, 40, 10]
num_list.sort(key= my_func)  # yeh ek ek kr k hr elements ko ghuzar raha hai my_func pr iss k baad sort ho jaeygha list
print(num_list)

print("-----")

# ___Case Insensitive Sort___
# by default sort() method may capital letters wale phele sort ho jate hai phir lower case wale atay hai
thislist = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thislist.sort()
print(thislist)

# if we want to sort lower case letter first, then use str.lower key function
# notes, yeh alphabetically hi order may karegha, yaani kuch uppercase letter word phele bhi aa sakhte hai
thislist = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thislist.sort(key= str.lower)
print(thislist)

print("-----")

# ___Reverse Order___
# reverse() method list ko ultra krti hai
thislist = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thislist.reverse()
print(thislist)

print("-----")

# ___Order the Dictionary list___
# yeh ek best tareeqa hai dictionary ko sort krne ka
dict_list = {"UserName": "noman.abc112", "Age": 21, "Gender": "Male", "Email": "abc@gmail.com"}
sorted_list = dict(sorted(dict_list.items()))  # dict ka use kr list say wapsi dict type pr convert kiya hai
print(sorted_list)

# hum kudh say bhi order bana sakhte customize kr k without using sort() method
dict_list = {"UserName": "noman.abc112", "Age": 21, "Gender": "Male", "Email": "abc@gmail.com"}
# yeh order bata rahe hai k list kss order may ho
order_list = ["UserName", "Email", "Age", "Gender"]
# yaha hum nay key value ki pairs banaey hai loop may
order_dict_list = {x: dict_list[x] for x in order_list}
print(order_dict_list)

print("-----")

# yeh hum students ko sort kr rahe hai hr students k age k hisab say
student = [{"Name": "Noman", "Age": 21},
           {"Name": "Asad", "Age": 19},
           {"Name": "Aarib", "Age": 20},
           {"Name": "Ubaid", "Age": 26},
           {"Name": "Bablu", "Age": 16}]
sort_list = student.sort(key = lambda student: student["Age"])
print(student)