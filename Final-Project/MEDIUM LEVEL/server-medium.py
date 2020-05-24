import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq

# -- THE PORT
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# -- FUNCTIONS

# -- With function: connecting we can connect to the ensembl database server and obtain all the information we want
def connecting(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "content-type=application/json"
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


#  --------------------- 1 -----------------------------------------
# -- With this function: listSpecies, we can obtain what a list of what the client is asking for
def listSpecies(ENDPOINT):
    response = connecting(ENDPOINT)
    count = 0
    list_Species = []
    for elements in response:
        for things in response[elements]:
            count = count + 1
            list_Species.append(things['display_name'])
    ordered_list = sorted(list_Species)
    return ordered_list


# -- We transform any list into a string, to import to html
def stringlist(anylist):
    whole_list = ""
    for element in anylist:
        whole_list = whole_list + " &nbsp;&nbsp;&nbsp;&nbsp; &#9679 " + element + "<br>"
    return whole_list


def splitting(word, string, number):
    splitted = word.split(string)
    new_word = splitted[number]
    return new_word


# -- The html file that will be imported to the client
def showing_listSpecies(cut_listSpecies, total_listSpecies):
    contents = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> LIST OF SPECIES </title>
    <head> 
    <body style="background-color: lightgreen;">
        <h1>DATA ASKED:</h1>
        <p> The total number of species in the ensembl is: {len(total_listSpecies)} </p>
        <p> The limit you have selected is: {len(cut_listSpecies)} </p>
        <p>The list of the species is: <br> {stringlist(cut_listSpecies)}</p>
            <a href="http://127.0.0.1:8080/">[Main page]</a>
    </body>
    </html>
                    """
    return contents


#  --------------------- 2 ---------------------------------
def karyotype(ENDPOINT):
    response = connecting(ENDPOINT)
    karyolist = response['karyotype']
    return karyolist


# -- The html file that will be imported to the client
def showing_karyotype(karyolist):
    contents = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> KARYOTYPE </title>
    <head> 
    <body style="background-color: lightblue;">
        <h1>DATA ASKED:</h1>
        <p> The names of the chromosomes are: <br> {stringlist(karyolist)} </p>
            <a href="http://127.0.0.1:8080/">[Main page]</a>
    </body>
    </html>
                    """
    return contents


#  --------------------- 3---------------------------------
def chromosome_length(ENDPOINT, number):
    response = connecting(ENDPOINT)
    list_chromosome = []
    for elements in response['top_level_region']:
        if elements['coord_system'] == 'chromosome':
            list_chromosome.append(elements)
    for element in list_chromosome:
        if element['name'] == number:
            chromo = element['length']
            return chromo


# -- The html file that will be imported to the client

def showing_chromolength(chromo):
    contents = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> CHROMOSOME LENGTH </title>
    <head> 
    <body style="background-color: #FFA07A;">
        <h1>DATA ASKED:</h1>
        <p> The length of the chromosome is: {chromo} </p>
            <a href="http://127.0.0.1:8080/">[Main page]</a>
    </body>
    </html>
                    """
    return contents


#  --------------------- 4---------------------------------
def ID_function(INPUT):
    ENDPOINT1 = "/lookup/symbol/homo_sapiens/"
    GENE = connecting(ENDPOINT1 + INPUT + "?")
    ID_gene = GENE['id']
    return ID_gene


def sequence(INPUT):
    ID = ID_function(INPUT)
    ENDPOINT2 = "/sequence/id/"
    sequence_dict = connecting(ENDPOINT2 + ID + "?")
    seq = sequence_dict['seq']
    return seq


# -- The html file that will be imported to the client

def showing_geneSeq(whole_sequence):
    contents = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> WHOLE SEQUENCE </title>
    <head> 
    <body style="background-color: #E0FFFF;">
        <h1>DATA ASKED:</h1>
        <p> The sequence is:  </p>
        <textarea readonly id="GENE" rows="10" cols="70">{whole_sequence} </textarea>
<br><br>
            <a href="http://127.0.0.1:8080/">[Main page]</a>

    </body>
    </html>
                    """
    return contents


#  --------------------- 5 ---------------------------------
def finding_chromosome(ID):
    ENDPOINT = "/sequence/id/"
    response = connecting(ENDPOINT + ID + "?")
    information = response['desc']
    chromosome = information.split(":")[2]
    return chromosome


# -- The html file that will be imported to the client

def showing_geneInfo(whole_sequence, id_seq, chromosome):
    contents = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> INFORMATION </title>
    <head> 
    <body style="background-color: #D8BFD8;">
        <h1>DATA ASKED:</h1>
        <p> The sequence's start is: {whole_sequence[0:10]}...</p><br>
        <p> The sequence's end is: ...{whole_sequence[-10:]} </p><br>
        <p> The sequence's length is:{len(whole_sequence)} </p><br>
        <p> The sequence's ID is:{id_seq} </p><br>
        <p> The sequence is located in the chromosome :{chromosome} </p><br>

<br><br>
            <a href="http://127.0.0.1:8080/">[Main page]</a>

    </body>
    </html>
                    """
    return contents


#  --------------------- 6 ---------------------------------
def calculations(whole_seq):
    s = Seq(whole_seq)
    dictionarycount = s.count
    length = s.len()
    list0 = f"Total length: {length}<br><br>"
    for key in dictionarycount:
        average = (int(dictionarycount[key]) / length) * 100
        bases = f"{key}: {dictionarycount[key]} ({round(average, 1)}%)\n"
        list0 = list0 + bases + f"<br><br>"
    return list0


def showing_geneCalc(statistics):
    contents = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> CALCULATIONS </title>
    <head> 
    <body style="background-color: #F0F8FF;">
        <h1>DATA ASKED:</h1>
        <p> The calculations are:<br><br>{statistics} </p><br>
<br><br>
            <a href="http://127.0.0.1:8080/">[Main page]</a>

    </body>
    </html>
                    """
    return contents


#  --------------------- 7 ---------------------------------
def gene_dictionary(gene):
    list1 = []
    for dictionary in gene:
        list1.append(dictionary['external_name'])
    return list1


def showing_geneList(genes):
    contents = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> SEQUENCE </title>
    <head> 
    <body style="background-color: #E6E6FA;">
        <h1>DATA ASKED:</h1>
        <p> The genes are:  </p>
        <p>{stringlist(genes)} <p>
<br><br>
            <a href="http://127.0.0.1:8080/">[Main page]</a>

    </body>
    </html>
                    """
    return contents


# -- Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# --  Our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # -- THE REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        # -- NOTE: self.path already contains the requested resource
        list_resource = self.path.split('?')
        resource = list_resource[0]

        try:
            if resource == "/":
                # Read the file
                contents = Path('index-medium.html').read_text()
                content_type = 'text/html'
                error_code = 200
            elif resource == "/listSpecies":
                ENDPOINT = "/info/species"
                data = listSpecies(ENDPOINT + "?")
                if "limit" in self.path:
                    number1 = splitting(self.path, 'limit=', 1)
                    if number1 !=  "":
                        number = number1
                    else:
                        number = len(data)
                    contents = showing_listSpecies(data[0:int(number)], data)
                else:
                    contents = showing_listSpecies(data, data)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/karyotype':
                species = splitting(self.path, 'specie=', 1)
                ENDPOINT = "/info/assembly/" + species
                data = karyotype(ENDPOINT + "?")
                contents = showing_karyotype(data)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/chromosomeLength':
                complete = splitting(self.path, 'specie=', 1)
                species = splitting(complete, "&chromo=", 0)
                chromosome = splitting(complete, "&chromo=", 1)
                ENDPOINT = "/info/assembly/" + species + "?"
                data = chromosome_length(ENDPOINT, chromosome)
                contents = showing_chromolength(data)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/geneSeq':
                user_input = splitting(self.path, "gene=", 1)
                seq = sequence(user_input)
                contents = showing_geneSeq(seq)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/geneInfo':
                user_input = splitting(self.path, "gene=", 1)
                seq = sequence(user_input)
                ID_input = ID_function(user_input)
                chromosome = finding_chromosome(ID_input)
                contents = showing_geneInfo(seq, ID_input, chromosome)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/geneCalc':
                user_input = splitting(self.path, "gene=", 1)
                seq = sequence(user_input)
                calculating = calculations(seq)
                contents = showing_geneCalc(calculating)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/geneList':
                cutting = splitting(self.path, "chromo=", 1)
                chromosome = splitting(cutting, "&start=", 0)
                end = splitting(cutting, "&end=", 1)
                cutting2 = splitting(cutting, "&end=", 0)
                start = splitting(cutting2, "&start=", 1)
                ENDPOINT1 = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + "?feature=gene;"
                response = connecting(ENDPOINT1)
                genes = gene_dictionary(response)
                contents = showing_geneList(genes)
                content_type = 'text/html'
                error_code = 200
            else:
                contents = Path('Error-medium.html').read_text()
                content_type = 'text/html'
                error_code = 404
        except (ValueError, KeyError, IndexError, TypeError):
            contents = Path('Error-medium.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
