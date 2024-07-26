# Program Konversi Suhu / temperature conversion program

# Cetak Judul
options = '''
=============================
Pengkonversian Suhu

1. Celcius ke semua suhu
2. Fahrenheith ke semua suhu
3. Kelvin ke semua suhu
4. Reamur ke semua suhu
=============================
'''

# Proses Perhitungan, Jika Input dari Celcius
def celciusConverter():
    try:
        value = int(input('Masukkan Nilai Celcius: '))
    except:
        print('Nilai yang dimasukkan harus berupa angka.')
        return celciusConverter()
    
    reamur = (4/5) * value
    farenheith = (9/5) * value + 32
    kelvin = value + 273
    
    print(f' [=>] : {farenheith:.2f} °F')
    print(f' [=>] : {kelvin:.2f} °K')
    print(f' [=>] : {reamur:.2f} °R')

# Proses Perhitungan, Jika Input dari Fahrenheit
def farenheithConverter():
    try:
        value = int(input('Masukkan Nilai Fahrenheit: '))
    except:
        print('Nilai yang dimasukkan harus berupa angka.')
        return farenheithConverter()
    
    celcius = (5/9) * (value - 32)
    reamur = (4/9) * (value - 32)
    kelvin = (value - 32) * 5/9 + 273.15
    
    print(f' [=>] : {celcius:.2f} °C')
    print(f' [=>] : {kelvin:.2f} °K')
    print(f' [=>] : {reamur:.2f} °R')

# Proses Perhitungan, Jika Input dari Kelvin
def kelvinConverter():
    try:
        value = int(input('Masukkan Nilai Kelvin: '))
    except:
        print('Nilai yang dimasukkan harus berupa angka.')
        return kelvinConverter()
    
    celcius = value - 273
    reamur = (4/5) * (value - 273)
    farenheith = (value - 273.15) * 9/5 + 32
    
    print(f' [=>] : {celcius:.2f} °C')
    print(f' [=>] : {farenheith:.2f} °F')
    print(f' [=>] : {reamur:.2f} °R')

# Proses Perhitungan, Jika Input dari Reamur
def reamurConverter():
    try:
        value = int(input('Masukkan Nilai Reamur: '))
    except:
        print('Nilai yang dimasukkan harus berupa angka.')
        return reamurConverter()
    
    celcius = (5/4) * value
    farenheith = (9/4) * value + 32
    kelvin = (5/4) * value + 273
    
    print(f' [=>] : {celcius:.2f} °C')
    print(f' [=>] : {farenheith:.2f} °F')
    print(f' [=>] : {kelvin:.2f} °K')

# Kondisi
def main():
    print(options)
    try:
        opt = int(input('Pilih Opsi: '))
    except:
        print('Opsi yang dipilih harus berupa angka.')
        return main()
    
    if opt == 1:
        celciusConverter()
    elif opt == 2:
        farenheithConverter()
    elif opt == 3:
        kelvinConverter()
    elif opt == 4:
        reamurConverter()
    else:
        print('Opsi yang dipilih tidak tersedia.')
        return main()
    
if __name__ == '__main__':
    while True:
        main()
        again = input('Ada yang ingin ditanyakan lagi? (Y/T): ').strip().lower()
        if again != 'y':
            print("Terima kasih!")
            break
