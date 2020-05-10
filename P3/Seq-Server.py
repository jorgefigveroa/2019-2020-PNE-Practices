import socket
import termcolor
from Seq1 import Seq

# -- CONFIGURING THE PORT AND THE IP

PORT = 8080
IP = "127.0.0.1"
listseqs = ["GAGCAGGAGCAGGTGCTGGCACAAGAGATAGAAGAGCTGTATTTGAAGCTGTCCTCACAG",
            "GGTTAACAAGAGTTCTGGACAGAAATATAGTTATAATTAAGCATTAGTCAGGCTGCAATT",
            "TGACTCATTTCCTTGTAGCCAGAATTCATGGAGCACTAGATGTTGACCATTTGTATCCCC",
            "ATTGTTTCTACAGATGAAATTTCTGATGTTAGAATCATAAGGGTTTTGTTTAAGAATGAC",
            "TTAAACAGATCCTTAATTCTAGTGGAGTAGCTGATGCCAACCACTTCAAAGATCCCACAG"]
# -- STEP 1: CREATING


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- OPTIONAL:

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- STEP 2: BINDING

ls.bind((IP, PORT))

# -- STEP 3: LISTENING

ls.listen()
print("SEQ Server configured!")


# -- STEP 4: LOOPING

# FUNCTIONS:

def get(string):
    for i, k in enumerate(listseqs):
        if string == f"GET {i}":
            return k


def sepparate(word, string):
    if word in string:
        x = string.partition(word)
        rest = x[2].replace(" ", "")
        return rest


def info(string):
    rest = sepparate("INFO", string)
    s = Seq(rest)
    dictionarycount = s.count
    length = s.len()
    list0 = f"Sequence: {rest}\n" \
            f"Total length:{length}\n"
    for key in dictionarycount:
        average = (int(dictionarycount[key]) / length) * 100
        potato = f"{key}: {dictionarycount[key]} ({round(average, 1)}%)\n"
        list0 = list0 + potato
    return list0


def comp(string):
    rest = sepparate("COMP", string)
    s = Seq(rest)
    return s.complement


def rev(string):
    rest = sepparate("REV", string)
    s = Seq(rest)
    apple = s.reverse
    return str(apple)


def gene(string):
    folder = "../SESSION-04/"
    txt = ".txt"
    rest = sepparate("GENE", string)
    s = Seq()
    banana = s.read_fasta(folder + rest + txt)
    return str(banana)


while True:
    # -- WAIT FOR CLIENT TO CONNECT:
    print("Waiting for client to connect...")

    try:

        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user.")

        # -- CLOSING
        ls.close()

        # -- EXITING
        exit()

    else:

        # -- READING AND RECEIVING
        msg_raw = cs.recv(2048)

        # -- DECODING AND SENDING

        msg = msg_raw.decode()
        if "PING" in msg:
            termcolor.cprint("PING command!", "green")
            response = "OK!\n"
            cs.send(response.encode())
            print(response)

        elif "INFO" in msg:
            termcolor.cprint("INFO", "green")
            response = info(msg)
            cs.send(response.encode())
            print(response)
            print()

        elif "COMP" in msg:
            termcolor.cprint("COMP", "green")
            response = comp(msg)
            cs.send(response.encode())
            print(response)
            print()

        elif "REV" in msg:
            termcolor.cprint("REV", "green")
            response = rev(msg)
            cs.send(response.encode())
            print(response)
            print()

        elif "GENE" in msg:
            termcolor.cprint("GENE", "green")
            response = gene(msg)
            cs.send(response.encode())
            print(response)
            print()

        for j in range(0, 5):
            if msg == f"GET {j}":
                termcolor.cprint("GET", "green")
                a = get(msg)
                cs.send(a.encode())
                print(a)
                print("\n")

        # -- CLOSING

        cs.close()
