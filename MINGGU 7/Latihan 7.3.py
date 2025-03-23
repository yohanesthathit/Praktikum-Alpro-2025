def deret_biasa(tinggi, lebar):
    x = 0
    for i in range(1, tinggi+1):
        for j in range(1, lebar+1):
            x += 1
            if j < lebar:
                print(x, end=" ")
            else:
                print(x)
            
tinggi = int(input("Masukkan Tinggi : "))
lebar = int(input("Masukkan Lebar : "))
deret_biasa(tinggi,lebar)