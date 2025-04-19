# Menampilkan deret bilangan genap dari inputan keyboard

# Program meminta user untuk memasukkan berapa banyak bilangan genap yang ingin ditampilkan
jumlah = int(input("Masukkan jumlah deret genap: "))

angka = 2  # Kita mulai dari 2, karena 2 adalah bilangan genap pertama
deret = []  # List kosong untuk menyimpan deret bilangan genap

# Mengisi list deret dengan bilangan genap sebanyak 'jumlah' kali
for i in range(jumlah):
    deret.append(str(angka))  # Ubah angka ke string sebelum dimasukkan ke list (untuk kemudahan saat print)
    angka += 2  # Menambahkan 2 untuk mendapatkan bilangan genap berikutnya

# Menampilkan deret bilangan genap yang telah disusun, dipisahkan dengan koma
print(', '.join(deret))

# Menampilkan jumlah total dari seluruh bilangan genap dalam deret
print("Jumlah total:", sum(map(int, deret)))  # Ubah elemen list ke integer untuk dijumlahkan
