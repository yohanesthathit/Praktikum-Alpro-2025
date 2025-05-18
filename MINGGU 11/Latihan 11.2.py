z = []
while True:
    x = input("X : ")
    x = x.lower()
    if x == "done":
        break
    x = int(x)
    z.append(x)
print(f'Rata - Rata = {sum(z)/len(z)}')