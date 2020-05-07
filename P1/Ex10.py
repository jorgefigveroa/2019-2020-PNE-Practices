from Seq1 import Seq

print("-----|Practice 1, Exercise 10|------")
FOLDER = "../SESSION-04/"
list1 = ["U5", "ADA", "FRAT1", "FXN"]
txt = ".txt"


def maximumkey(d):
    value = list(d.values())
    keys = list(d.keys())
    return keys[value.index(max(value))]


for element in list1:
    s = Seq()
    s.read_fasta(FOLDER + element + txt)
    dictionary = s.count
    print(f"Gene {element}: Most frequent Base:{maximumkey(dictionary)}")
