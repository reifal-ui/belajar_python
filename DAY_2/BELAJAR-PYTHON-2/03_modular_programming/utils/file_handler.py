import json

def simpan_data(nama_file, mhs):
    data = {"nama": mhs.nama, "nim": mhs.nim}
    with open(nama_file, 'w') as file:
        json.dump(data, file)