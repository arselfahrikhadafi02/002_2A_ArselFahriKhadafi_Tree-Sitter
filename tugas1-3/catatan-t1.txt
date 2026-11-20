Ringkasan Tugas 1

1. Perbandingan prediksi dan hasil
   - Pohon fungsi sesuai prediksi secara utama: module -> function_definition -> identifier,
     parameters -> identifier, dan block -> return_statement -> identifier.
   - Pohon if/else lebih spesifik daripada prediksi. Operator perbandingan terbentuk sebagai
     node comparison_operator dengan dua child: identifier dan integer.
   - String pada call dan return_statement memiliki node bernama string beserta anak-anak
     anonim string_start, string_content, dan string_end.
   - Pohon kelas sesuai prediksi secara utama: class_definition -> block ->
     function_definition -> parameters -> block -> return_statement.

2. Node bernama dan anonim
   Node bernama berasal dari rule grammar, misalnya module, function_definition,
   identifier, parameters, block, dan return_statement.
   Contoh node anonim pada fungsi sapa adalah def, (, ), :, dan return.

3. children dan named_children
   children mencakup seluruh child, termasuk node anonim. Sebagai contoh,
   function_definition memiliki nama, parameters, :, dan body. named_children hanya
   berisi node bernama: identifier, parameters, dan block.

4. Kasus kode rusak
   Kode def sapa(nama) tanpa titik dua menghasilkan module dengan node ERROR.
   Ini membuktikan bahwa parser tetap menghasilkan pohon dan menandai bagian yang
   tidak sesuai grammar sebagai node ERROR.
