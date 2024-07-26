#Program menentukan JAM MENIT DETIK dengan menginput DETIK

print()
print('Satuan Waktu')
jd = int(input ("Input Jumlah Detik: "))
print('Setara Dengan')
#Hitung jumlah jam
j = jd//3600

#Hitung jumlah menit
if j > 0:
    m = (jd - j * 3600) // 60
else:
    m = jd //60

#Hitung jumlah detik
d = jd % 60
print(j, "Jam")
print(m, "Menit")
print(d, "Detik")
print()
