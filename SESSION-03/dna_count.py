# Create a program for counting the number of bases presented in a DNA sequence.

seq = "CATGTAGACTAG"

length = len(seq)


def countbase(n, sequence):
    count = 0
    for i in sequence:
        if i == n:
            count = count + 1
    return count


# PRINTING THE SEQUENCE.
print("Introduce the sequence: ", seq)
# WITH THE LENGTH FUNCTION WE CALCULATE THE TOTAL LENGTH OF THE STRING.
print("Total length: ", length)
# WITH THE COUNTBASE FUNCTION WE CREATED BEFORE WE COUNT BASES.
print("A: ", countbase("A", seq))
print("C: ", countbase("C", seq))
print("T: ", countbase("T", seq))
print("G: ", countbase("G", seq))
