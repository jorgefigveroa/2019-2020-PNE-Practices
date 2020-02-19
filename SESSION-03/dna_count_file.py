file = "dna.txt"


def countbase(n, sequence):
    count = 0
    for i in sequence:
        if i == n:
            count = count + 1
    return count


def formatting(lists):
    if "\n" in lists:
        lists.pop(-1)
        return lists
    else:
        return lists


def typeofbase(sequence):
    listbase = []
    for base in sequence:
        if base not in listbase:
            listbase.append(base)
    z = formatting(listbase)
    return z


def length(sequence):
    if "\n" in sequence:
        return len(sequence) - 1
    else:
        return len(sequence)


with open(file, "r") as f:
    for seq in f:
        a = typeofbase(seq)
        print("for: ", seq, "\n length: ", length(seq))
        for character in a:
            print(character, ": ", countbase(character, seq))
