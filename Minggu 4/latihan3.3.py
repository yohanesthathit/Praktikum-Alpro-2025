bulan = input("Masukkan bulan : ")

try:
    bulan = int(bulan)
    if bulan == 1 and 3 and 5 and 7 and 8 and 10 and 12:
        print("Jumlah hari : 31")
    elif bulan == 2:
        print("Jumlah hari : 29")
    else:
        print("Jumlah hari : 30")
except:
    print("Input tidak valid! Harus berupa INTERGER!")