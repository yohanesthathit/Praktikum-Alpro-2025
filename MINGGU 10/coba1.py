def decryptThis(filePath):
    filePath = "encrypted.txt"
    try:
        with open(filePath, "r") as file:
            bacaBaris = file.readlines()
            print(bacaBaris)
            for i in range (len(bacaBaris)):
                baris = bacaBaris[i].rstrip()
                # print(baris)
                x = baris.split(" ", 1)
                # print(len(x))
                # print(x[1].strip() == "")
                if len(x) < 2 or len(x) == 1 or x[1].strip() == "":
                    print(f"Tidak menemukan pesan di baris ke-{i+1}")
                    continue

                y = int(x[0])
                pesan = x[1]
                z = ""
                for j in pesan:
                    if j.isalpha():
                        if j.isupper():
                            xnxx = ord('A')
                            z += chr((ord(j) - xnxx - y) % 26 + xnxx)
                        elif j.islower():
                            xnxx = ord('a')
                            z += chr((ord(j) - xnxx - y) % 26 + xnxx)
                    elif j in "4310":
                        aeio = {'4': 'a', '3': 'e', '1': 'i', '0': 'o'}
                        z += aeio[j]
                    else:
                        z += j

                print(f"{i+1}.  {z}")

    except FileNotFoundError:
            print("Surat tidak bisa ditemukan!")