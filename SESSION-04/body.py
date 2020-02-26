from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

listcontents = file_contents.split("\n")

del listcontents[0]

for element in listcontents:
    print(element)
