# Dictionary = {"A" : ">85", "B" : ">75", "C" : ">65", "D" : ">55", "C" : "<55"}
# # key = Dictionary.keys()
# for key in Dictionary:
#     print(key, Dictionary[key])

# Dictionary = {"A" : 85, "B" : 75, "C" : 65, "D" : 55, "E" : 55}
# for key in Dictionary:
#     if Dictionary[key] > 60:
#         print(key, Dictionary[key])

Dictionary = {"E" : "<55", "B" : ">75", "A" : ">85", "C" : ">65", "D" : ">55"}
lstkey = list(Dictionary.keys())
print("Sebelum disort : ", lstkey)
lstkey.sort()
print("Sesudah disort : ",lstkey)
for key in Dictionary:
    print(key, Dictionary[key])