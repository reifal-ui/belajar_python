class Orang:
    def __init__(self, nama):
        self.nama = nama

    def perkenalan(self):
        return f"Hallo, nama saya {self.nama}."
    
class Mahasiswa(Orang):
    def __init__(self, nama, jurusan):
        super().__init__(nama)
        self.jurusan = jurusan
    
    def perkenalan(self):
        return f"Hallo, nama saya {self.nama}, saya mahasiswa jurusan {self.jurusan}."

class Dosen(Orang):
    def __init__(self, nama, mata_kuliah):
        super().__init__(nama)
        self.mata_kuliah = mata_kuliah
    
    def perkenalan(self):
        return f"Hallo, nama saya {self.nama}, saya dosen mata kuliah {self.mata_kuliah}."
    
# Contoh penggunaan
mahasiswa = Mahasiswa("Budi", "Informatika")
dosen = Dosen("Ibu Siti", "Matematika")
print(mahasiswa.perkenalan())
print(dosen.perkenalan())

orang = Orang("Andi")
print(orang.perkenalan())