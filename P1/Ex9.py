from Seq1 import Seq

print("-----|Practice 1, Exercise 9|------")
FOLDER = "../SESSION-04/"
FILENAME = "U5.txt"
s = Seq()

s.read_fasta(FOLDER+FILENAME)

print(f"Sequence: (Length: {s.len()}) {s}\n"
      f"Bases: {s.count}\n"
      f"Rev:{s.reverse}\n"
      f"Comp:{s.complement}")
