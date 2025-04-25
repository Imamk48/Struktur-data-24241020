# Ini adalah list untuk menyimpan data nama siswa
data_siswa = []

# Fungsi untuk menampilkan menu pilihan ke pengguna
def show_menu():
    print("\n===== MENU =====")
    print("1. Tambah siswa")
    print("2. Lihat semua siswa")
    print("3. Ubah nama siswa")  
    print("4. Hapus siswa")
    print("5. Keluar dari program")

    # Ambil input dari pengguna
    pilihan = input("Pilih menu (1-5): ")

    # Panggil fungsi sesuai pilihan
    if pilihan == '1':
        tambah_siswa()  
    elif pilihan == '2':
        lihat_siswa()  
    elif pilihan == '3':
        ubah_siswa()  
    elif pilihan == '4':
        hapus_siswa()  
    elif pilihan == '5':
        print("Sampai jumpa! 👋")  
        exit() 
    else:
        print("Pilihan tidak valid. Coba lagi ya!") 

# Fungsi untuk menambahkan nama siswa ke list
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")  
    data_siswa.append(nama)  
    print(f"Siswa bernama '{nama}' berhasil ditambahkan!")

# Fungsi untuk menampilkan semua nama siswa
def lihat_siswa():
    if len(data_siswa) == 0:
        print("Belum ada data siswa.")  
    else:
        print("\nDaftar Siswa:")
        for i in range(len(data_siswa)):
            print(f"{i}. {data_siswa[i]}")  

# Fungsi untuk mengubah nama siswa berdasarkan indeks
def ubah_siswa():
    lihat_siswa() 
    indeks_input = input("Masukkan nomor indeks siswa yang ingin diubah: ")

    # Cek apakah input angka
    if indeks_input.isdigit():
        indeks = int(indeks_input)
        if 0 <= indeks < len(data_siswa):
            nama_baru = input("Masukkan nama baru: ")  
            data_siswa[indeks] = nama_baru  
            print("Nama siswa berhasil diubah.")
        else:
            print("Indeks tidak ditemukan.") 
    else:
        print("Masukkan angka yang benar, ya!")  

# Fungsi untuk menghapus siswa dari list
def hapus_siswa():
    lihat_siswa() 
    indeks_input = input("Masukkan nomor indeks siswa yang ingin dihapus: ")

    # Validasi input
    if indeks_input.isdigit():
        indeks = int(indeks_input)
        if 0 <= indeks < len(data_siswa):
            nama = data_siswa.pop(indeks)  
            print(f"Data siswa '{nama}' berhasil dihapus.")
        else:
            print("Indeks tidak ditemukan.") 
    else:
        print("Masukkan angka yang benar, ya!") 

# Program utama, akan terus jalan sampai user memilih keluar
if __name__ == "__main__":
    while True:
        show_menu()  
