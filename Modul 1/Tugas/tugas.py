# Langkah 1: Minta input dari pengguna untuk menentukan berapa banyak mahasiswa yang ingin didata
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))  # Mengubah input menjadi integer (bilangan bulat)

# Langkah 2: Siapkan struktur data utama yaitu dictionary untuk menyimpan data semua mahasiswa
data_mahasiswa = {}  # Format: {NIM: {'nama': ..., 'nilai': [(matkul1, nilai1), (matkul2, nilai2), ...]}}

# Langkah 3: Lakukan pengulangan sebanyak jumlah mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")  # Memberi tahu urutan input saat ini

    # Input data dasar mahasiswa
    nim = input("Masukkan NIM: ")  # NIM digunakan sebagai key di dictionary utama
    nama = input("Masukkan Nama: ")  # Nama disimpan sebagai bagian dari value-nya

    # Langkah 4: Siapkan list untuk menyimpan mata kuliah dan nilai
    daftar_nilai = []  # Ini akan menyimpan tuple seperti: ('Matematika', 80)

    # Langkah 5: Input mata kuliah dan nilai dilakukan berulang kali
    while True:
        matkul = input("Masukkan nama mata kuliah (atau 'selesai' untuk berhenti): ")
        
        # Cek apakah input adalah kata "selesai", jika iya, keluar dari perulangan
        if matkul.lower() == 'selesai':
            break
        
        # Input nilai untuk mata kuliah tersebut
        nilai = float(input(f"Masukkan nilai untuk mata kuliah {matkul}: "))  # float karena nilai bisa desimal
        
        # Simpan sebagai tuple dalam list
        daftar_nilai.append((matkul, nilai))

    # Langkah 6: Simpan data lengkap mahasiswa ke dalam dictionary
    data_mahasiswa[nim] = {
        'nama': nama,         # Simpan nama
        'nilai': daftar_nilai # Simpan list mata kuliah dan nilainya
    }

# Langkah 7: Tampilkan nilai rata-rata setiap mahasiswa
print("\n===== Daftar Mahasiswa dan Nilai Rata-Rata =====")
for nim, info in data_mahasiswa.items():
    nama = info['nama']        # Ambil nama dari dictionary
    nilai_list = info['nilai'] # Ambil list tuple nilai
    
    # Cek jika nilai_list tidak kosong agar tidak error saat dihitung
    if nilai_list:
        total = sum(nilai for _, nilai in nilai_list)  # Jumlah semua nilai
        rata_rata = total / len(nilai_list)            # Hitung rata-rata
    else:
        rata_rata = 0  # Jika tidak ada mata kuliah, rata-rata dianggap 0

    # Tampilkan data
    print(f"NIM: {nim} | Nama: {nama} | Nilai Rata-Rata: {rata_rata:.2f}")  # Tampilkan 2 angka di belakang koma

# Langkah 8: Tampilkan semua data mahasiswa secara lengkap
print("\n===== Seluruh Data Mahasiswa =====")
for nim, info in data_mahasiswa.items():
    print(f"\nNIM: {nim}")               # Tampilkan NIM
    print(f"Nama: {info['nama']}")       # Tampilkan Nama
    print("Nilai:")                      # Judul bagian nilai
    
    # Tampilkan semua mata kuliah dan nilai satu per satu
    for matkul, nilai in info['nilai']:
        print(f" - {matkul}: {nilai}")   # Format: - Matematika: 80.0
