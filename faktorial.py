# Program Menghitung Faktorial dengan Input 

# Cetak judul
print("===========================================")
print("|                                         |")
print("|      Program Menghitung Faktorial       |")
print("|                                         |")
print("===========================================")
print()
print()

def faktorial(n):
    faktorial = 1
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial

# Input bilangan bulat
bilangan = int(input("   * Masukkan bilangan bulat positif: "))
print()

# Memanggil fungsi faktorial
hasil_faktorial = faktorial(bilangan)

# Menampilkan hasil faktorial
print()
print("===========================================")
print("       Faktorial dari", bilangan, "adalah =>", hasil_faktorial)
print("===========================================")
print()
