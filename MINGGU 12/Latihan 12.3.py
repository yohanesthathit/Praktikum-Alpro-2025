namaFile = "mbok-short.txt"
hasil = {}
with open(namaFile, "r") as teks:
    for line in teks:
        if line.startswith("From "):
            baris = line.split()
            if len(baris) > 1:
                email = baris[1]
                # print(email)
                if email not in hasil:
                    hasil[email] = 1
                else:
                    hasil[email] += 1

print(hasil)