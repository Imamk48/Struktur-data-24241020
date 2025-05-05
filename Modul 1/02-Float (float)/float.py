# cara membuat list
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True]
kosong = []

# memanggil list
print(angka)
print(buah)
print(campuran)
print(kosong)

# Indexing dan Slicing
# indexing dan slicing pada list
data = ["a", "b", "c", "d"]
print(data[0])      # Output: a
print(data[-1])     # Output: d
print(data[1:3])    # Output: ['b', 'c']
print(data[:2])     # Output: ['a', 'b']

# operasi pada list
# Operasi penambahan anggota list
data = [1, 2, 3, 4, 5]
data = data + [10, 20]
print(data)

# Operasi pengulangan list
list = [1, 2]
list = list * 3
print(list)

# Operasi mengukur panjang list
print(len(data))
print(len(list))

# Operasi mengecek keanggotaan pada list
print(20 in data)
print(13 in list)

# Fungsi pada list 
a = [3, 1, 4, 1, 5]
print(a)
a.append(9)         # Menambahkan elemen di akhir
print(a)
a.insert(2, 7)      # Menyisipkan angka 7 di indeks ke-2
print(a)
a.remove(1)         # Menghapus elemen pertama yang bernilai 1
print(a)
a.pop()             # Menghapus elemen terakhir
print(a)
a.sort()            # Mengurutkan list secara ascending
print(a)
a.reverse()         # Membalik urutan elemen
print(a)
print(a.index(4))   # Mengembalikan indeks dari nilai 4
print(a.count(1))   # Menghitung jumlah kemunculan angka 1

# list bersarang (nested ling)
# membuat matriks dari list bersarang
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# memanggil matriks
print(matrix)
# memanggil elemen list pada indeks [1][2]
print(matrix[1][2])  # Output: 6

# looping list
# Contoh looping list
buah = ["apel", "jeruk", "mangga"]

# For Loop
for item in buah:
    print(item)

# Mengakses indeks dan elemen
for i, item in enumerate(buah):
    print(f"{i}: {item}")

# List Comprehension
# Buat list kuadrat dari 0-9
kuadrat = [x**2 for x in range(10)]
print(kuadrat)  # [0, 1, 4, 9, ..., 81]

# Filter hanya bilangan genap
genap = [x for x in range(10) if x % 2 == 0]
print(genap)  # [0, 2, 4, 6, 8]