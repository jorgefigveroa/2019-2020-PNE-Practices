class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        if "A" and "C" and "T" and "G" in strbases:
            print("New sequence created!")
        else:
            print("ERROR!!")

    @property
    def __str__(self):
        a = self.strbases
        if "A" and "C" and "T" and "G" in a:
            return a
        else:
            return "ERROR"


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")