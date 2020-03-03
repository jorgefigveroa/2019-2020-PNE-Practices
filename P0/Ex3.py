from Seq0 import *

FOLDER = "../SESSION-04/"
list1 = ["U5", "ADA", "FRAT1", "FXN"]
txt = ".txt"

print("-----| Exercise 3 |------")

for element in list1:
    seq = seq_read_fasta(FOLDER + element + txt)
    length = seq_len(seq)
    print("Gene", element, " ---> Length:", length)
