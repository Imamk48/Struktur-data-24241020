# variabel global untuk menyimpan data buku
buku = []

#fungsi untuk menampilkan semua data buku
def snow_data():
    if len(buku) <=0 :
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

def insert_data():
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)

def edit_data():
    snow_data()
    indeks = int(input("Inputkan Id Buku :" ))
    if(indeks > len(buku)):
        print("Id Buku Tidak Ditemukan")
    else:
        judul_baru = input("judul baru : ")
        buku[indeks] = judul_baru

def delete_data():
    snow_data()
    indeks = int(input("inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        buku.remove(buku[indeks])
        print(f"Buku Dengan ID{indeks} Terhapus")
        
def snow_menu():
    print("\n")
    print(5*"-","MENU", 5*"-")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("PILIH MENU : "))
    print("\n")
    if menu == 1:
        snow_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Pilihan Anda Salah!")

if __name__ == "__main__":
    while(True):
        snow_menu()