# Ini adalah list untuk menyimpan data nama siswa
data_siswa = []  # Variabel data_siswa digunakan untuk menyimpan nama-nama siswa dalam bentuk list.

# Fungsi untuk menampilkan menu pilihan ke pengguna
def show_menu():
    print("\n===== MENU =====")
    print("1. Tambah siswa")  # Opsi untuk menambah siswa baru
    print("2. Lihat semua siswa")  # Opsi untuk melihat daftar semua siswa
    print("3. Ubah nama siswa")  # Opsi untuk mengubah nama siswa
    print("4. Hapus siswa")  # Opsi untuk menghapus siswa
    print("5. Keluar dari program")  # Opsi untuk keluar dari program

    # Ambil input dari pengguna
    pilihan = input("Pilih menu (1-5): ")  # Menunggu input pilihan menu dari pengguna

    # Panggil fungsi sesuai pilihan
    if pilihan == '1':  # Jika pilihan 1, panggil fungsi untuk menambah siswa
        tambah_siswa()
    elif pilihan == '2':  # Jika pilihan 2, panggil fungsi untuk melihat semua siswa
        lihat_siswa()
    elif pilihan == '3':  # Jika pilihan 3, panggil fungsi untuk mengubah nama siswa
        ubah_siswa()
    elif pilihan == '4':  # Jika pilihan 4, panggil fungsi untuk menghapus siswa
        hapus_siswa()
    elif pilihan == '5':  # Jika pilihan 5, keluar dari program
        print("Sampai jumpa! 👋")
        exit()  # Menghentikan program
    else:  # Jika input tidak valid, beri tahu pengguna
        print("Pilihan tidak valid. Coba lagi ya!")  

# Fungsi untuk menambahkan nama siswa ke list
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")  # Meminta input nama siswa dari pengguna
    data_siswa.append(nama)  # Menambahkan nama siswa yang dimasukkan ke dalam list data_siswa
    print(f"Siswa bernama '{nama}' berhasil ditambahkan!")  # Memberi konfirmasi bahwa siswa berhasil ditambahkan

# Fungsi untuk menampilkan semua nama siswa
def lihat_siswa():
    if len(data_siswa) == 0:  # Mengecek apakah list data_siswa kosong
        print("Belum ada data siswa.")  # Jika kosong, beri tahu pengguna
    else:
        print("\nDaftar Siswa:")  # Menampilkan daftar siswa
        for i in range(len(data_siswa)):  # Melakukan iterasi untuk menampilkan semua siswa
            print(f"{i}. {data_siswa[i]}")  # Menampilkan nomor indeks dan nama siswa

# Fungsi untuk mengubah nama siswa berdasarkan indeks
def ubah_siswa():
    lihat_siswa()  # Menampilkan daftar siswa
    indeks_input = input("Masukkan nomor indeks siswa yang ingin diubah: ")  # Meminta input indeks siswa yang ingin diubah

    # Cek apakah input angka
    if indeks_input.isdigit():  # Memastikan input adalah angka
        indeks = int(indeks_input)  # Mengubah input ke dalam bentuk integer
        # Cek apakah indeks valid (dalam rentang list)
        if 0 <= indeks < len(data_siswa):
            nama_baru = input("Masukkan nama baru: ")  # Meminta nama baru dari pengguna
            data_siswa[indeks] = nama_baru  # Mengubah nama siswa pada indeks yang dipilih
            print("Nama siswa berhasil diubah.")  # Memberi konfirmasi bahwa nama siswa telah diubah
        else:
            print("Indeks tidak ditemukan.")  # Menangani kasus jika indeks tidak valid
    else:
        print("Masukkan angka yang benar, ya!")  # Menangani jika input bukan angka

# Fungsi untuk menghapus siswa dari list
def hapus_siswa():
    lihat_siswa()  # Menampilkan daftar siswa
    indeks_input = input("Masukkan nomor indeks siswa yang ingin dihapus: ")  # Meminta input indeks siswa yang ingin dihapus

    # Validasi input
    if indeks_input.isdigit():  # Memastikan input adalah angka
        indeks = int(indeks_input)  # Mengubah input ke dalam bentuk integer
        if 0 <= indeks < len(data_siswa):  # Memastikan indeks valid (ada dalam rentang list)
            nama = data_siswa.pop(indeks)  # Menghapus siswa berdasarkan indeks dan mendapatkan nama siswa yang dihapus
            print(f"Data siswa '{nama}' berhasil dihapus.")  # Memberi konfirmasi bahwa siswa telah dihapus
        else:
            print("Indeks tidak ditemukan.")  # Menangani kasus jika indeks tidak valid
    else:
        print("Masukkan angka yang benar, ya!")  # Menangani jika input bukan angka

# Program utama, akan terus jalan sampai user memilih keluar
if __name__ == "__main__":
    while True:  # Looping agar program terus berjalan
        show_menu()  # Menampilkan menu pilihan kepada pengguna
