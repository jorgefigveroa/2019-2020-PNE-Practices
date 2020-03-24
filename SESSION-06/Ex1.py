class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        bases = ["A", "C", "T", "G"]
        for b in strbases:
            if b not in bases:
                print("ERROR!!")
                self.strbases = "ERROR"
                return
        print("New sequence created!")
        self.strbases = strbases

    def __str__(self):
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
