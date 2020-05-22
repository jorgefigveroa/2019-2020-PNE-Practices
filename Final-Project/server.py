import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json

# -- THE PORT
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# -- FUNCTIONS

# -- With function: connecting we can connect to the ensembl database server and obtain all the information we want
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
                     <h4> Warning: the limit you introduce must be an integer number between 1
                            and the total number of species.</h4>
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
                     <h4> Warning: the species you introduce must be in the ensembl database.</h4>
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
                     <h4> Warning: the species you introduce must be in the ensembl database
                        and the chromosome must also be in the database, else, an error will be shown</h4>
                    <p> The length of the chromosome is: {chromo} </p>
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
                contents = Path('index.html').read_text()
                content_type = 'text/html'
                error_code = 200
            elif resource == "/listSpecies":
                ENDPOINT = "/info/species"
                data = listSpecies(ENDPOINT)
                if "limit" in self.path:
                    limit = self.path.split('limit=')
                    number = limit[1]
                    contents = showing_listSpecies(data[0:int(number)], data)
                else:
                    contents = showing_listSpecies(data, data)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/karyotype':
                species = splitting(self.path, 'specie=', 1)
                ENDPOINT = "/info/assembly/" + species
                data = karyotype(ENDPOINT)
                contents = showing_karyotype(data)
                content_type = 'text/html'
                error_code = 200
            elif resource == '/chromosomeLength':
                complete = splitting(self.path, 'specie=', 1)
                species = splitting(complete, "&chromo=", 0)
                chromosome = splitting(complete, "&chromo=", 1)
                ENDPOINT = "/info/assembly/" + species
                data = chromosome_length(ENDPOINT, chromosome)
                contents = showing_chromolength(data)
                content_type = 'text/html'
                error_code = 200
            else:
                contents = Path('Error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        except (ValueError, KeyError):
            contents = Path('Error.html').read_text()
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
