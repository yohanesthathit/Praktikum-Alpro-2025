namaFile = "Karma.txt"
with open (namaFile, "r") as teks:
    isi = teks.read()

isi = isi.replace('\n', ' ').lower()
# print(isi)

pisah = isi.split(" ")
# print(pisah)

unik = sorted(set(pisah))
# print(unik)
print("Kata unik :")
for i in range (len(unik)):
    if i < len(unik)-1:
        print(unik[i], end=", ")
    else:
        print(f"{unik[i]}.")