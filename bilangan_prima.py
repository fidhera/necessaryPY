# Program Menentukan Bilangan Prima dengan Input 
# Prime Number Program with Input

# Cetak judul
print("==========================================")
print("|                                        |")
print("|   Program Menentukan Bilangan Prima    |")
print("|                                        |")
print("==========================================")
 
# untuk mengambil input
# num = int(input("......"))
print()
angka = int(input("Masukan bilangan: "))
print()

# jika input angka 1 langsung di proses ke BUKAN BILANGAN PRIMA
if angka == 1:
    print()
    print("|========================================|")
    print('      ',angka,"ini bukan bilangan prima       ")
    print("|========================================|")
    print()

# PROSES UTAMA DISINI
# proses jika angka lebih besar dari 1
elif angka > 1:
   # untuk memproses 
   for i in range(2,angka):
       if (angka % i) == 0:
            print()
            print("============================================================"),
            print(angka,"ini BUKAN BILANGAN PRIMA, karena")
            print(i,"dikali",angka//i,"sama dengan",angka)
            print("============================================================"),
            print("bilangan prima itu dapat dibagi dengan 1 dan dirinya sendiri")
            print("============================================================"),
            print()
            break
   #
   else:
            print("|==================================|")
            print('    ',angka," adalah BILANGAN PRIMA     ")
            print("|==================================|")
            print()
        
# proses jika input kurang dari 1
# atau sama dengan 1, itu bukan bilangan prima
else:
   print("|======================================================|"),
   print('|             ',angka,"ini adalah bilangan prima             |")
   print("|======================================================|"),
   print("|angka negatif, 0, dan 1 bukan termasuk bilangan prima!|")
   print("|angka negatif bukan bilangan prima BUKAN BILANGAN ASLI|")
   print("|======================================================|")
   print()
   