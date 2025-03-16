def perkalian(x,y):
    print(f"{x} x {y} =",end=" ")
    for _ in range(x) :
        if _ < x-1 :
            print(y, end=" ")
            print("+", end=" ")
        else:
            print(f"{y} = {x*y}")

perkalian(10,11)
perkalian(6,5)
perkalian(9,2)