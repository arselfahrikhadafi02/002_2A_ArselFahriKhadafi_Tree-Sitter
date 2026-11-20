import tree_sitter_python as tspython
from tree_sitter import Language, Parser


parser = Parser(Language(tspython.language()))

potongan = {
    "fungsi": b"def sapa(nama):\n    return nama\n",
    "if_else": b"x = 10\nif x > 5:\n    print(\"besar\")\nelse:\n    print(\"kecil\")\n",
    "kelas": b"class Orang:\n    def sapa(self):\n        return \"halo\"\n",
}


def cetak_anonymous(node):
    for child in node.children:
        if not child.is_named:
            print(child.type, "anonim")
        cetak_anonymous(child)


def cari_error(node):
    if node.type == "ERROR" or node.is_missing:
        print(
            f"  {node.type} "
            f"[{node.start_point[0] + 1}:{node.start_point[1]}]"
        )
    for child in node.children:
        cari_error(child)


for nama, kode in potongan.items():
    print(f"\n=== {nama} ===")
    tree = parser.parse(kode)
    print(tree.root_node)

print("\n=== node anonim pada fungsi ===")
tree_fungsi = parser.parse(potongan["fungsi"])
cetak_anonymous(tree_fungsi.root_node)

print("\n=== perbedaan children dan named_children ===")
function_node = tree_fungsi.root_node.children[0]
print("function_definition.children:")
for child in function_node.children:
    print(f"  {child.type}: {'bernama' if child.is_named else 'anonim'}")
print("function_definition.named_children:")
for child in function_node.named_children:
    print(f"  {child.type}: bernama")

print("\n=== hasil rusak: fungsi tanpa titik dua ===")
kode_rusak = b"def sapa(nama)\n    return nama\n"
tree_rusak = parser.parse(kode_rusak)
print(tree_rusak.root_node)
cari_error(tree_rusak.root_node)
