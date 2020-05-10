from Client0 import Client

PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "127.0.0.1"
PORT = 8080

# -- CREATING
c = Client(IP, PORT)

print(c)

# -- MESSAGING

list1 = ["PING ", "GET ", "INFO ", "COMP ", "REV "]
sequence = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"

for element in list1:
    print(f"*Testing {element}...")
    if element == "GET ":
        for i in range(0, 5):
            number = str(i)
            response = c.talk(element + number)
            print(f"GET {i}: {response}")
        print()
    else:
        if element != "PING " and element != "INFO ":
            print(f"{element} {sequence}")
        response = c.talk(element + sequence)
        print(response)
        print()

list2 = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print(f"*Testing GENE...")
a = "GENE "
for element in list2:
    print(a+element)
    response = c.talk(a+element)
    print(response)
    print()
