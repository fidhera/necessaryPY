# Program Program Mencari Nilai Determinan MATRIKS dengan Input 

import numpy as np  # Mengimpor pustaka NumPy untuk operasi matriks


# Cetak judul
print("=================================================")
print("|                                               |")
print("|   Program Mencari Nilai Determinan MATRIKS    |")
print("|                                               |")
print("=================================================")
def input_matrix():
#    Fungsi untuk menginput matriks dari pengguna.

    print()
    print("Masukkan ukuran matriks (misal: 2x2)")
    
    # Meminta ukuran matriks dari pengguna dalam format "mxn"
    size = input("Ukuran: ")
    rows, cols = map(int, size.split('x'))  # Memisahkan ukuran menjadi jumlah baris dan kolom
    
    # Menampilkan instruksi untuk menginput nilai matriks
    print()
    print(f"Masukkan nilai {'baris' if rows > 1 else 'elemen'} matriks (dipisahkan dengan spasi):")
    
    matrix = []  # Inisialisasi list untuk menyimpan baris-baris matriks
    
    # Menginput nilai setiap baris matriks
    for i in range(rows):
        row = list(map(float, input(f"Baris ke-{i+1}: ").split()))
        
        # Memeriksa apakah jumlah elemen yang diinput sesuai dengan jumlah kolom
        if len(row) != cols:
            print(f"Jumlah {'kolom' if cols > 1 else 'elemen'} tidak sesuai dengan ukuran matriks")
            return None  # Mengembalikan None jika jumlah elemen tidak sesuai
        
        matrix.append(row)  # Menambahkan baris ke matriks
    
    return np.array(matrix)  # Mengembalikan matriks dalam bentuk array NumPy

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    print()
    print()
    print("Masukkan matriks A:")
    matrix_a = input_matrix()  # Meminta input matriks A dari pengguna
    if matrix_a is None:
        return  # Keluar dari fungsi jika input matriks A tidak valid
    
    print("\nMasukkan matriks B:")
    matrix_b = input_matrix()  # Meminta input matriks B dari pengguna
    if matrix_b is None:
        return  # Keluar dari fungsi jika input matriks B tidak valid
    
    try:
        # Menghitung determinan dari hasil perkalian matriks A dan B
        det_ab = np.linalg.det(np.dot(matrix_a, matrix_b))
        
        # Menampilkan nilai determinan
        print(f"\nDeterminan matriks AB: {det_ab}")
    except np.linalg.LinAlgError:
        # Menangani kesalahan jika determinan tidak bisa dihitung
        print("Determinan tidak bisa dihitung karena matriks tidak memenuhi syarat")

if __name__ == "__main__":
    main()  # Menjalankan fungsi utama jika file ini dieksekusi langsung
