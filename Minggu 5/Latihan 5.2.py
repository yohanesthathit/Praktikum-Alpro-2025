def cek_digit_belakang(a,b,c):
    belakang_a = a % 10
    belakang_b = b % 10
    belakang_c = c % 10

    if belakang_a == belakang_b or belakang_a == belakang_c or belakang_b == belakang_a or belakang_b == belakang_c or belakang_c == belakang_a or belakang_c == belakang_b:
        return True
    else:
        return False

print(cek_digit_belakang(30,20,18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))