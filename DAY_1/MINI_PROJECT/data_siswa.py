# Data Siswa menggunakan dictionary
mahasiswa = {
    'nama': '',
    'umur': 0,
    'jurusan': ''
}

# User input data
mahasiswa['nama'] = input("Masukkan nama mahasiswa: ")
mahasiswa['umur'] = int(input("Masukkan umur mahasiswa: "))
mahasiswa['jurusan'] = input("Masukkan jurusan mahasiswa: ")

# Menampilkan data mahasiswa
print("\nData Mahasiswa:")
print(f"Nama: {mahasiswa['nama']}")
print(f"Umur: {mahasiswa['umur']}")
print(f"Jurusan: {mahasiswa['jurusan']}")