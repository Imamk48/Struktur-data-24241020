# cara membuat tuple singleton
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# Indexing dan Slicing Tuple
# membuat tuple
nama = ('Adam', 'Bachtiar', 'Maulachela')

# mengakses indeks ke 1 dari tuple
print(nama[1])

# Membuat Tuple
t = (1, 5, 10, 15)

# mengubah isi elemen tuple
t[0] = 0

# angka
# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])

# Operasi pada tuple
# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

# Tuple Bersarang (Nested Tuple)
# Nested Tuple atau Tuple Bersarang
t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)

# mula-mula kita buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)