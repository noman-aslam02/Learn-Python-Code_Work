# Python - Loop Tuples

# ___Loop Through a Tuple___

# tuple k hr elements kr ghuzarne k liay "for" loop ka astamaal kare
this_tuple = ("apple", "banana", "cherry")
for i in this_tuple:
    print(i)  # yeh for loop hr ek items ko ek ek kr k print kr de ghi

print("-----")

# ___Loop Through the Index Numbers___
# hum index ka bhi use kr sakhte hai loop may tuple items ko print krne k liay
# yaha hamay range() method and length() method ki zahroorat pade ghi
this_tuple = ("apple", "banana", "cherry")
for i in range(len(this_tuple)):
    print(this_tuple[i])

print("-----")

# ___Using a While Loop___
# hum "while" loop ka bhi astamaal kr k tuple k hr items pr iterate kr sakhte hai
this_tuple = ("apple", "banana", "cherry")
i = 0  # where to start
while i in range(len(this_tuple)):
    print(this_tuple[i])
    i += 1  # Remember to increase the index by 1 after each iteration
    # Aghr hum increase nhi krte index ko to yeh infinite loop may chala jaeygha