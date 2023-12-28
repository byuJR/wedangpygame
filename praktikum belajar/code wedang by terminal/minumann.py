# minumann.py

class Minuman:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def detail_pilihan(self, banyak_minuman):
        print("=======================================")
        print(f"Minuman yang dibeli : {self.nama}")
        print(f"Harga              : Rp {self.harga}")
        total_harga = round(self.harga * banyak_minuman)
        print(f"Banyak minuman     : {banyak_minuman} gelas")
        print(f"Total harga        : Rp {total_harga}")
        print("================================================")
        return total_harga

# Fungsi input_banyak_minuman bisa juga dimasukkan ke sini jika diinginkan
def input_banyak_minuman():
    while True:
        try:
            return int(input("Banyak minuman (gelas): "))
        except ValueError:
            print("Masukkan angka")
