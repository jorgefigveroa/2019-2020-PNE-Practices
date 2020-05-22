import http.client
import json
from Seq1 import Seq


def connecting(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
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
    return response


def ID_function(INPUT):
    ENDPOINT1 = "/lookup/symbol/homo_sapiens/"
    GENE = connecting(ENDPOINT1 + INPUT)
    ID_gene = GENE['id']
    return ID_gene


def sequence(INPUT):
    ID = ID_function(INPUT)
    ENDPOINT2 = "/sequence/id/"
    sequence_dict = connecting(ENDPOINT2 + ID)
    seq = sequence_dict['seq']
    return seq


def finding_chromosome(ID):
    ENDPOINT = "/sequence/id/"
    response = connecting(ENDPOINT + ID)
    information = response['desc']
    chromosome = information.split(":")[2]
    return chromosome


def calculations(whole_seq):
    sequence = Seq(whole_seq)
    dictionarycount = sequence.count
    length = sequence.len()
    list0 = f"Total length:{length}<br><br>"
    for key in dictionarycount:
        average = (int(dictionarycount[key]) / length) * 100
        bases = f"{key}: {dictionarycount[key]} ({round(average, 1)}%)\n"
        list0 = list0 + bases + f"<br><br>"
    return list0


ENDPOINT1 = "/sequence/region/human/10:97319271:97319281"
id = ID_function("FRAT1")
print(connecting('/sequence/id/' + id))

s = connecting(ENDPOINT1)

print(s['seq'])
