from models.mahasiswa import Mahasiswa
from utils.file_handler import simpan_data

mhs = Mahasiswa("Rei", "080903")
simpan_data("mahasiswa.json", mhs)