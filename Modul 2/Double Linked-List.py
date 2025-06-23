# Praktek 29 : Membuat Double Linked-List di Awal
# membuat node baru
def buat_node_double(data):
    return {'data': data, 'prev': head, 'next': None}

# Menambahkan node baru di awal double linked-list
def tambah_node_depan(head, data):
    new_node = buat_node_double(data)
    new_node['next'] = head
    new_node['prev'] = None
    
    if head is not None:
        head['prev'] = new_node
        
    return new_node

# Mencetak double linked-list dengan traversal maju
def cetak_dll(head):
    current = head
    print('HEAD', end=' <-> ')
    while current:
        print(current['data'], end=' <-> ')
        current = current['next']
    print('NULL')
    
# Penerapannya 
# Head awal dari linked-list
head = None

# Tambah Node
head = tambah_node_depan(head, 16) # 16
head = tambah_node_depan(head, 19) # 16 <-> 19

# Cetak double linked-list sebelum penyisipan di awal node
print("Double Linked-list Awal Sebelum Penyisipan : \n", end='')
cetak_dll(head)

# Tambah Node didepan double linked-list
head = tambah_node_depan(head, 22) # 16 <-> 19 <-> 22
head = tambah_node_depan(head, 99) # 16 <-> 19 <-> 22 <-> 99

# Cetak double linked-list setelah penyisipan di awal node
print("\nDouble Linked-list Awal Setelah Penyisipan: \n", end='')
cetak_dll(head)


# Praktek 30 : Membuat Double Linked-List di Akhir
# membuat node baru
def buat_node_double(data):
    return {'data': data, 'prev': head, 'next': None}

# Menambahkan node baru di akhir double linked-list
def tambah_node_akhir(head, data):
    new_node = buat_node_double(data)

    # Jika list kosong
    if head is None:
        return new_node

    # Jika list tidak kosong, cari node terakhir
    current = head
    while current['next'] is not None:
        current = current['next']

    # Sambungkan node terakhir ke node baru
    current['next'] = new_node
    new_node['prev'] = current

    return head


# Mencetak double linked-list dengan traversal maju
def cetak_dll(head):
    current = head
    print('HEAD', end=' <-> ')
    while current:
        print(current['data'], end=' <-> ')
        current = current['next']
    print('NULL')
    
# Penerapannya 
# Head awal dari linked-list
head = None

# Tambah Node
head = tambah_node_depan(head, 16) # 16
head = tambah_node_depan(head, 19) # 19 <-> 16

# Cetak double linked-list sebelum penyisipan di akhir node
print("Double Linked-list Sebelum Penyisipan diakhir: \n", end='')
cetak_dll(head)

# Tambah Node diakhir double linked-list
head = tambah_node_akhir(head, 22) # 19 <-> 16 <-> 22 
head = tambah_node_akhir(head, 99) # 19 <-> 16 <-> 22  <-> 19 

# Cetak double linked-list setelah penyisipan di akhir node
print("\nDouble Linked-list Setelah Penyisipan diakhir: \n", end='')
cetak_dll(head)


# Praktek 31 : Menyisipakan Node Baru di Tengah Double Linked-list
# membuat node baru
def buat_node_double(data):
    return {'data': data, 'prev': head, 'next': None}

# Menambahkan node baru di awal double linked-list
def tambah_node_depan(head, data):
    new_node = buat_node_double(data)
    new_node['next'] = head
    new_node['prev'] = None
    
    if head is not None:
        head['prev'] = new_node
        
    return new_node

# sisip node diposisi mana saja
def sisip_double_dimana_aja(head, data, position):
    # membuat node baru
    new_node = buat_node_double(data)
    
    # cek jika posisi = 0 gunakan fungsi tambah_node_depan()
    if position == 0:
        return tambah_node_depan(head, data)
    
    # cek jika posisi < 0, input tidak valid
    if position < 0:
        print('\nPosisi Tidak Valid')
        return head
    
    # deklarasi node pertama
    current = head
    index = 1
    
    # traversal menuju posisi yang diinginkan dan bukan posisi 0
    while current is not None and index < position - 1:
        current = current['next']
        index += 1
        
    # validasi posisi
    if current is None:
        print("Posisi melebihi panjang linked list!")
        return head
    
    # sisipkan node diantara current dan current.next
    next_node = current['next']
    current['next'] = new_node
    new_node['prev'] = current
    new_node['next'] = next_node
    if next_node is not None:
        next_node['prev'] = new_node
        
        
    return head

# Mencetak double linked-list dengan traversal maju
def cetak_dll(head):
    current = head
    print('HEAD', end=' <-> ')
    while current:
        print(current['data'], end=' <-> ')
        current = current['next']
    print('NULL')
    
# Penerapannya 
# Head awal dari linked-list
head = None

# Tambah Node
head = tambah_node_depan(head, 16) # 16
head = tambah_node_depan(head, 19) # 16 <-> 19

# Cetak double linked-list sebelum penyisipan di awal node
print("Double Linked-list Awal Sebelum Penyisipan Tengah: \n", end='')
cetak_dll(head)

# Tambah Node pada posisi mana saja, di double linked-list
head = sisip_double_dimana_aja(head, 22, 1) # 19 <-> 22 <-> 16
head = sisip_double_dimana_aja(head, 10, 2) # 19 <-> 10 <-> 22 <-> 16
head = sisip_double_dimana_aja(head, 30, 3) # 9 <-> 10 <-> 30 <-> 22 <-> 16

# Cetak double linked-list setelah penyisipan di awal node
print("\nDouble Linked-list Awal Setelah Penyisipan Tengah: \n", end='')
cetak_dll(head)