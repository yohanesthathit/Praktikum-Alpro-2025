gaji = int(input("Masukkan gaji yang anda inginkan : "))
jam = int(input("Masukkan jam kerja anda selama 1 minggu : "))

pendapatanBudi = gaji * jam * 5
Setelahpajak = pendapatanBudi - (pendapatanBudi * 0.14)
pakaianAkesoris = (Setelahpajak * 0.1)
alatTulis = Setelahpajak * 0.01
uangBudi = Setelahpajak - (pakaianAkesoris + alatTulis)
sedekah = 0.25 * uangBudi
yatim = 0.3 * sedekah
dhuafa = 0.7 * sedekah

print("Pendapatan Budi selama musim panas sebelum pajak = ", pendapatanBudi)
print("Pendapatan Budi selama musim panas setelah pajak = ", Setelahpajak)
print("Jumlah uang yang akan dihabiskan untuk membeli pakaian dan aksesoris = ", pakaianAkesoris)
print("Jumlah uang yang akan dihabiskan untuk membeli ATK = ", alatTulis)
print("Jumlah uang yang akan disedekahkan = ", sedekah)
print("Jumlah uang yang akan diterima anak yatim = ", yatim)
print("Jumlah uang yang akan diterima kaum dhuafa = ", dhuafa)