import requests
import sys
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


##############################################################
# 
#  Declare Global Variables Below
#
##############################################################
all_cards = None



##############################################################
#
# Class Definitions Below
#
##############################################################

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
        print('Recieved A POST!')
        self._set_headers()
        #print self.rfile.read(int(self.headers.getheader('Content-Length')))
        #self.wfile.write(self.rfile.read(int(self.headers.getheader('Content-Length'))))
	#self.send_response(200,all_cards)
        self.wfile.write(all_cards)

def parseCardData():
    with open('AllCards.json') as data_file:
    	data = json.load(data_file)
    return data        

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port ' + str(port) + ' ...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        all_cards = parseCardData()
        run()
