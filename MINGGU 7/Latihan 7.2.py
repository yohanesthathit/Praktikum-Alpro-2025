def deretFaktorial(n):
    z = 1

    for i in range(1,n+1):
        z *= i

    for j in range(1,n+1):
        for i in range(n+1,0,-1):
            if i == n+1:
                print(z, end=" ")
                z = z // n
            elif i == 1:
                print(i)
            else:
                print(i, end=" ")
        n-=1

n = int(input("Masukkan bilangan n : "))
deretFaktorial(n)