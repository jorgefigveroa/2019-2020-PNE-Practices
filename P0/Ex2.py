import Seq0

FOLDER = "../SESSION-04/"
FILENAME = "U5.txt"

body = Seq0.seq_read_fasta(FOLDER + FILENAME)[0:20]

print("DNA file:", FILENAME)
print("The first 20 DNA bases are:\n", body)
