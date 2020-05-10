from Client0 import Client

SESSION = 10
EXERCISE = 4

print(f"-----| SESSION {SESSION}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.42"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

print(c)
# -- Send a message to the server

for i in range(0, 5):
    c.debug_talk(f"Message {i}")
    print()
