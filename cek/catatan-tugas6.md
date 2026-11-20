# Catatan Verifikasi Tugas 6

## Pengujian pada folder uji

Perintah:

```powershell
py cek/cek.py cek/uji
```

Hasil yang diverifikasi pada file buatan sendiri:

- `todo.py`: menemukan 2 komentar, yaitu `TODO` pada baris 1 dan `FIXME` pada baris 2.
- `fungsi_panjang.py`: menemukan `fungsi_panjang` pada baris 1 dengan body 32 baris.
- `sintaks_rusak.py`: menemukan node `ERROR` pada baris 2.

Output lengkap disimpan di `cek/output-uji.txt`.

## Pengujian pada repositori

Perintah:

```powershell
py cek/cek.py .
```

Output disimpan di `cek/output-repo.txt`. Jalur repository merupakan basis
pengujian nyata yang tersedia saat pengerjaan Tugas 6.

## Pengecekan manual dua file

- `cek/uji/todo.py`: jumlah komentar TODO/FIXME manual adalah 2 dan hasil CLI
  juga melaporkan 2 komentar.
- `cek/uji/fungsi_panjang.py`: fungsi memiliki body sepanjang 32 baris dan CLI
  melaporkan fungsi tersebut sebagai fungsi panjang.
- `cek/uji/sintaks_rusak.py`: sintaks yang tidak lengkap menghasilkan `ERROR`
  pada baris 2 dan cocok dengan pengecekan pohon.
