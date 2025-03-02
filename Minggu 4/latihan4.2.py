bilangan = input("Masukkan suatu bilangan : ")

try:
    bilangan = int(bilangan)
    cabang = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol"
    print(cabang)
except:
    print("Input tidak valid! Harus berupa INTERGER!")