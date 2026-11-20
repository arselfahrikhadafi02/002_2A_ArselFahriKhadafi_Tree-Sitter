# Pendeteksi TODO, Fungsi Panjang, dan Error Python

CLI ini menggunakan Tree-sitter untuk memeriksa file Python.

## Instalasi

```powershell
py -m pip install tree-sitter tree-sitter-python
```

## Menjalankan

```powershell
py cek/cek.py <folder>
```

Contoh:

```powershell
py cek/cek.py cek/uji
```

Fitur yang dilaporkan:

1. Komentar yang berisi `TODO` atau `FIXME`.
2. Fungsi yang body-nya lebih dari 30 baris.
3. File yang memiliki node `ERROR` atau `MISSING` pada pohon sintaks.

Folder `venv/`, `.venv/`, `.git/`, `node_modules/`, dan `__pycache__/` dilewati.
