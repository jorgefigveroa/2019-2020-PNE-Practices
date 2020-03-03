from Seq0 import *

FOLDER = "../SESSION-04/"
list1 = ["U5", "ADA", "FRAT1", "FXN"]
txt = ".txt"
bases = ["A", "C", "T", "G"]

print("-----| Exercise 4 |------\n")

for element in list1:
    seq = seq_read_fasta(FOLDER + element + txt)
    print("Gene: ", element)
    for letter in bases:
        print(letter, " :", seq_count_base(seq, letter))
    print("\n")
