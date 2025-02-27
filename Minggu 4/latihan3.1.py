a = input("Masukkan bilangan pertama :")
b = input("Masukkan bilangan kedua : ")
c = input("Masukkan bilangan ketiga : ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a > c:
        print("Terbesar : ", a)
    elif b > a and b > c:
        print("Terbesar : ", b)
    else:
        print("Terbesar : ", c)
except:
    print("Input tidak valid! Harus berupa INTERGER!")