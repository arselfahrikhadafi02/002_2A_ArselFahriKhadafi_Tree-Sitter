Catatan Verifikasi Tugas 3

File uji:
- tugas1-3/contoh.py
- Salah satu fungsi memiliki docstring sebagai pengayaan langkah 7.

Hitungan manual nama fungsi:
- tambah
- sapa
- Jumlah fungsi manual: 2

Hasil query fungsi:
- Query: fungsi.scm
- Perintah: py tugas1-3/q.py tugas1-3/contoh.py tugas1-3/fungsi.scm
- Hasil aktual: tambah pada baris 5 dan sapa pada baris 10.
- Hasil ini cocok dengan hitungan manual: 2 fungsi.

Hitungan manual parameter:
- tambah(a, b): 2 parameter
- sapa(nama): 1 parameter

Hasil query parameter:
- Query: params.scm
- Perintah: py tugas1-3/q_params.py tugas1-3/contoh.py tugas1-3/params.scm
- Hasil aktual:
  tambah 2
  sapa 1
- Hasil ini cocok dengan hitungan manual.

Hitungan manual pemanggilan print:
- print(nama) di dalam fungsi sapa
- print(tambah(1, 2)) di tingkat module
- Jumlah pemanggilan print manual: 2

Hasil query print:
- Query: print.scm
- Perintah: py tugas1-3/q.py tugas1-3/contoh.py tugas1-3/print.scm
- Hasil aktual menangkap dua identifier print pada baris 11 dan 14.
- Capture args masing-masing berisi (nama) dan (tambah(1, 2)).
- Jumlah pemanggilan dari query cocok dengan hitungan manual: 2.

Hitungan manual import:
- import os
- from pathlib import Path
- Modul os
- Modul pathlib
- Nama yang diimpor: Path

Hasil query import:
- Query: import.scm
- Perintah: py tugas1-3/q.py tugas1-3/contoh.py tugas1-3/import.scm
- Hasil aktual: os pada baris 1, pathlib pada baris 2, dan Path pada baris 2.
- Hasil ini cocok dengan hitungan manual.

Pengayaan docstring:
- Query: docstring.scm
- Perintah: py tugas1-3/q.py tugas1-3/contoh.py tugas1-3/docstring.scm
- Fungsi tambah memiliki string pertama pada block sebagai docstring.
- Hasil aktual pada baris 6: """Menambahkan dua angka."""

Kesalahan yang diperiksa:
- Tidak menebak nama node atau nama field.
- Nama tipe dan field diperoleh dari pohon atau jelajah.py.
- Query print membatasi identifier agar teksnya sama dengan "print".
- Query parameter memakai matches agar pasangan nama fungsi dan parameter tidak terpisah.
