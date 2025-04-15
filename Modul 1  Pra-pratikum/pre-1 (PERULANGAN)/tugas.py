# tugas for-loop dari 3 soal

# Menampilkan Bintang Ganjil
for i in range(1, 6, 2):    # Mulai dari 1, hingga 5, loncat 2
    print(' ' * ((5 - i) // 2) + '*' * i)

print("akhir perulangan bintang/n")

# Menampilkan deret bilangan genap dari inputan keyboard
jumlah = int(input("Masukkan jumlah deret genap: "))

# Menampilkan deret genap
angka = 2
for i in range(jumlah):
    print(angka, end=' ')
    angka += 2

print("akhir perulangan deret/n")

# Menampilkan deret Fibonacci dari inputan keyboard
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

# Inisialisasi dua angka pertama Fibonacci
a, b = 0, 1

# Menampilkan deret Fibonacci
for i in range(jumlah):
    print(a, end=' ')
    a, b = b, a + b

print("akhir perulangan fibonaci/n")
