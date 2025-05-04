tinggi = int(input("Masukkan Tinggi Segitiga :"))

with open("jaran.txt", "w") as file:
    for i in range(tinggi):
        for j in range(i + 1):
            file.write("*")
        file.write("\n")
