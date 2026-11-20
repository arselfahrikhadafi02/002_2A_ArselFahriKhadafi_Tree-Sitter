import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser


parser = Parser(Language(tspython.language()))


def jelajah(cursor, kedalaman=0, field=None):
    node = cursor.node

    if node.is_named:
        baris, kolom = node.start_point
        label = f"{field}: " if field else ""
        print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")
        child_kedalaman = kedalaman + 1
    else:
        child_kedalaman = kedalaman

    if cursor.goto_first_child():
        while True:
            jelajah(cursor, child_kedalaman, cursor.field_name)
            if not cursor.goto_next_sibling():
                break
        cursor.goto_parent()


if len(sys.argv) != 2:
    print("Pemakaian: py jelajah_cursor.py <file.py>")
    raise SystemExit(1)

with open(sys.argv[1], "rb") as f:
    tree = parser.parse(f.read())

jelajah(tree.walk())
