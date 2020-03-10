from pathlib import Path


def seq_ping():
    return "OK!"


def seq_read_fasta(filename):
    contents = Path(filename).read_text().split("\n")[1:]
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


#def seq_read_fasta(filename):
    #for letter in filename:
        #if letter == "A" or "C" or "T" or "G":
            #return letter  (ANOTHER WAY TO DO THE SEQ_READ_FASTA FUNCTION)


def count(seq):
    listbases = ["A", "C", "T", "G"]
    listnumbers = []
    for base in listbases:
        a = seq_count_base(seq,base)
        listnumbers.append(a)
    dictionary = dict(zip(listbases, listnumbers))
    return dictionary


def seq_reverse(seq):
    reverse = seq[::-1]
    return reverse
