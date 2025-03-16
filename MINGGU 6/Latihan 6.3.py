def hitungIPS():
    totalNilai = 0
    A = 4
    B = 3
    C = 2
    D = 1
    E = 0
    jumlahMatkul = input("Berapa jumlah mata kuliah? ")
    try :
        jumlahMatkul = int(jumlahMatkul)
        for _ in range (1, jumlahMatkul+1):
            nilai = input(f"Nilai MK {_} : ")
            if nilai.upper() == "A":
                totalNilai += A
            elif nilai.upper() == "B":
                totalNilai += B
            elif nilai.upper() == "C":
                totalNilai += C
            elif nilai.upper() == "D":
                totalNilai += D
            elif nilai.upper() == "E":
                totalNilai += E
            else:
                print("INPUT TIDAK VALID")
        print(f"Nilai IPS anda semester ini {(totalNilai/jumlahMatkul):.2f}")
    except:
        print("INPUT TIDAK VALID")

hitungIPS()