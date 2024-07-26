# Program Fibonacci

'''Fibonacci adalah nama dari deret bilangan yang dihasilkan dengan
menjumlahkan dua bilangan sebelumnya untuk mendapatkan bilangan berikutnya.

contohnya:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...   '''


# Cetak judul
print("==========================================")
print("|                                        |")
print("| Program Menampilkan Bilangan Fibonacci |")
print("|                                        |")
print("==========================================")

print()
print()
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Contoh penggunaan fungsi untuk menampilkan deret Fibonacci hingga ke-n
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))
fibonacci_long = fibonacci(n)
print(f"Deret Fibonacci hingga ke-{n} adalah:")
print(fibonacci_long)