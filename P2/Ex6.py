# -- Write a python program that takes 5 fragments of 10 bases each from the FRAT1 gene
# -- and sends them to the server.
# -- Use the talk method. Print the fragments on the Client console for checking

from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.42"
PORT = 8080
c = Client(IP, PORT)
print(c)
s = Seq()
s.read_fasta("../SESSION-04/FRAT1.txt")
s1 = str(s)
message = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."
F1 = ""
F2 = ""
F3 = ""
F4 = ""
F5 = ""

for index in range(0, 50):
    if 0 <= index < 10:
        F1 = F1 + s1[index]
    elif 10 <= index < 20:
        F2 = F2 + s1[index]
    elif 20 <= index < 30:
        F3 = F3 + s1[index]
    elif 30 <= index < 40:
        F4 = F4 + s1[index]
    elif 40 <= index < 50:
        F5 = F5 + s1[index]

listFragments = [F1, F2, F3, F4, F5]
print(f"Gene FRAT1:{s1}")

for i, k in enumerate(listFragments):
    print(f"Fragment {i}: {k}")

c.talk(message)

for i, k in enumerate(listFragments):
    c.talk(f"Fragment {i}: {k}")
