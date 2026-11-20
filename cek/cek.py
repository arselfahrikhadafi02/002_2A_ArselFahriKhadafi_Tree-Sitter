import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor


PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNCTION = Query(
    PY,
    "(function_definition name: (identifier) @nama) @fungsi",
)


def body_lines(node):
    body = node.child_by_field_name("body")
    if body is None:
        return 0
    return body.end_point[0] - body.start_point[0] + 1


def first_error(node):
    if node.type == "ERROR" or node.is_missing:
        return node
    for child in node.children:
        error = first_error(child)
        if error is not None:
            return error
    return None


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    todo_nodes = (
        QueryCursor(Q_TODO).captures(tree.root_node).get("c", [])
    )
    for node in todo_nodes:
        print(
            f"{path}:{node.start_point[0] + 1}: "
            f"{node.text.decode(errors='replace').strip()}"
        )

    for _, captures in QueryCursor(Q_FUNCTION).matches(tree.root_node):
        nama = captures["nama"][0].text.decode(errors="replace")
        fungsi = captures["fungsi"][0]
        jumlah = body_lines(fungsi)
        if jumlah > 30:
            print(
                f"{path}:{fungsi.start_point[0] + 1}: "
                f"fungsi '{nama}' panjang ({jumlah} baris)"
            )

    if tree.root_node.has_error:
        error = first_error(tree.root_node)
        if error is not None:
            print(
                f"{path}:{error.start_point[0] + 1}: "
                f"{error.type}"
            )
        else:
            print(f"{path}: file memiliki error sintaks")


if len(sys.argv) != 2:
    print("Pemakaian: py cek/cek.py <folder>")
    raise SystemExit(1)

root = Path(sys.argv[1])
if not root.is_dir():
    print(f"Bukan folder: {root}")
    raise SystemExit(1)

skip = {".git", ".venv", "venv", "node_modules", "__pycache__"}

for path in root.rglob("*.py"):
    if any(part in skip for part in path.parts):
        continue
    cek_file(path)
