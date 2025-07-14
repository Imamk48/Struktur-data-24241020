# Input data customer dan tanggal disimpan dalam tuple
data_customer = (
    input("Masukkan nama customer: "),
    input("Masukkan tanggal belanja (DD-MM-YYYY): ")
)

jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

# List untuk menyimpan data belanja
daftar_belanja = []

# Input data barang
for i in range(jumlah_barang):
    print(f"\nData Barang ke-{i+1}")
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga satuan: "))
    qty = int(input("Masukkan jumlah beli: "))
    subtotal = harga * qty
    daftar_belanja.append((nama_barang, harga, qty, subtotal))

# Tampilkan hasil belanja
print("\n=== STRUK BELANJA ===")
print(f"Nama Customer : {data_customer[0]}")
print(f"Tanggal       : {data_customer[1]}")
print("\nDaftar Belanja:")

total = 0
for i, (nama, harga, qty, subtotal) in enumerate(daftar_belanja, 1):
    print(f"{i}. {nama} - {qty} x {harga} = {subtotal}")
    total += subtotal

print(f"\nTotal Bayar   : {total}")
