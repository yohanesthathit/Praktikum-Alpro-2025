def decipher(nama_file, id):
# nama_file = "terenkripsi.txt"
# id = 14
    try:
        with open(nama_file, "r") as file:
            bacaBaris = file.readlines()
            # print(bacaBaris)
            for i in range (len(bacaBaris)):
                baris = bacaBaris[i].rstrip()
                # print(baris)
                x = baris.split(" ")
                # print(x)
                # print(len(x))
                if len(x) < 2 or len(x) == 1 or x[1].strip() == "":
                    print(f"Tidak menemukan pesan di baris ke-{i+1}")
                    continue

                IDPesan = int(x[0])
                y = int(x[-1])
                pesan = " ".join(x[1:-1])
                # print(pesan)
                z = ""

                if IDPesan == id :
                    for j in pesan:
                        if j.isalpha():
                            xnxx = ord('A') if j.isupper() else ord('a')
                            z += chr((ord(j) - xnxx - y) % 26 + xnxx)
                        else:
                            z += j
                    return (z)

    except FileNotFoundError:
        return("file tidak ditemukan")


print(decipher('terenkripsi.txt',14))
print(decipher('cipher.txt',14))
print(decipher('terenkripsi.txt',1564))
