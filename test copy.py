import json


# with open('word_3.json', 'w') as file:
#     json.dump(gl, file, ensure_ascii=False, indent=4)

a = []
b = []

with open('word_3.json') as file:
    tr3 =json.load(file)
print(len(tr3))
# print(tr)
with open('word_4.json') as file:
    tr4 =json.load(file)
print(len(tr4))
# for key3 in tr3.keys():
#     for key4 in tr4.keys():
#         if key3 == key4:
#             a.append(key3)

print('_______________________-')

for key in tr3.keys():
    if key in tr4.keys():
        a.append(key)
    if key not in tr4.keys():
        b.append(key)
        print(key, tr3[key])



print(len(a))
print(len(b))