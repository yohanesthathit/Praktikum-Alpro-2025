def ganjil(bawah, atas):
    if bawah > atas:
        for _ in range(bawah, atas-1,-1):
            if _ % 2 != 0:
                print(_, end=" ")
    else:    
        for _ in range(bawah, atas+1):
            if _ % 2 != 0:
                print(_, end=" ")
    print("\n")

ganjil(10,30)
ganjil(97,82)