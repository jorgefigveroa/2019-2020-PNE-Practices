from typing import List

from Seq1 import Seq

print("-----|Practice 1, Exercise 5|------")

# -- Creating a Null sequence
s1 = Seq()
# -- Creating a valid sequence
s2 = Seq("ACTGA")
# -- Creating an invalid sequence
s3 = Seq("Invalid sequence")

listS: List[Seq] = [s1, s2, s3]

for number, s in enumerate(listS):
    print(f"Sequence {number}: (Length: {s.len()}) {s}")
    for base in ["A", "C", "T", "G"]:
        print(f"{base}: {s.count_base(base)}", end=", ")
    print()
