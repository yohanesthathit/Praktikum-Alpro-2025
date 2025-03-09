def cek_angka(a,b,c):
    if a != b and a != c and b != a and b!=c and c != a and c != b:
        if a + b == c or a + c == b or b + a == c or b + c == a or c + a == b or c + b == a:
            return True
        else :
            return False
    else:
        return False


print(cek_angka(1,2,3))
print(cek_angka(3,2,1))
print(cek_angka(2,1,3))
print(cek_angka(3,2,3))
print(cek_angka(1,3,3))
print(cek_angka(1,1,3))