# Python - Slicing Strings

# ___Slice___
# As we know we can select normally one character from data type sequences
#Example
x = "Hello World!"
print(x[1])  # it will print e because e is index[1]
# remember index starts from [0]

# ___Range of Slice___
x1 = "Hello World!"
print(x1[0:3])  # starts from H[0] and end with l[2]
# yaha [3] 'l' ignore kiya q k python may yeh slicing ka basic behaviour hai last index ko ignore krna

# ___Slice From the Start___
x2 = "Hello World!"
print(x2[:4])  # yaha starting index say print krne k liay index leave kiya jaa sakhta hai

# ___Slice To the End___
x3 = "Hello World!"
print(x3[2:])  # yaha ending takh index ko print k liay index leave kiya jaa sakhta hai

# ___Negative Indexing___
# end index say start krne k liay negative number index ka astamaal kre
x4 = "Hello World!"
print(x4[-3:-1])
# its starting from d[-2] and end with l[-3], ![-1] index will ignore here
"""
notice: last index hamesha ignore kiya gha aghr hum ek index k saath dusra de rahe hai yaani
2nd index jo colon":" k baad diya jata hai
"""