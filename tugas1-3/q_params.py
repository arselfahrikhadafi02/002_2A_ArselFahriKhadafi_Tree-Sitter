import sys

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2], "r", encoding="utf-8").read()
tree = parser.parse(kode)

query = Query(PY, pola)
cursor = QueryCursor(query)

for _, cap in cursor.matches(tree.root_node):
    nama = cap["nama"][0].text.decode()
    params = cap.get("params", [])

    jumlah = params[0].named_child_count if params else 0
    print(nama, jumlah)