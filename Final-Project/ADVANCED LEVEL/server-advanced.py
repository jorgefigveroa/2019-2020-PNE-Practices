import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq
import random

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
def main_page():
    contents = f"""<br><br><a href="http://127.0.0.1:8080/">[Main page]</a> """
    return contents


def showing_listSpecies(cut_listSpecies, total_listSpecies, limit_selected):
    contents = f"""
        <p> The total number of species in the ensembl is: {len(total_listSpecies)} </p>
        <p> The limit you have selected is: {limit_selected} </p>
        <p>The list of the species is: <br> {stringlist(cut_listSpecies)}</p>
                    """
    return contents + main_page()


def transform(anydict):
    transformed = json.dumps(anydict)
    return transformed


# -- The json file that will be imported to the client

def dict_listSpecies(cut_listSpecies, total_listSpecies, limit):
    contents = {
        "total_number_of_species": len(total_listSpecies),
        "limit": limit,
        "list_species": cut_listSpecies,
    }
    return transform(contents)


def deletingjson(link1):
    link = splitting(link1, "&json=", 0)
    return link


def value(json1):
    jsonvalue = splitting(json1, "&json=", 1)
    return jsonvalue


#  --------------------- 2 ---------------------------------
def karyotype(ENDPOINT):
    response = connecting(ENDPOINT)
    karyolist = response['karyotype']
    return karyolist


# -- The html file that will be imported to the client
def showing_karyotype(karyolist, species):
    contents = f"""
        <p> Species selected: {species} </p>
        <p> The names of the chromosomes are: <br> {stringlist(karyolist)} </p>
                    """
    return contents + main_page()


# -- The json file that will be imported to the client

def dict_karyotype(karyolist, species):
    contents = {"species": species, "chromosomes": karyolist}
    return transform(contents)


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

def showing_chromolength(chromo, species, chromosome):
    contents = f""" <p> Species selected: {species} </p>
                    <p> Chromosome selected: {chromosome} </p>
                    <p> The length of the chromosome is: {chromo} </p> """
    return contents + main_page()


# -- The json file that will be imported to the client
def dict_chromolength(chromo, species, chromosome):
    contents = {"species": species, "chromosome": chromosome, "length": chromo}
    return transform(contents)


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

def showing_geneSeq(whole_sequence, gene):
    contents = f""" 
        <p> The gene is: {gene}  </p>
        <p> The sequence is:  </p>
        <textarea readonly id="GENE" rows="10" cols="70">{whole_sequence} </textarea>
                    """
    return contents + main_page()


# -- The json file that will be imported to the client
def dict_geneSeq(whole_sequence, gene):
    contents = {"gene": gene, "sequence": whole_sequence}
    return transform(contents)


#  --------------------- 5 ---------------------------------
def finding_chromosome(ID):
    ENDPOINT = "/sequence/id/"
    response = connecting(ENDPOINT + ID + "?")
    information = response['desc']
    chromosome = information.split(":")[2]
    return chromosome


# -- The html file that will be imported to the client

def showing_geneInfo(whole_sequence, id_seq, chromosome, gene):
    contents = f"""
        <p> The name of the gene is: {gene} </p> <br>
        <p> The sequence's start is: {whole_sequence[0:10]}...</p>
        <p> The sequence's end is: ...{whole_sequence[-10:]} </p>
        <p> The sequence's length is: {len(whole_sequence)} </p>
        <p> The sequence's ID is: {id_seq} </p>
        <p> The sequence is located in the chromosome: {chromosome} </p>
                    """
    return contents + main_page()


# -- The json file that will be imported to the client
def dict_geneInfo(whole_sequence, id_seq, chromosome, gene):
    contents = {"gene": gene,
                "start": whole_sequence[0:10],
                "end": whole_sequence[-10:],
                "length": len(whole_sequence),
                "ID": id_seq,
                "chromosome": chromosome}

    return transform(contents)


#  --------------------- 6 ---------------------------------
def percentages(whole_seq):
    listBases = ["A", "C", "T", "G"]
    listPerc = []
    s = Seq(whole_seq)
    dictionarycount = s.count
    length = s.len()
    for key in dictionarycount:
        average = (int(dictionarycount[key]) / length) * 100
        average_rounded = round(average, 1)
        listPerc.append(average_rounded)
    percentage = dict(zip(listBases, listPerc))
    return percentage


def percentages_dict(dictionary):
    string = ""
    for key in dictionary:
        sub = f"""{key}  --> {dictionary[key]}% <br>"""
        string = string + " &nbsp;&nbsp;&nbsp;&nbsp; &#9679 " + sub
    return string


# -- The html file that will be imported to the client
def showing_geneCalc(whole_seq, gene):
    contents = f""" 
        <p> Gene: {gene} <p>
        <p> The calculations are:<br><br>
            Length: {len(whole_seq)} <br><br>
            Percentages: <br> {percentages_dict(percentages(whole_seq))}
                    </p><br>
                    """
    return contents + main_page()


# -- The json file that will be imported to the client
def dict_geneCalc(whole_seq, gene):
    contents = {"gene": gene, "length": len(whole_seq), "percentage_of_each_base:": percentages(whole_seq)}
    return transform(contents)


#  --------------------- 7 ---------------------------------
def showing_geneList(genes, chromosome, start, end):
    contents = f""" 
        <p>Located in the chromosome: {chromosome}</p>
        <p>Start: {start}</p>
        <p>End: {end}</p>
        <p>The sequence is: <br> {stringlist(genes)} </p>
                    """
    return contents + main_page()


def gene_dictionary(gene):
    list1 = []
    for dictionary in gene:
        list1.append(dictionary['external_name'])
    return list1


# -- The json file that will be imported to the client
def dict_geneList(genes, chromosome, start, end):
    contents = {"location": chromosome, "start": start, "end": end, "genes": genes}
    return transform(contents)


# -- To print our HTML
def HTMLdoc():
    listcolors = ['#D8BFD8', 'lightgreen', 'lightblue', '#E0FFFF', '#E6E6FA', "#F0F8FF", "#FFA07A", '#FFC0CB']
    color = random.choice(listcolors)
    doc = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset= "utf-8">
        <title> DATA </title>
    <body style="background-color: {color};">
        <h1>DATA ASKED:</h1>
         """
    return doc


# -- Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# --  Our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # -- THE REQUEST LINE
        termcolor.cprint(self.requestline, 'green')
        list_resource = self.path.split('?')
        resource = list_resource[0]

        if "&json=" in self.path:
            link = deletingjson(self.path)
            values = value(self.path)
        else:
            link = self.path
            values = "0"

        try:
            if resource == "/":
                contents = Path('index-advanced.html').read_text()
            elif resource == "/listSpecies":
                ENDPOINT = "/info/species?"
                data = listSpecies(ENDPOINT)
                if "limit" in link:
                    number = splitting(link, 'limit=', 1)
                    if values == "1":
                        contents = dict_listSpecies(data[0:int(number)], data, number)
                    else:
                        contents = HTMLdoc() + showing_listSpecies(data[0:int(number)], data, number)
                else:
                    if values == "1":
                        contents = dict_listSpecies(data, data, data)
                    else:
                        contents = HTMLdoc() + showing_listSpecies(data, data, data)
            elif resource == '/karyotype':
                species = splitting(link, 'specie=', 1)
                ENDPOINT = "/info/assembly/" + species + "?"
                data = karyotype(ENDPOINT)
                if values == "1":
                    contents = dict_karyotype(data, species)
                else:
                    contents = HTMLdoc() + showing_karyotype(data, species)
            elif resource == '/chromosomeLength':
                complete = splitting(link, 'specie=', 1)
                species = splitting(complete, "&chromo=", 0)
                chromosome = splitting(complete, "&chromo=", 1)
                ENDPOINT = "/info/assembly/" + species + "?"
                data = chromosome_length(ENDPOINT, chromosome)
                if values == "1":
                    contents = dict_chromolength(data, species, chromosome)
                else:
                    contents = HTMLdoc() + showing_chromolength(data, species, chromosome)
            elif resource == '/geneSeq':
                user_input = splitting(link, "gene=", 1)
                seq = sequence(user_input)
                if values == "1":
                    contents = dict_geneSeq(seq, user_input)
                else:
                    contents = HTMLdoc() + showing_geneSeq(seq, user_input)
            elif resource == '/geneInfo':
                user_input = splitting(link, "gene=", 1)
                seq = sequence(user_input)
                ID_input = ID_function(user_input)
                chromosome = finding_chromosome(ID_input)
                if values == "1":
                    contents = dict_geneInfo(seq, ID_input, chromosome, user_input)
                else:
                    content2 = showing_geneInfo(seq, ID_input, chromosome, user_input)
                    contents = HTMLdoc() + content2
            elif resource == '/geneCalc':
                user_input = splitting(link, "gene=", 1)
                seq = sequence(user_input)
                if values == "1":
                    contents = dict_geneCalc(seq, user_input)
                else:
                    content2 = showing_geneCalc(seq, user_input)
                    contents = HTMLdoc() + content2
            elif resource == '/geneList':
                cutting = splitting(link, "chromo=", 1)
                chromosome = splitting(cutting, "&start=", 0)
                end = splitting(cutting, "&end=", 1)
                cutting2 = splitting(cutting, "&end=", 0)
                start = splitting(cutting2, "&start=", 1)
                ENDPOINT1 = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + "?feature=gene;"
                response = connecting(ENDPOINT1)
                genes = gene_dictionary(response)
                if values == "1":
                    contents = dict_geneList(genes, chromosome, start, end)
                else:
                    content2 = showing_geneList(genes, chromosome, start, end)
                    contents = HTMLdoc() + content2

            else:
                contents = Path('Error-advanced.html').read_text()
        except (ValueError, KeyError, IndexError, TypeError):
            contents = Path('Error-advanced.html').read_text()

        list_resources = ["/", "/listSpecies", "/karyotype", "/chromosomeLength",
                          "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]

        if resource in list_resources:
            error_code = 200
            if values == "1":
                content_type = "application/json"
            else:
                content_type = "text/html"
        else:
            error_code = 404
            content_type = "text/html"

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
