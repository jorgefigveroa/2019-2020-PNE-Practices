def seq_read_fasta(filename):
    for letter in filename:
        if letter == "A" or "C" or "T" or "G":
            return letter

print(seq_read_fasta(Homo_sapiens_RNU6_1110P_sequence.fa))