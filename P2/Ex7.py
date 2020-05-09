# -- Write a python program that takes 10 fragments of 10 bases each from
# -- the FRAT1 gene and sends them to two servers. The odd segments
# -- (1,3,5,7 and 9) should be sent to server 1, and the even segments
# -- (2,4,6,8 and 10) to server 2. The client should print on the console
# -- all the fragments

from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.42"
PORT1 = 8080
PORT2 = 8081
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)
s = Seq()
s.read_fasta("../SESSION-04/FRAT1.txt")
s1 = str(s)
message = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."


def cutting_fragments(n1, n2, sqq1):
    string = ""
    for index in range(n1, n2):
        string = string + sqq1[index]
    return string


def list_fragments(k, sq1):
    list1 = []
    for index in range(1, k + 1):
        n1 = 10 * (index - 1)
        n2 = 10 * index
        a = cutting_fragments(n1, n2, sq1)
        list1.append(a)
    return list1


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listfrags = list_fragments(10, s1)
everything = dict(zip(number_list, listfrags))
listvalues = list(everything.values())
even_list = [2, 4, 6, 8, 10]
odd_list = [1, 3, 5, 7, 9]
print(f"Gene FRAT1: {s1}")
for key in everything:
    print(f"Fragment {key}: {everything[key]}")

c1.talk(message)
c2.talk(message)

for i in even_list:
    c2.talk(f" Fragment {i}: {everything[i]}")
for i in odd_list:
    c1.talk(f" Fragment {i}: {everything[i]}")
