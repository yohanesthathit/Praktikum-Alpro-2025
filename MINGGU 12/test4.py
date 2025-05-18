import string
namaFile = "romeo.txt"
counts = dict()
with open(namaFile, "r") as file:
    for line in file:
        line = line.rstrip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
print(counts)