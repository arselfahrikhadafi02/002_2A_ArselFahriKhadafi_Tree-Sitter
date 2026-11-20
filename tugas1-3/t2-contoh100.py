produk = []


def tambah_produk(nama, harga):
    produk.append({"nama": nama, "harga": harga})
    return len(produk)


def cari_produk(nama):
    for item in produk:
        if item["nama"] == nama:
            return item
    return None


def hapus_produk(nama):
    for i, item in enumerate(produk):
        if item["nama"] == nama:
            del produk[i]
            return True
    return False


def total_harga():
    total = 0
    for item in produk:
        total = total + item["harga"]
    return total


def cetak_produk():
    if not produk:
        print("Daftar kosong")
        return

    for item in produk:
        print(item["nama"], item["harga"])


def cek_stok(nama):
    item = cari_produk(nama)
    if item is None:
        return False
    return item["harga"] > 0


def ringkas_produk():
    ringkasan = {}
    for item in produk:
        nama = item["nama"]
        ringkasan[nama] = ringkasan.get(nama, 0) + item["harga"]
    return ringkasan


def diskon_harga(harga, persen):
    if persen < 0:
        return harga
    if persen > 100:
        return 0
    potongan = harga * persen / 100
    return harga - potongan


class Kasir:
    def __init__(self, cabang):
        self.cabang = cabang
        self.transaksi = []

    def jual(self, nama, jumlah):
        item = cari_produk(nama)
        if item is None:
            return None
        return {
            "nama": nama,
            "jumlah": jumlah,
            "total": item["harga"] * jumlah,
            "cabang": self.cabang,
        }

    def catat(self, transaksi):
        if transaksi is not None:
            self.transaksi.append(transaksi)
            return True
        return False

    def laporan(self):
        return len(self.transaksi)

    def hitung_total(self):
        total = 0
        for transaksi in self.transaksi:
            if "total" in transaksi:
                total = total + transaksi["total"]
        return total

    def cetak_laporan(self):
        print("Cabang:", self.cabang)
        print("Jumlah transaksi:", self.laporan())
        print("Total nilai:", self.hitung_total())


tambah_produk("Tiket", 50000)
tambah_produk("Voucher", 25000)

kasir = Kasir("Pusat")
pesanan = kasir.jual("Tiket", 2)
kasir.catat(pesanan)
cetak_produk()
