# Nama : Raffael Fidhera Yahya
# NPM : 51423180
# Kelas : 1IA06

 
# untuk mengambil input
# num = int(input("......"))
angka = int(input("masukan bilangan ==> "))

# jika input angka 1 langsung di proses ke BUKAN BILANGAN PRIMA
if angka == 1:
    print("|========================================|")
    print('|      ',angka,"ini bukan bilangan prima       "  "|")
    print("|========================================|")

# PROSES UTAMA DISINI
# proses jika angka lebih besar dari 1
elif angka > 1:
   # untuk memproses 
   for i in range(2,angka):
       if (angka % i) == 0:
            print("============================================================"),
            print(angka,"ini BUKAN bilangan PRIMA, karena")
            print(i,"dikali",angka//i,"sama dengan",angka)
            print("============================================================"),
            print("bilangan prima itu dapat dibagi dengan 1 dan dirinya sendiri")
            print("============================================================"),
            break
   #
   else:
            print("|==================================|")
            print('|    ',angka," adalah bilangan prima     |")
            print("|==================================|")
        
# proses jika input kurang dari 1
# atau sama dengan 1, itu bukan bilangan prima
else:
   print("|======================================================|"),
   print('|             ',angka,"ini adalah bilangan prima             |")
   print("|======================================================|"),
   print("|angka negatif, 0, dan 1 bukan termasuk bilangan prima!|")
   print("|angka negatif bukan bilangan prima BUKAN BILANGAN ASLI|")
   print("|======================================================|")

   