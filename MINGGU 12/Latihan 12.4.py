namaFile = "mbok-short.txt"
hasil = {}
with open(namaFile, "r") as teks:
    for line in teks:
        if line.startswith("From "):
            baris = line.split()
            if len(baris) > 1:
                email = baris[1]
                domain = email.split("@")
                domain = domain[1]
                # print(email)
                if domain not in hasil:
                    hasil[domain] = 1
                else:
                    hasil[domain] += 1

print(hasil)