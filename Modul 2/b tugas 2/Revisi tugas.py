# Kelas Node untuk menyimpan data dan referensi ke node sebelumnya dan sesudahnya
class Node:
    def __init__(self, data):              # Konstruktor Node menerima satu parameter: data
        self.data = data                   # Menyimpan nilai data
        self.prev = None                   # Pointer ke node sebelumnya (awalnya None)
        self.next = None                   # Pointer ke node berikutnya (awalnya None)

# Kelas DoubleLinkedList untuk mengelola daftar berantai ganda
class DoubleLinkedList:
    def __init__(self):                    # Konstruktor DoubleLinkedList
        self.head = None                   # Pointer ke node pertama dalam list

    def append(self, data):                # Menambahkan node baru di akhir list
        new_node = Node(data)              # Membuat node baru dengan data
        if self.head is None:              # Jika list kosong
            self.head = new_node           # Node baru menjadi head
            return
        curr = self.head                   # Mulai dari head
        while curr.next:                   # Telusuri sampai ke node terakhir
            curr = curr.next
        curr.next = new_node               # Node terakhir menunjuk ke node baru
        new_node.prev = curr               # Node baru menunjuk ke node sebelumnya

    def delete_front(self):                # Menghapus node pertama
        if self.head is None:              # Jika list kosong
            print("List kosong.")
            return
        print(f"Menghapus node awal: {self.head.data}")  # Menampilkan data yang dihapus
        self.head = self.head.next         # Head dipindahkan ke node berikutnya
        if self.head:                      # Jika list tidak kosong setelah penghapusan
            self.head.prev = None          # Node pertama baru tidak punya node sebelumnya

    def delete_end(self):                  # Menghapus node terakhir
        if self.head is None:              # Jika list kosong
            print("List kosong.")
            return
        curr = self.head                   # Mulai dari head
        while curr.next:                   # Telusuri sampai node terakhir
            curr = curr.next
        print(f"Menghapus node akhir: {curr.data}")  # Menampilkan data yang dihapus
        if curr.prev:                      # Jika ada node sebelum node terakhir
            curr.prev.next = None          # Putuskan hubungan dengan node terakhir
        else:
            self.head = None               # Jika hanya ada satu node, kosongkan list

    def delete_by_value(self, value):      # Menghapus node berdasarkan nilai
        curr = self.head                   # Mulai dari head
        while curr:                        # Telusuri node satu per satu
            if curr.data == value:         # Jika nilai ditemukan
                print(f"Menghapus node dengan nilai: {value}")
                if curr.prev:              # Jika node bukan di awal
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # Jika node di awal, geser head
                if curr.next:              # Jika node bukan di akhir
                    curr.next.prev = curr.prev
                return                     # Keluar setelah penghapusan
            curr = curr.next               # Lanjut ke node berikutnya
        print(f"Data {value} tidak ditemukan.")  # Jika nilai tidak ditemukan

    def display(self):                     # Menampilkan seluruh isi list
        curr = self.head                   # Mulai dari head
        while curr:                        # Telusuri semua node
            print(curr.data, end=" <-> ")  # Cetak data dengan panah penghubung
            curr = curr.next
        print("None")                      # Akhir dari list

# ------------------ Contoh Penggunaan ------------------
dll = DoubleLinkedList()                   # Membuat instance DoubleLinkedList
dll.append(10)                             # Tambahkan 10
dll.append(20)                             # Tambahkan 20
dll.append(30)                             # Tambahkan 30
dll.append(40)                             # Tambahkan 40

print("Linked List Awal:")
dll.display()                              # Tampilkan list awal

dll.delete_front()                         # Hapus node pertama (10)
dll.display()                              # Tampilkan list

dll.delete_end()                           # Hapus node terakhir (40)
dll.display()                              # Tampilkan list

dll.delete_by_value(20)                    # Hapus node dengan nilai 20
dll.display()                              # Tampilkan list akhir
