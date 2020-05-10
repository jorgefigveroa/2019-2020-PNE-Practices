from Client0 import Client

SESSION = 10
EXERCISE = 1

print(f"-----| SESSION {SESSION}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.42"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

print(c)
# -- Send a message to the server
print("Sending a message to the server...")
response1 = c.talk("Test1...")
print(f"ECHO: {response1}")

print("Sending a message to the server...")
response2 = c.talk("Test2...")
print(f"ECHO: {response2}")

print("Sending a message to the server...")
response3 = c.talk("Test3...")
print(f"ECHO: {response3}")
