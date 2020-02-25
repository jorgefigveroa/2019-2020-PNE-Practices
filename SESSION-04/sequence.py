from pathlib import Path

FILENAME = "ADA.txt"

file_contents = Path(FILENAME).read_text()

file = file_contents.split("\n")
del file[0]

new_file = file

total_length = 0
for element in new_file:
    length = len(element)
    total_length = total_length + length

print("The total length of", FILENAME, "is: ", total_length)
