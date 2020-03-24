import termcolor

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

    @property
    def len(self):
        return len(self.strbases)


def print_seqs(seq_lists,color):
    for element in seq_lists:
        termcolor.cprint(f"Sequence {seq_lists.index(element)}: (Length: {element.len}) {element}",color)


def generate_seqs(pattern, number):
    list1 = []
    count = ""
    for element in range(0, number):
        count = count + pattern
        list1.append(Seq(count))
    return list1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1,"blue")

print()
print("List 2:")
print_seqs(seq_list2,"green")
