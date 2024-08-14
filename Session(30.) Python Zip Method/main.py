# Python Zip Method

# ___zip()___
# zip() har iterable se elements ko utha ke unko tuples mein jodta hai
fruit_name = ["apple", "avocado", "Strawberry"]
fruit_price = [150, 300, 250]
# to abhi yeh object return karegha
result = zip(fruit_name, fruit_price)
print(result)

print("--------------------------------")

# issko as a list ya tuple use karna padegha taa k yeh readable format may data show ho
result1_list = list(zip(fruit_name, fruit_price))
result1_tuple = tuple(zip(fruit_name, fruit_price))
print(result1_list)
print(result1_tuple)
