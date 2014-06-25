#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
from sshsparser import FileParser

PORT_NUMBER = 8000
DOC_ROOT = '/usr/local/web'

# This class handles incoming HTTP requests 
class myHandler(BaseHTTPRequestHandler):

  # a method for handling 404s to the main class
	def handle404(self):
		self.send_error(404,'File Not Found: %s' % self.path)

	
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
			if self.path.endswith(".jpg"):
				mimetype='image/jpeg'
				sendReply = True

			if sendReply: # == True:
				# Open the static file requested and serve it to client
				#f = open(curdir + sep + self.path) # the version using current directory
				# Serve files from document root directory
				f = open( DOC_ROOT + sep + self.path)

				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()

				# translate paragraphs into chinese
				fileparser = FileParser()
				output= fileparser.translateParagraphs(f)

				# encode in unicode if applicable
				try:
				    output=output.encode('utf-8')
				except UnicodeDecodeError:
					  pass

				self.wfile.write(output)

				f.close()
			else:
				# requested file has unknown extension so return error
				pass
			return

		except IOError:
			#self.send_error(404,'File Not Found: %s' % self.path) # version using inline
			self.handle404()
	


try:
	# Create a web server running on localhost and define the handler to manage the request
	server = HTTPServer(('localhost', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	# Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print 'ctrl-C received, shutting down the web server'
	server.socket.close()
	
