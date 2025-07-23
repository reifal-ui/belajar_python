todos = []

def tambah():
    task = input("Tugas: ")
    todos.append({"task": task, "done": False})

def tampil():
    for i, t in enumerate(todos):
        status = "✓" if t["done"] else " "
        print(f"{i+1}. [{status}] {t['task']}")

def tandai():
    i = int(input("Nomor tugas yang sudah selesai: ")) - 1
    todos[i]["done"] = True

def run():
    while True:
        print("1. Tambah\n2. Tampil\n3. Tandai Selesai\n0. Keluar")
        p = input("Pilih: ")
        if p == "1": tambah()
        elif p == "2": tampil()
        elif p == "3": tandai()
        elif p == "0": break

run()
