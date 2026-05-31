"""
Sanitizes HOI4 localisation files by removing duplicate
VICTORY_POINTS entries while keeping the first occurrence.

Usage:
    1. Place this script in your `mod/MODNAME/localisation/english` folder.
    2. Run the script inside Visual Studio Code.
        If you run the script locally, you will need to change the
        destination file location. This is marked with "CHANGE ME".
    3. Enter the complete path to the file you wish to read from.
    4. Open the resulting file.
        By default, this will be in the `localisation/english` folder.
        This file will be named "_SanitizedNames.txt"
    6. APPEND the file content to your existing file.
"""

import re

pattern_vic = re.compile(r"^ {2}([A-Z]{3}_VICTORY_POINTS_\d{3,6}):")
pattern_sta = re.compile(r"^ {2}([A-Z]{3}_STATE_\d{3,6}):")

seen = set[str]()
filtered_lines : list[str] = []

file = input("Paste the full path to the file:\n")
mode = input("Select the mode:\n(1) Victory Points (Default)\n(2) States\n")

with open(file, "r", encoding="utf-8-sig") as f:
    for line in f:
        if mode == "2":
            match = pattern_sta.match(line)
        else:
            match = pattern_vic.match(line)

        if match:
            key : str = match.group(1)

            if key not in seen:
                seen.add(key)
                filtered_lines.append(line)
            # else: Duplicate -> Skip
        
        else:
            filtered_lines.append(line)

with open("./localisation/english/_SanitizedNames.txt", "w", encoding="utf-8-sig") as resultfile:
    for line in filtered_lines:
        resultfile.write(line)