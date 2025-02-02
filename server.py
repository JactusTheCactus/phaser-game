import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Set the directory where your files are located (use the current directory by default)

# Set the port for the server (default is 8000)
PORT = 8000

def readme(port):
    markdown = f"""# __[Link](http://localhost:{PORT})__"""
    with open('README.md','w') as file:
        file.write(markdown)

# Create a TCP server with the SimpleHTTPRequestHandler to serve files
with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving files from {os.getcwd()} at http://localhost:{PORT}")
    readme(PORT)
    httpd.serve_forever()