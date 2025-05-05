# tipe data numerik
# Tipe data float (float)
a = 3.141592
b = -0.001
c = 1.0
d = float('inf') # memasukkan infinity sebagai float

# melihat isi variabel
print(a)
print(b)
print(c)
print(d)

# cek tipe data dari variabel
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'float'>

# contohnya
# membandingkan nilai b3 dengan yang lain
if (a < d):
    print('lebih kecil')
else:
    print('lebih besar')

# Operasi aritmatika pada float
print(a + c)
print(b ** a)
print(abs(a))

# ciri data khas tipe data Float
# hasil operasi aritmatika pada float
float = b * a
print(float)
print(type(float))

# mengubah hasil operasi aritmatika float menjadi integer
print(int(b * a))