from Seq0 import *

FOLDER = "../SESSION-04/"
U5 = "U5"
txt = ".txt"

seq = seq_read_fasta(FOLDER + U5 + txt)[0:20]
complement = seq_complement(seq)
print("------| Exercise 7 |------")
print("GENE U5\nFrag: ", seq, "\nComp: ", complement)
