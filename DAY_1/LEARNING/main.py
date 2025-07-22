# Variable dan Tipe data
Nama = "Reifal" # Ini adalah String
Umur = 17 # Ini adalah Integer
Tinggi = 170.5 # Ini adalah Float
is_student = True # Ini adalah Boolean

# Operator
a = 10
b = 5

print(a+b) # Penjumlahan
print(a-b) # Pengurangan
print(a*b) # Perkalian
print(a/b) # Pembagian

# Input dan Output
nama = input("Masukkan nama Anda: ")
print("Halo, " + nama + "! Selamat datang di program Python.")

# Kondisi
Umur = int(input("Masukkan umur Anda: "))
if Umur >= 18:
    print("Anda sudah dewasa.")
else:
    print("Anda masih di bawah umur.")

# Perulangan
for i in range(5):
    print(f"Perulangan ke-{i+1}")

# Fungsi
def salam(nama):
    """Menerima parameter nama dan mencetak sapaan"""
    return f"Halo, {nama}!"

print(salam("Reifal"))

# List
buah = ["Apel", "Jeruk", "Pisang"]
print(buah[0])  # Mengakses elemen pertama

# Tuple
koordinat = (10, 20)
print(koordinat[1])

# Dictionary
data = {"nama": "Reifal", "umur": 20}
print(data["nama"])
