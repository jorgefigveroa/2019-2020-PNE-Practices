from Seq0 import *

FOLDER = "../SESSION-04/"
U5 = "U5"
txt = ".txt"

seq = seq_read_fasta(FOLDER + U5 + txt)  # type: object
reverse = seq_reverse(seq)
print("------| Exercise 6 |------")
print("GENE U5\nFrag: ", seq[0:20], "\nRev : ", reverse[0:20])
