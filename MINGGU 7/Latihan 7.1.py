def prima_terdekat(n):
    prima = 0
    is_prima = True
    for j in range(n-1, 1, -1):
        for i in range(2, int(j ** 0.5) + 1):
            if j % i == 0:
                is_prima = False
                break
            else:
                is_prima = True
        if is_prima == True:
            prima = j
            break
    
    print(f"Bilangan prima terdekat < {n} adalah {prima}")

n = int(input("Masukkan suatu bilangan : "))
prima_terdekat(n)