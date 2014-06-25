
sshs
====

Super Simple HTTP Server

Basic Python server that implements the HTTP GET method

== Instruction ==
To start the server, run 'python server.py' and open up [http://localhost:8000](http://localhost:8000) in your browser.
To access the files, after 'http://localhost:8000' type '/' and the file name. The directory for files to be served is currently '/usr/local/web'.

== Note == 
The server translate paragraphs into Chinese (text wrapped in <p> tags).
The server supports html, css, jpg files.

== Known Issues ==
Language encoding problem: Please include following code in the top of html files
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
