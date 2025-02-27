def tiket_bioskop(usia, hari):
    if usia < 12:
        if hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis":
            return 25000
        elif hari == "Jumat" or hari == "Sabtu" or hari == "Minggu":
            return 30000
        else:
            return "hari tidak valid"
    else:
        if hari == "Jumat" or hari == "Sabtu" or hari == "Minggu":
            return 50000
        elif hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis":
            return 40000
        else:
            return "hari tidak valid"

print(tiket_bioskop(15, "Liburan"))