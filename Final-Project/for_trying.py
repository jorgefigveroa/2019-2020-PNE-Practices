import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/assembly/human"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

# -- CONNECTING

connection = http.client.HTTPConnection(SERVER)

# -- MESSAGING

try:
    connection.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- READING RESPONSE
r1 = connection.getresponse()

# -- STATUS LINE
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- DECODING
data1 = r1.read().decode("utf-8")

# -- CREATING A VARIABLE WITH THE DATA
response = json.loads(data1)

print(response['karyotype'])