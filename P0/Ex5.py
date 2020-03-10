from Seq0 import *

FOLDER = "../SESSION-04/"
list1 = ["U5", "ADA", "FRAT1", "FXN"]
txt = ".txt"

print("-----| Exercise 4 |------\n")

for element in list1:
    seq = seq_read_fasta(FOLDER + element + txt)
    print("Gene: ", element, count(seq))
