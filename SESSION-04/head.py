from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

listcontents = file_contents.split("\n")

print("First line of the ", FILENAME, " file is: \n", listcontents[0])
