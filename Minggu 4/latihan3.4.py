a = int(input("Masukkan sisi 1 : "))
b = int(input("Masukkan sisi 2 : "))
c = int(input("Masukkan sisi 3 : "))

if a == b and b != c:
    print("2 sisi sama")
elif a == b and b == c:
    print ("3 sisi sama")
else :
    print("Tidak ada sama")