import csv
from tabulate import tabulate

data_inventaris = {}

def tambah_barang(nama, jumlah):
    data_inventaris[nama] = data_inventaris.get(nama, 0) + jumlah
    print(f"{jumlah} {nama} ditambahkan.")

def hapus_barang(nama):
    if nama in data_inventaris:
        del data_inventaris[nama]
        print(f"{nama} dihapus dari inventaris.")
    else:
        print("Barang tidak ditemukan.")

def lihat_barang():
    if data_inventaris:
        print("\nInventaris Barang:")
        data = [(barang, jumlah) for barang, jumlah in data_inventaris.items()]
        print(tabulate(data, headers=["Barang", "Jumlah"], tablefmt="grid"))
    else:
        print("Inventaris kosong.")

def simpan_data(filename="inventaris.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Barang", "Jumlah"])
        writer.writerows(data_inventaris.items())
    print("Data inventaris disimpan.")

def muat_data(filename="inventaris.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data_inventaris[row[0]] = int(row[1])
    except FileNotFoundError:
        pass

muat_data()
while True:
    print("\n=== Inventaris Barang ===")
    print("1. Tambah Barang")
    print("2. Lihat Inventaris")
    print("3. Hapus Barang")
    print("4. Simpan & Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nama = input("Nama barang: ")
        jumlah = int(input("Jumlah: "))
        tambah_barang(nama, jumlah)
    elif pilihan == "2":
        lihat_barang()
    elif pilihan == "3":
        nama = input("Nama barang yang ingin dihapus: ")
        hapus_barang(nama)
    elif pilihan == "4":
        simpan_data()
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
