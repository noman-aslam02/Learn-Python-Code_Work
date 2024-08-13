# # Python Arrays
#
# # ___Arrays___
# # Arrays ek list ki thara hoti hain jismein ek hi type ka data maujood hota hai
#
# # String type array
# array_string_list = ["noman", "asad", "ahsan", "junaid"]  # sabhi values same type ki hain
# print(array_string_list)
# # Integer type array
# array_integer_list = [22, 20, 18, 24]  # sabhi values same type ki hain
# print(array_integer_list)
#
# print("-----")
#
# # ___Accessing value of array list___
# print("<<Accessing string value>>")
# print(array_string_list[0])
# print(array_string_list[1])
# print(array_string_list[2])
# print(array_string_list[3])
# print("<<Accessing integer value>>")
# print(array_integer_list[0])
# print(array_integer_list[1])
# print(array_integer_list[2])
# print(array_integer_list[3])
#
# print("-----")
#
# # ___Updating value of array list___
# array_string_list[3] = "Ubaid"  # updating value of array string list
# array_integer_list[3] = 25  # updating value of array integer list
# print(array_string_list)
# print(array_integer_list)
#
# print("-----")
#
# # ___Itertating over array list___
# # String Array List
# print("Iterating over string array")
# for string in array_string_list:
#     print(string)
#
# # Integer Array List
# print("Iterating over integer array")
# for integer in array_integer_list:
#     print(integer)
#
# print("-----")
#
# # ___Fixed Sized Array List___
# # Fixed Sized Array List aik aisi list hoti hai jismein elements ki total quantity pehle
# # se hi tay hoti hai aur badli nahi ja sakti
# # hamay bs yeh Fixed Sized Array List bana nay k liay module import krna zahroori hota hai
# # q k python may built in array nahi hotay to hum "numpy" ya "array" module ka astamaal karenghay
#
# # import module "numpy"
# import numpy as np
#
# # Integer type array using numpy
#
# # create numpy array list
# NEW_ARRAY_LIST = np.array([1, 2, 3, 4, 5])
# print(NEW_ARRAY_LIST)
#
# array_integer_list = np.zeros(5, dtype=int, order="C")
# array_integer_list[0] = 19
# array_integer_list[1] = 20
# array_integer_list[2] = 21
# array_integer_list[3] = 22
# array_integer_list[4] = 23
#
# print("Integer array:", array_integer_list)

class MagicClass:
    name = "Noman"

    def __len__(self):
        i = 0
        for a in self.name:
            i += 1
        return i

obj_magic = MagicClass()
print(len(obj_magic))