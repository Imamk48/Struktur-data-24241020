# Meminta input dari pengguna untuk menentukan berapa banyak angka Fibonacci yang akan ditampilkan
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

# Menginisialisasi dua angka pertama dalam deret Fibonacci
a, b = 0, 1

# Menampilkan deret Fibonacci sebanyak 'jumlah' angka
for i in range(jumlah):
    print(a, end=' ')  # Menampilkan angka Fibonacci saat ini, diikuti spasi (tanpa pindah baris)
    a, b = b, a + b    # Mengupdate nilai 'a' dan 'b' ke dua angka berikutnya dalam deret Fibonacci