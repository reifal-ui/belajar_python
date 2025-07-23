try:
    angka = int(input("Masukkan angka: "))
    print("Hasil:", angka * 2)
except ValueError:
    print("Itu bukan angka yang valid!")
finally:
    print("Terima kasih.")
