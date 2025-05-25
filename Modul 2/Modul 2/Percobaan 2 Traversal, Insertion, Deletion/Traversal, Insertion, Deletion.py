# Praktek 4 : Linear Traversal
# membuat array
arr = [1, 2, 3, 4, 5]

# Linear Traversal ke tiap elemen arr
print("Linear Traversal: ", end=" ")
for i in arr:
    print(i, end=" ")
print()


# Praktek 5 : Reverse Traversal
# membuat array
arr = [1, 2, 3, 4, 5]

# Reverse Traversal dari elemen akhir 
print("Reverse Traversal: ", end="")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()


# Praktek 7 : Linear Traversal dengan Metode While
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
n = len(arr)
i = 0

print("Linear Traversal using while loop: ", end=" ")
# Linear Traversal dengan while
while i < n:
    print(arr[i], end=" ")
    i += 1
print()


# Praktek 8 : Reverse Traversal dengan Metode While
# membuat array
arr = [1, 2, 3, 4, 5]

# mendeklarasikan nilai awal
start = 0
end = len(arr) - 1

print("Reverse Traversal using while loop: ", end=" ")
# Reverse Traversal dengan while
while start < end:
    # mengubah indeks array
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)


# Praktek 9 : Insertion pada akhir elemen array
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array di akhir elemen menggunakan .append()
arr.append(26)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))


# Praktek 10 : Insertion pada tengah elemen array
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(4, 5)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

# jika tidak menggunakan fungsi .insert()
# membuat array dan cetak array
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Penyisipan : " , arr)

# Deklarasi elemen tengah yang disisipkan
pos = 4

# Deklarasi nilai yang akan disisipkan
x = 5

# menambah elemen dummy agar menambah panjang array
arr.append(0) # arr = [12, 16, 20, 40, 50, 70, 0]

# melakukan pergeseran elemen mulai dari belakang
for i in range(len(arr) - 2, pos-1, -1):
    arr[i + 1] = arr[i]

# memasukkan nilai x pada elemen yang diinginkan
arr[pos] = x

# Cetak array baru
print("Array Sesudah Penyisipan : ", arr)


# Praktek 11 : Menghapus array
# membuat array
a = [10, 20, 30, 40, 50]
print("Array Sebelum Deletion : ", a)

# menghapus elemen array pertama yang nilainya 30
a.remove(30)  
print("Setelah remove(30):", a)

# menghapus elemen array pada index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("Setelah pop(1):", a) 

# Menghapus elemen pertama (10)
del a[0]  
print("Setelah del a[0]:", a)