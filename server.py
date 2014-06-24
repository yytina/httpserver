#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8000
DOC_ROOT = '/usr/local/web'

# This class handles incoming HTTP requests 
class myHandler(BaseHTTPRequestHandler):
	
	# Handler for GET requests
	def do_GET(self):

		# if client did not specify a file name, default to serving index.html
		if self.path=="/":
			self.path="/index.html"
		try:
			# Check the file extension and set proper MIME type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply: # == True:
				# Open the static file requested and serve it to client
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			else:
				# requested file has unknown extension so return error
				pass
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	# Create a web server running on localhost and define the handler to manage the request
	server = HTTPServer(('localhost', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	# Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print 'ctrl-C received, shutting down the web server'
	server.socket.close()
	
