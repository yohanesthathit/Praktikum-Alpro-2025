# word = 'harimurti'
# Dictionary = dict()
# for huruf in word:
#     if huruf not in Dictionary:
#         Dictionary[huruf] = 1
#     else:
#         Dictionary[huruf] += 1

# print(Dictionary)

word = 'mamipokopants'
Dictionary = dict()
for huruf in word:
    Dictionary[huruf] = Dictionary.get(huruf,0) + 1

print(Dictionary)