from Seq1 import Seq

print("-----|Practice 1, Exercise 6|------")

# -- Creating a Null sequence
s1 = Seq()
# -- Creating a valid sequence
s2 = Seq("ACTGA")
# -- Creating an invalid sequence
s3 = Seq("Invalid sequence")

listS = [s1, s2, s3]

for number,s in enumerate(listS):
    print(f"Sequence {number}: (Length: {s.len()}) {s}"
          f"Bases: {s.count}")