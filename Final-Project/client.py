import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Supposing the user introduces all of the ENDPOINTS RIGHT
r1 = "/listSpecies?limit=10&json=1"
r2 = "/karyotype?specie=chicken&json=1"
r3 = "/chromosomeLength?specie=chicken&chromo=MT&json=1"
r4 = "/geneSeq?gene=FRAT1&json=1"
r5 = "/geneInfo?gene=ADA&json=1"
r6 = "/geneCalc?gene=MIR633&json=1"
r7 = "/geneList?chromo=1&start=0&end=30000&json=1"

# -- SUPPOSING the user makes mistakes
r8 = "/geneList?chromo=1&start=0&end=30000&json=0"
r9 = "/geneList?chromo=&start=&end=&json=1"
r10 = "/page_doesnt_exist&json=1"
r11 = "/listSpecies?limit=10"
r12 = "/listSpecies"

requests = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11,r12]

count = 0
for request1 in requests:
    try:
        try:
            count = count + 1
            conn.request("GET", request1)
            print("---------------------------------------------------")
            termcolor.cprint(f"My request {count}:", 'green', end="")
            print(request1)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print()
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        data1 = r1.read().decode("utf-8")

        # -- Create a variable with the data,
        # -- form the JSON received
        response = json.loads(data1)
        termcolor.cprint(f"Response {count}: ", "blue", end="")
        print(response)
        print()
    except json.decoder.JSONDecodeError:
        termcolor.cprint("Cant't be read because json's value is not 1 or error in the endpoint", "red")
