class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Tambah node di akhir
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Hapus node awal
    def delete_front(self):
        if self.head is None:
            print("List kosong.")
            return
        print(f"Menghapus node awal: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Hapus node akhir
    def delete_end(self):
        if self.head is None:
            print("List kosong.")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        print(f"Menghapus node akhir: {curr.data}")
        if curr.prev:
            curr.prev.next = None
        else:
            self.head = None

    # Hapus node berdasarkan nilai
    def delete_by_value(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                print(f"Menghapus node dengan nilai: {value}")
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next
        print(f"Data {value} tidak ditemukan.")

    # Cetak semua data
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Linked List Awal:")
dll.display()

dll.delete_front()
dll.display()

dll.delete_end()
dll.display()

dll.delete_by_value(20)
dll.display()
