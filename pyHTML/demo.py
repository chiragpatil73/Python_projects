import http.server
import socketserver
import os

# Define the port you want to run the server on
PORT = 8005

# Change to the directory containing your HTML file
DIRECTORY = "E:\project of python\pyHTML\demo.html"

# Define the handler to serve HTML files
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    # Start the server
    httpd.serve_forever()
