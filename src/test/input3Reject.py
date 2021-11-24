#test case: while, True, break

# KAMUS
# N = int

# ALGORITMA
N = int(input("Masukkan N: "))  # memasukkan nilai N
a = 1   # inisialisasi (elemen awal)

while a <= N: # pengulangan dari 1 sampai kurang dari sama dengan N
    a = a * 10
print(a)

jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break random_words

print("Total perulagan: {hitung}")