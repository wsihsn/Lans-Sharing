import http.server
import socketserver
import socket
import os

class SimpleFileServer(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == '/':
                self.path = '/index.html'  # Default file to serve
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        except Exception as e:
            print("An error occurred:", e)
            self.send_error(500, "Internal Server Error")

# Directory se serve karna hai jahan aapke files hain
directory_to_serve = os.getcwd()  # Yeh current directory ko serve karega, aap isse change kar sakte hain

os.chdir(directory_to_serve)

# IP Address paata kare
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

PORT = 8000

Handler = SimpleFileServer
httpd = socketserver.TCPServer(("", PORT), Handler)

print("File server has started IP address", IPAddr, "par port", PORT, "pe")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer band kar diya gaya hai")
    httpd.server_close()
except Exception as e:
    print("An unexpected error occurred:", e)
    httpd.server_close()
