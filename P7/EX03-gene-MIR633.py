import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
MIR633 = "/ENSG00000207552"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + MIR633 + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

# -- CONNECTING

conn = http.client.HTTPConnection(SERVER)

# -- MESSAGING

try:
    conn.request("GET", ENDPOINT + MIR633 + PARAMS)
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

termcolor.cprint("GENE: ", "green", end="")
print("MIR633")

termcolor.cprint("DESCRIPTION: ", "green", end="")
print(response['desc'])

termcolor.cprint("BASES: ", "green", end="")
print(response['seq'])
