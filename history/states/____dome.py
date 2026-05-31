# C:\\Users\\Strawb\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\tomboy_reich_v3\\history\\states

import os

folder_path = "C:\\Users\\Strawb\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\tomboy_reich_v3\\history\\states"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        changed = False

        skip_block = False
        brace_depth = 0

        for line in lines:
            stripped = line.strip()

            # --- START skipping IF block ---
            if not skip_block and stripped.startswith("IF ="):
                skip_block = True
                brace_depth = line.count("{") - line.count("}")
                changed = True
                continue

            if skip_block:
                brace_depth += line.count("{") - line.count("}")
                if brace_depth <= 0:
                    skip_block = False
                continue
            # --- END skipping IF block ---

            # Your existing replacements
            if stripped.startswith("owner ="):
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(f"{indent}owner = ANI\n")
                changed = True

            elif stripped.startswith("add_core_of ="):
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(f"{indent}add_core_of = ANI\n")
                changed = True
            
            elif stripped.startswith("controller ="):
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(f"{indent}controller = ANI\n")
                changed = True

            else:
                new_lines.append(line)

        if changed:
            print(f"Modified: {filename}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

print("Done.")