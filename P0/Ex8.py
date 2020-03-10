from Seq0 import count, seq_read_fasta

print("-----| Exercise 8 |------")

FOLDER = "../SESSION-04/"
list1 = ["U5", "ADA", "FRAT1", "FXN"]
txt = ".txt"


def maximumkey(d):
    value = list(d.values())
    keys = list(d.keys())
    return keys[value.index(max(value))]


for element in list1:
    seq = seq_read_fasta(FOLDER + element + txt)
    dictionary = count(seq)
    print("Gene ", element, ": Most frequent Base: ", maximumkey(dictionary))
