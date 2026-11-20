Ringkasan Tugas 2

Urutan penyelesaian:

1. Versi awal jelajah.py dibuat dan diuji pada kecil.py.
2. Traversal rekursif diisi menggunakan node.children dan named_children.
3. Hasil diuji pada t1.py dan t2-satu-fungsi.py.
4. Traversal dinaikkan pada t2-contoh100.py yang berisi 108 baris.
5. Baru setelah traversal rekursif berhasil, versi pengayaan ditambahkan memakai TreeCursor.

1. File jelajah.py
   Skrip menggunakan node.named_children dan enumerate pada node.children.
   Nama field diambil dengan node.field_name_for_child(i), sehingga hanya nama field
   yang benar-benar terkait dengan child pada indeks tersebut yang dicetak.

2. Pengujian kecil
   Perintah py tugas1-3/jelajah.py tugas1-3/kecil.py menghasilkan:
   module
     expression_statement
       assignment
         left: identifier
         right: integer

   Output sesuai pohon assignment yang diharapkan pada Tugas 1.

3. Pengujian file nyata
   File t2-contoh100.py berisi 108 baris. Skrip berhasil mencetak semua node bernama
   beserta indentasi, baris, kolom, dan nama field.

4. Pengayaan TreeCursor
   jelajah_cursor.py menggunakan tree.walk(), goto_first_child(),
   goto_next_sibling(), dan goto_parent().
   Output pada t2-contoh100.py dibandingkan dengan output versi rekursif.
   Kedua output identik, sehingga kedua versi menghasilkan traversal yang sama.

5. Pelaksanaan pengecekan
   - py -m py_compile berhasil untuk jelajah.py, jelajah_cursor.py, dan contoh100.py.
   - Output rekursif dan output TreeCursor disimpan masing-masing sebagai
     output-jelajah.txt dan output-jelajah-cursor.txt.
