a = input("Masukkan sisi 1 : ")
b = input("Masukkan sisi 2 : ")
c = input("Masukkan sisi 3 : ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a!=b and b!=c and a!=c:
        print("Tidak ada yang sama")
    elif a == b and a == c and c==b:
        print("3 sisi sama")
    else:
        print("2 sisi sama")
except:
      print("INPUT HARUS BERUPA INTEGER NDESS!!")