bilangan = [13,51,29,99,111,1,5,6,2]

unik = list(set(bilangan))
unik.sort(reverse=True)
for i in range (3):
    if i == 2:
        print(unik[i])
    else:
        print(unik[i], end=", ")