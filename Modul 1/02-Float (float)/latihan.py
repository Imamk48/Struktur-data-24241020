data_mahasiswa = []
jumlah = int(input("Input jumlah mahasiswa: "))

# perulangan untuk memasukkan nama mahasisqa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nilai = list(map(int, input("Masukkan 3 nilai dipisahkan spasi: ").split()))
    rata2 = sum(nilai) / len(nilai)
    data_mahasiswa.append([nama, nilai, rata2])

# Tampilkan semua data
print("\nData Mahaiswa:")
print("Nama\tNilai\t\tRata-rata")
for siswa in data_mahasiswa:
    print(f"{siswa[0]}\t{siswa[1]}\t{siswa[2]:.2f}")

# Tampilkan siswa yang lulus
print("\nMahasiswa Lulus (>= 75):")
for siswa in data_mahasiswa:
    if siswa[2] >= 75:
        print(f"{siswa[0]} - {siswa[2]:.2f}")