
class Seq:
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL Seq created")
        else:
            bases = ["A", "C", "T", "G"]
            for b in strbases:
                if b not in bases:
                    print("INVALID Seq!")
                    self.strbases = "ERROR"
                    return
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL":
            return 0
        if self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL":
            return "0"
        if self.strbases == "ERROR":
            return "0"
        else:
            return self.strbases.count(base)
    @property
    def count(self):
        listbases = ["A", "C", "T", "G"]
        listzeros = [0, 0, 0, 0]
        zerodict = dict(zip(listbases, listzeros))
        if self.strbases == "NULL":
            return zerodict
        if self.strbases == "ERROR":
            return zerodict
        else:
            list2 = {"A": self.count_base("A"), "C": self.count_base("C"),
                     "T": self.count_base("T"), "G": self.count_base("G") }
            return list2

    def reverse(self):
