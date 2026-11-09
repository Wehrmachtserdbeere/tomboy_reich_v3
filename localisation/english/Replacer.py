# Replaces INPUT_FILE entries within TARGET_FILE while keeping the rest untouched.

import re
import shutil
from pathlib import Path

# Ask for file paths
INPUT_FILE = Path(input("INPUT_FILE: ").strip().strip('"'))
TARGET_FILE = Path(input("TARGET_FILE: ").strip().strip('"'))

# Matches YAML keys such as ANI_STATE_357:
KEY_PATTERN = re.compile(r"^[ \t]*([A-Za-z0-9_]+)[ \t]*:")


def split_line(line):
    """Separate a line's content from its newline character."""
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    elif line.endswith("\n") or line.endswith("\r"):
        return line[:-1], line[-1]
    return line, ""


# Check that both files exist
if not INPUT_FILE.is_file():
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

if not TARGET_FILE.is_file():
    raise FileNotFoundError(f"Target file not found: {TARGET_FILE}")


# Read replacement entries
replacements = {}

with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
    for line in file:
        content, _ = split_line(line)
        match = KEY_PATTERN.match(content)

        if match:
            replacements[match.group(1)] = content


# Read target file
with TARGET_FILE.open("r", encoding="utf-8", newline="") as file:
    target_lines = file.readlines()


# Replace matching entries
new_lines = []
matched_keys = set()

for line in target_lines:
    content, newline = split_line(line)
    match = KEY_PATTERN.match(content)

    if match and match.group(1) in replacements:
        key = match.group(1)

        # Preserve target file indentation
        indentation = re.match(r"[ \t]*", content).group()

        new_content = indentation + replacements[key].lstrip(" \t")
        new_lines.append(new_content + newline)

        matched_keys.add(key)
    else:
        new_lines.append(line)


# Create backup
backup_file = TARGET_FILE.with_name(TARGET_FILE.name + ".bak")
shutil.copy2(TARGET_FILE, backup_file)


# Write modified target file
with TARGET_FILE.open("w", encoding="utf-8", newline="") as file:
    file.writelines(new_lines)


# Report results
print(f"\nReplaced {len(matched_keys)} entries.")

missing_keys = set(replacements) - matched_keys

if missing_keys:
    print("\nThese input keys were not found in the target file:")
    for key in sorted(missing_keys):
        print(f"  {key}")

print(f"\nBackup created: {backup_file}")
print("Done!")