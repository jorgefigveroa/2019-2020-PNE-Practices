from pathlib import Path


def seq_ping():
    return "OK!"


def seq_read_fasta(filename):
    contents = Path(filename).read_text().split("\n")
    seq = "".join(contents)
    return seq


def seq_len(seq):
    length = len(seq)
    return length


def seq_count_base(seq, base):
    count1 = 0
    for element in seq:
        if element == base:
            count1 = count1 + 1
    return count1


def count(seq):
    listbases = ["A", "C", "T", "G"]
    listnumbers = [seq_count_base(seq, "A"), seq_count_base(seq, "C"), seq_count_base(seq, "T"),
                   seq_count_base(seq, "G")]
    dictionary = dict(zip(listbases, listnumbers))
    return dictionary


def seq_reverse(seq):
    reverse = seq[::-1]
    return reverse
