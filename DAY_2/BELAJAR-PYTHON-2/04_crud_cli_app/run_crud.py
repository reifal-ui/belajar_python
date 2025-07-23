from mahasiswa import Mahasiswa

data = []

def tambah():
    nama = input("Masukan Nama: ")
    nim = input("Masukan NIM: ")
    data.append(Mahasiswa(nama, nim))

def tampilkan():
    for m in data:
        print(f"Nama: {m.nama}, NIM: {m.nim}")

def hapus():
    nim = input("Masukan NIM yang ingin dihapus: ")
    global data
    data = [m for m in data if m.nim != nim]

def run():
    while True:
        print("1. Tambah\n2. Tampil\n3. Hapus\n0. Keluar")
        p = input("Pilih: ")
        if p == "1": tambah()
        elif p == "2": tampilkan()
        elif p == "3": hapus()
        elif p == "0": break

run ()