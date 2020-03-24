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

    def len(self):
        return len(self.strbases)


def print_seqs(seq_lists):
    for element in seq_lists:
        print(f"Sequence {seq_lists.index(element)}: (Length: {element.len()}) {element}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)
