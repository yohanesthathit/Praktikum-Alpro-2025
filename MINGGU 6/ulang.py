nama = "thathit"
# for i in range (round(len(nama)/2)):
#     if i == 0:
#         print (f"   {nama[round(len(nama)/2)]}")
#     elif i == 1 :
#         print (f"  {nama[2:5]}")
#     elif i == 2 :
#         print (f" {nama[1:6]}")
#     else:
#         print (nama)

for i in range (round(len(nama)/2)):
    for j in range (len(nama) + 1):
        if j < len(nama):
            print (nama[j], end=" ")
        else:
            print ("\n")