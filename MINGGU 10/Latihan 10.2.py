nama_file = input("Nama file1: ")
with open(nama_file, "r") as file:
    for line in file:
        line = line.rstrip()
        line = line.lower()
        line = line.split(" || ")
        print(line[0])
        x = input(f"Jawab : ")
        x = x.lower()
        if x == line[1]:
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")