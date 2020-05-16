import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

# -- CONNECTING

conn = http.client.HTTPConnection(SERVER)

# -- MESSAGING

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- READING RESPONSE
r1 = conn.getresponse()

# -- STATUS LINE
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- DECODING
data1 = r1.read().decode("utf-8")

# -- CREATING A VARIABLE WITH THE DATA
response = json.loads(data1)

if response['ping'] == 1:
    print("PING OK! The database is running.")
