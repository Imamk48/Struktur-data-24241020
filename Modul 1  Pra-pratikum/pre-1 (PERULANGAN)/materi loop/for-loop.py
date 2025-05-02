# PERULANGAN (LOOP)

# for-loop
# for kondisi:
#   aksi

a = 0
a += 1 # a = a + 1
print (a)
a += 1
print (a)
a += 1
print (a)

# Perulangan dengan list
angka_list = [0,1,4,8,10]
for i in angka_list:
    print (f"i sekarang -> {i}")

print("ini akhir for 1/n")

# perulangan dengan range
angka_range = range(5) # diulang 5 kali

for i in angka_range:
    print (f"i sekarang -> {i}")

print("ini akhir for 2/n")

angka_range2 = range(1, 10) #di ulang 9/10
for i in angka_range2:
    print (f"i sekarang -> {i}")

print("ini akhir for 3/n")

data_str = "pendididkan mandalika"
for huruf in data_str:
    print(huruf)

print("akhir perulangan string/n")


#latihan
#forloop dengang nama
nama = "imam"
for i, huruf in enumerate(nama) :
    print(f"huruf ke-{i + 1}: {huruf}")

print("ini akhir for nama/n")

#forloop dengang nama
data_str = "imam"
for huruf in data_str :
    print(huruf)

print ("akhir perulangan string")
