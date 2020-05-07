
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
        return len(self.strbases)
