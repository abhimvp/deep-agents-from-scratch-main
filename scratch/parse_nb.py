import json
import os
import sys

# Set standard output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

nb_path = os.path.join("notebooks", "1_todo.ipynb")
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

output_path = os.path.join("scratch", "parsed_nb.txt")
with open(output_path, "w", encoding="utf-8") as out:
    for idx, cell in enumerate(nb["cells"]):
        cell_type = cell["cell_type"]
        source = "".join(cell["source"])
        out.write(f"=== Cell {idx} ({cell_type}) ===\n")
        if cell_type == "code":
            out.write(source)
        else:
            lines = source.splitlines()
            out.write("\n".join(lines[:15]))
        out.write("\n" + "="*40 + "\n\n")

print("Parsed notebook written to scratch/parsed_nb.txt")
