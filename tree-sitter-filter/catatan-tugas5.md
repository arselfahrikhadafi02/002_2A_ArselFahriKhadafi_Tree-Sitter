# Catatan Verifikasi Tugas 5

File yang digunakan:

- `queries/highlights.scm`
- `contoh.filter`
- `tree-sitter.json`

Perintah pengecekan:

```powershell
tree-sitter highlight contoh.filter
tree-sitter query queries/highlights.scm contoh.filter
```

Hasil query diverifikasi:

- keyword: `not`, `and`, `in`, `or`, `contains`
- operator: `=`, `>=`
- string: `"open"`, `"pending"`, `"closed"`, `"invoice"`
- number: `2`
- boolean: `true`
- property/nama field: `archived`, `status`, `priority`, `title`
