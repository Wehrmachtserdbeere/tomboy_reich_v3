"""
Gets the localized victory point name lines from the input file.

Usage:
    1. Place this script in your `mod/MODNAME/localisation/english` folder.
    2. Run the script inside Visual Studio Code.
        If you run the script locally, you will need to change the
        destination file location. This is marked with "CHANGE ME".
    3. Enter the complete path to the file you wish to read from.
    4. Enter the TAG you want to filter by.
        Entering "VICTORY" or "STATE" will give you all non-localised
        lines, depending on if you have input a victory point or a
        state name file.
        In other words, this filters out "GER", "ENG", etc lines.
    5. Open the resulting file.
        By default, this will be in the `localisation/english` folder.
        This file will be named "_LocalizedNames.txt"
    6. APPEND the file content to your existing file.
"""

filecontents = []

file = input("Paste the full path to the file:\n")

tag = input("Successfully read file. Please enter country tag:\n").upper()

result : list[str] = []

with open(file, "r", encoding="utf-8-sig") as f:
    for line in f:
        if line.startswith(" " + tag + "_"):
            result.append(line.rstrip("\n"))

# CHANGE ME
with open("./localisation/english/_LocalizedNames.txt", "w", encoding="utf-8-sig") as resultfile:
    for line in result:
        resultfile.write(" " + line + "\n")