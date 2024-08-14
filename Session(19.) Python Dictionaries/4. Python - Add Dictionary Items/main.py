# Python - Add Dictionary Items

# ___Adding Items___
# hum dict may new item add kr sakhte hai ek new index key aur usski value assign kr k
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print("-----")


# ___Update Dictionary___
# hum update() method ka use kr k ek new item bhi add kr sakhte hai
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"model": "abc"})
print(thisdict)