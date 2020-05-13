import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- FUNCTIONS

listseqs = ["GAGCAGGAGCAGGTGCTGGCACAAGAGATAGAAGAGCTGTATTTGAAGCTGTCCTCACAG",
            "GGTTAACAAGAGTTCTGGACAGAAATATAGTTATAATTAAGCATTAGTCAGGCTGCAATT",
            "TGACTCATTTCCTTGTAGCCAGAATTCATGGAGCACTAGATGTTGACCATTTGTATCCCC",
            "ATTGTTTCTACAGATGAAATTTCTGATGTTAGAATCATAAGGGTTTTGTTTAAGAATGAC",
            "TTAAACAGATCCTTAATTCTAGTGGAGTAGCTGATGCCAACCACTTCAAAGATCCCACAG"]


def get(number):
    n = int(number)
    return listseqs[n]


def gene(string):
    folder = "../SESSION-04/"
    txt = ".txt"
    s = Seq()
    banana = s.read_fasta(folder + string + txt)
    return str(banana)


def msg(pathmessage, sepparator, n):
    list1 = pathmessage.partition(sepparator)
    rest = list1[n].replace("+", " ")
    return rest


# def check_on(message):
# mensaje = msg(message)
# normal = mensaje.replace("&chk=on", "")
# return normal.upper()


def ping():
    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset= "utf-8">
                        <title> PING OK! </title>
                    <head> 
                    <body>
                        <h1> PING OK! </h1>
                        <p> The SEQ2 server in running... </p>
                    <a href="http://127.0.0.1:8080/">[Main page]</a>
                    </body>
                    </html>
                    """
    return contents


def getting(message):
    decoded_number = msg(message, "/get?get=", 2)
    string = get(decoded_number)
    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset= "utf-8">
                        <title> GET </title>
                    <head> 
                    <body>
                        <h1> Sequence number {decoded_number} </h1>
                        <p> {string} </p>
                    <a href="http://127.0.0.1:8080/">[Main page]</a>
                    </body>
                    </html>
                    """
    return contents


def genes(message):
    decoded_gene = msg(message, "/gene?get=", 2)
    string = gene(decoded_gene)

    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset= "utf-8">
                        <title> GENE</title>
                    <head> 
                    <body>
                        <h1> GENE: {decoded_gene} </h1>
                        <textarea readonly id="GENE" rows="10" cols="70">{string} </textarea>
<br><br>
                    <a href="http://127.0.0.1:8080/">[Main page]</a>
                    </body>
                    </html>
                    """
    return contents


def info(sequence):
    dictionarycount = sequence.count
    length = sequence.len()
    list0 = f"Total length:{length}<br><br>"
    for key in dictionarycount:
        average = (int(dictionarycount[key]) / length) * 100
        potato = f"{key}: {dictionarycount[key]} ({round(average, 1)}%)\n"
        list0 = list0 + potato + f"<br><br>"
    return list0


def what_to_do(message):
    firstpart = msg(message, "writing?sequence=", 2)
    sequence = msg(firstpart, "&operation=", 0)
    grapes = msg(message, "&operation=", 2)
    avocado = Seq(sequence)
    if "rev" in grapes:
        reverse = avocado.reverse
        return str(reverse)
    elif "comp" in grapes:
        complement = avocado.complement
        return str(complement)
    elif "info" in grapes:
        information = info(avocado)
        return information


def operation(message):
    firstpart = msg(message, "writing?sequence=", 2)
    sequence = msg(firstpart, "&operation=", 0)
    blueberry = msg(firstpart, "&operation=", 2)
    contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset= "utf-8">
                            <title> OPERATION </title>
                        <head> 
                        <body>
                            <h2> Sequence: </h2>
                            <p> {sequence} </p>
                        <h2>Operation:</h2>
                            <p> {blueberry} </p>
                        <h2> Result: </h2>
                        <p> {what_to_do(message)} </p>
<br><br>
                        <a href="http://127.0.0.1:8080/">[Main page]</a>
                        </body>
                        </html>
                        """
    return contents


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        print(self.path)

        # Open the form1.html file
        # Read the index from the file

        if self.path == "/":
            contents = Path('form-4.html').read_text()
        elif "/ping" in self.path:
            contents = ping()
        elif "/get?get=" in self.path:
            contents = getting(self.path)
        elif "/gene?get=" in self.path:
            contents = genes(self.path)
        elif "writing?sequence=" in self.path:
            contents = operation(self.path)
        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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
