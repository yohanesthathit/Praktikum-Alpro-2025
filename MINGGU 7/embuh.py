# x = int(input("Masukkan bilangan : "))
# if x > 0:
#     if x % 2 == 0:
#         print("Genap")
#     else:
#         print("Ganjil")
# else:
#     print("Bilangan Negatif")


# for i in range(1, 11):
#     for j in range(1,11):
#         print(j, end=" ") #Inner
#     print(i) #Outer

# i = 1
# j = 1
# while i < 11:
#     while j < 11:
#         print(j, end=" ") #Inner
#         j += 1 #Inner
#     print(i) #Outer
#     i += 1 #Outer
#     j = 1 #Outer

# x = -1
# y = 8
# if x > 0 :
#     if y > 0:
#         print("Keduanya Positif")
# else:
#     print("Salah Satu atau Keduanya Negatif")


# for i in range(1, 99999999):
#     print(i)
#     if i == 5:
#         break

# for i in range(1, 99999999):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

x = 1
y = 1
z = 1

if x == y:
    if x == z:
        print("X Sama Dengan Y dan Z")
    else:
        print("X Sama Dengan Y")
else:
    if y == z:
        print("X Tidak Sama dengan Y dan Y Sama Dengan Z")
    else:
        print("X Tidak Sama Dengan Y dan Y Tidak sama Dengan Z")