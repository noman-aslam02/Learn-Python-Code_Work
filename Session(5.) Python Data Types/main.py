#Data Types in Python

#___Text Type___
str_type = "My name is Muhammad Noman Aslam"
print(str_type)
print(type(str_type)) #issay hum "str"(string) type kehte hai

#___Numeric Types___
int_type = 50
print(int_type)
print(type(int_type)) #issay hum int(integer) type kehte hai

float_type = float(12.05)
print(float_type)
print(type(float_type)) #issay hum (float) type kehte hai

complex_type = 1j
print(complex_type)
print(type(complex_type)) #issay hum (complex) type kehte hai

#___Sequence Types___
list_type = ["apple", "banana", "cherry"]
print(list_type)
print(type(list_type)) #issay hum (list) type kehte hai

tuple_type = ("apple", "banana", "cherry")
print(tuple_type)
print(type(tuple_type)) #issay hum (tuple) type kehte hai

range_type = range(6)
print(range_type)
print(type(range_type)) #issay hum (range) type kehte hai

#___Mapping Type___
dict_type = {"name": "John", "age": 36}
print(dict_type)
print(type(dict_type)) #issay hum dic(dictionary) type kehte hai
#another example
dict_type1 = {"Alice":{"age":21,"Skin":"Fair"}}
print(dict_type1)
print(type(dict_type1)) #issay hum dic(dictionary) type kehte hai

#___Set Types___
set_type = {"apple", "banana", "cherry"}
print(set_type)
print(type(set_type)) #issay (set) type kehte hai

frozen_set = frozenset({"apple", "banana", "cherry"})
print(frozen_set)
print(type(frozen_set)) #issay (frozen set) type kehte hai

#___Boolean Type___
bool_type = (10 > 2)
print(bool_type)
print(type(bool_type)) #issay (bool) type kehte hai

#___Binary Types___
bytes_type = b"Hello"
print(bytes_type)
print(type(bytes_type)) #issay b,bytes(bytes) type kehte hai
#or
bytes_type1 = bytes(5)
print(bytes_type1)
print(type(bytes_type1))

bytearray_type = bytearray(5)
print(bytearray_type)
print(type(bytearray_type))

memoryview_type = memoryview(bytes(5))
print(memoryview_type)
print(type(memoryview_type))

#__None Type__
none_type = None
print(none_type)
print(type(none_type))

