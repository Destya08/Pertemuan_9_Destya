class Imunisasi:
    banyak_antrian = 0

    def __init__(self, nama, umur):
        self._nama = nama
        self.umur = umur
        Imunisasi.banyak_antrian += 1

    def tampilkan_data(self):
        print("Nama balita :", self.nama)
        print("Umur balita :", self.umur)

    @staticmethod 
    def syarat():
        print("Syarat Umur Imunisasi Balita 0 hingga 24 bulan")

    @property
    def nama(self):
        return self._nama

    @classmethod
    def antrian_imunisasi(cls):
        print("Banyaknya Antrian Imunisasi Adalah", cls.banyak_antrian)

blt1 = Imunisasi("Clara", 11)
blt2 = Imunisasi("Mima", 20)
blt3 = Imunisasi("Dom", 15)

Imunisasi.syarat()
Imunisasi.antrian_imunisasi()

blt1.tampilkan_data()
blt2.tampilkan_data()
blt3.tampilkan_data()
