bulan = input("Masukkan bulan : ")

try:
    bulan = int(bulan)
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("Jumlah hari : 31")
    elif bulan == 2:
        print("Jumlah hari : 29")
    else:
        print("Jumlah hari : 30")
except:
    print("bulan yang diinputkan tidak valid!")