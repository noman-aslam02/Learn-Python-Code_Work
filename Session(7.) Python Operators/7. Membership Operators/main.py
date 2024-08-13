# Membership Operators in Python

# ___in Membership Operators___
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
# another way
if "banana" in x:
    print("Yes, Banana exist kr raha hai")
else:
    print("NO, Banana majood nhi hai")

# ___not in Membership Operators___
# yeh kaam ulta karay gha
x1 = ["apple", "banana"]
print("banana" not in x1)
# returns True because a sequence with the value "banana" is in the list
# another way
if "banana" not in x1:
    print("Yes, Banana exist kr raha hai(liar)")
else:
    print("NO, Banana majood nhi hai(Liar)")