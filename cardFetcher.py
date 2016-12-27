import requests
from bs4 import BeautifulSoup
import socket
import sys
import json


#HOST = ''
#PORT = 8888

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print 'Socket created'

#try:
#    s.bind((HOST, PORT))
#except socket.error as msg:
#    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
#    sys.exit()
#     
#print 'Socket bind complete'##



from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        print 'Recieved A POST!'
        self._set_headers()
        print self.rfile.read(int(self.headers.getheader('Content-Length')))
        self.wfile.write(self.rfile.read(int(self.headers.getheader('Content-Length'))))
	self.send_response(200)


def parseCardData():
    with open('AllCards.json') as data_file:
    	data = json.load(data_file)
    print data        

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        parseCardData()
        run()


parsedCardName = ''
cardImg = ''
cardOracle = ''

def parseCardNamee(card):
	url = "+".join( card.split() )
	return url
    

cardName = raw_input("Which Card do you want the image for? ")

parsedCardName = parseCardName(cardName)



r = requests.get("http://magiccards.info/query?q=%21" + parsedCardName)
parsed = BeautifulSoup(r.text,'html.parser')

for image in parsed.find_all('img', {'height':445}):
	cardImg = image['src']
for name in parsed.find_all('p', {'class':'ctext'}):
	cardOracle = name.string


print cardImg
print '\n'
print cardOracle
