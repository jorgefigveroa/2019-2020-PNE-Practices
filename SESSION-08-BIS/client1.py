import socket

IP = "212.128.253.128"
PORT = 8080

# --- WE CREATE THE SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# --- FOR ESTABLISHING THE CONNECTION WITH THE SERVER
s.connect((IP, PORT))

# --- SEND DATA TO THE SERVER
s.send(str.encode("hello"))

# ---- RECIEVE DATA FROM THE SERVER

msg = s.recv(2000)

print("Message from the server: \n")
print(msg.decode("utf-8"))

# ----  CLOSING THE SERVER
s.close()
