# Fungsi untuk penjumlahan
def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk perkalian
def kali(a, b):
    return a * b

# Fungsi untuk pembagian
def bagi (a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

# Fungsi utama untuk kalkulator
print("Selamat datang di Kalkulator Sederhana!")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    hasil = tambah(angka1, angka2)
elif pilihan == '2':
    hasil = kurang(angka1, angka2)
elif pilihan == '3':
    hasil = kali(angka1, angka2)
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
else:
    hasil = "Pilihan tidak valid."

print(f"Hasil: {hasil}")