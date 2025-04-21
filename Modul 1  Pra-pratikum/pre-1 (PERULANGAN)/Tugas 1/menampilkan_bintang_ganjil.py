# Menampilkan Bintang Ganjil (piramida bintang kecil)

# Loop hanya pada angka ganjil: 1, 3, 5
for i in range(1, 6, 2):  
    # ' ' * ((5 - i) // 2): Menambahkan spasi agar bintang berada di tengah
    # '*' * i: Menampilkan bintang sebanyak i (jumlah ganjil)
    print(' ' * ((5 - i) // 2) + '*' * i)
