file_1 = "tempik.txt"
file_2 = "tempik2.txt"

with open(file_1, "r") as file1, open(file_2, "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    
    max_lines = max(len(lines1), len(lines2))
    
    for i in range(max_lines):
        line1 = lines1[i].rstrip().lower() if i < len(lines1) else ""
        line2 = lines2[i].rstrip().lower() if i < len(lines2) else ""
        
        if line1 != line2:
            print(f"Perbedaan di baris {i+1}:")
            print(f"File 1: {line1}")
            print(f"File 2: {line2}")
