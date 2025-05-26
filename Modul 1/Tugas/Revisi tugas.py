# Program Rekap Nilai Mahasiswa

# Menyimpan semua data mahasiswa dalam dictionary
data_mahasiswa = {}  # Format: {NIM: {'nama': ..., 'matkul': {...}, 'rata_rata': ...}}

# Meminta input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))  # Input harus berupa angka bulat (int)

# Memulai input data untuk setiap mahasiswa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")  # Menandai mahasiswa keberapa yang sedang diinput
    nim = input("Masukkan NIM: ")  # Input NIM (sebagai key utama)
    nama = input("Masukkan Nama: ")  # Input nama mahasiswa
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))  # Input berapa banyak mata kuliah yang diambil

    matkul = {}  # Dictionary untuk menyimpan nama mata kuliah dan nilainya
    total_nilai = 0  # Inisialisasi total nilai untuk menghitung rata-rata nanti

    # Input mata kuliah dan nilainya sebanyak jumlah_matkul
    for j in range(jumlah_matkul):
        nama_matkul = input(f"  Nama Mata Kuliah ke-{j+1}: ")  # Nama mata kuliah
        nilai = float(input(f"  Nilai Mata Kuliah {nama_matkul}: "))  # Nilai mata kuliah (bisa desimal)
        matkul[nama_matkul] = nilai  # Simpan ke dictionary matkul
        total_nilai += nilai  # Tambahkan nilai ke total

    # Hitung rata-rata nilai mahasiswa
    rata_rata = total_nilai / jumlah_matkul  # Total nilai dibagi jumlah mata kuliah

    # Simpan semua data ke dictionary utama
    data_mahasiswa[nim] = {
        "nama": nama,            # Simpan nama mahasiswa
        "matkul": matkul,        # Simpan daftar nilai mata kuliah
        "rata_rata": rata_rata   # Simpan hasil perhitungan rata-rata
    }

# Menampilkan hasil rekapitulasi data
print("\n=== Daftar Nilai Mahasiswa ===")
for nim, info in data_mahasiswa.items():  # Ulangi semua mahasiswa berdasarkan NIM
    print(f"\nNIM     : {nim}")              # Tampilkan NIM
    print(f"Nama    : {info['nama']}")      # Tampilkan nama
    print("Nilai Mata Kuliah:")             # Tampilkan daftar nilai mata kuliah
    for mk, nilai in info['matkul'].items():
        print(f"  {mk} : {nilai}")           # Tampilkan nama mata kuliah dan nilainya
    print(f"Rata-rata Nilai: {info['rata_rata']:.2f}")  # Tampilkan nilai rata-rata (dua angka di belakang koma)
