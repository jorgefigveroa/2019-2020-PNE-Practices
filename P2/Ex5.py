from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.42"
PORT = 8080
# -- More parameters:
message = "Sending the U5 Gene to the server..."
s = Seq()
s.read_fasta("../SESSION-04/U5.txt")

# -- Create a client object
c = Client(IP, PORT)

print(c)
c.debug_talk(message)
c.debug_talk(str(s))
