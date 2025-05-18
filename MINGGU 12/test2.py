namaFile = "mbok-crot.txt"
counts = dict()
with open (namaFile, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

print(counts)