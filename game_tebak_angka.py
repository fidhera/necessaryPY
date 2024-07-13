#program game tebak angka random
import random

print("Hai, selamat datang di permainan Tebak Angka!")
print("Kamu akan diberikan 5 kesempatan untuk menebak angka acak antara 1 sampai 10")

angka_acak = random.randint(1, 10)
kesempatan = 5

while kesempatan > 0:
    tebakan = int(input("Tebak angkanya: "))
    
    if tebakan == angka_acak:
        print("Selamat, tebakanmu BENAR!")
        break
    else:
        print("Sayang sekali, tebakanmu SALAH!") 
        kesempatan -= 1
        print(f"Kamu masih memiliki {kesempatan} kesempatan lagi")
        
if kesempatan == 0:
    print(f"Sayang sekali, kesempatan menebakmu telah habis. Angka acaknya adalah {angka_acak}")
