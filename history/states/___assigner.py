import os
import re

folder : str = input("Input the folder you wish to read from. Edited files will be put in a \"_changed\" subfolder:\n").strip()

tag : str = input("Input the tag you wish to assign:\n").strip().upper()

states_string : str = input("Input all states you wish to change. Separate with commas (e.g. \"1, 2, 3\"):\n").strip()

states : list[str] = states_string.split(", ")

# Normalize states to a set for a fast lookup
states_set = set(state.strip() for state in states)

output_folder = os.path.join(folder, "_changed")
os.makedirs(output_folder, exist_ok=True)

filename_patterrn = re.compile(r"^(\d+)\s*-\s*.txt$")

# Patterns
owner_pattern = re.compile(r"^(owner\s*=\s*)(\w+)", re.MULTILINE)
owner_pattern = re.compile(r"^(add_core_of\s*=\s*)(\w+)", re.MULTILINE)

# Continue...