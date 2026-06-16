import re

output_path = "Loc_Orderer_Output.txt"

input_file = input("Please put the full path to the loc file you wish to have ordered:\n")

def split_key(key: str):
    m = re.match(r"^(.*?)(\d+)?$", key)
    if not m:
        raise Exception(f"### ERROR ### - No pattern found in {key}!")
    prefix = m.group(1)
    number = int(m.group(2)) if m.group(2) else -1
    return prefix, number

def sort_yml_file(input_path : str):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].rstrip("\n")
    entries = []

    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue

        key, value = stripped.split(":", 1)
        entries.append((key.strip(), value))

    entries.sort(key=lambda kv: split_key(kv[0]))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for key, value in entries:
            f.write(f"  {key}:{value}\n")

sort_yml_file(input_file)