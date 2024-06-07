from http.server import BaseHTTPRequestHandler, HTTPServer

# Define a custom HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        # Send an HTTP 200 OK response
        self.send_response(200)
        
        # Set the response headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Prepare and send the response body
        response = "This is a GET request."
        self.wfile.write(response.encode())
        
        # Print a message indicating that a GET request was handled
        print("Handled GET request")

    # Handle POST requests
    def do_POST(self):
        # Get the length of the data sent in the request
        content_length = int(self.headers['Content-Length'])
        
        # Read the data sent in the request body
        post_data = self.rfile.read(content_length)
        
        # Print the received data
        print(f"Received POST: {post_data.decode()}")
        
        # Send an HTTP 200 OK response
        self.send_response(200)
        
        # Set the response headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Prepare and send the response body
        response = "Data received"
        self.wfile.write(response.encode())

    # Handle PUT requests
    def do_PUT(self):
        # Get the length of the data sent in the request
        content_length = int(self.headers['Content-Length'])
        
        # Read the data sent in the request body
        put_data = self.rfile.read(content_length)
        
        # Print the received data
        print(f"Received PUT: {put_data.decode()}")
        
        # Send an HTTP 200 OK response
        self.send_response(200)
        
        # Set the response headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Prepare and send the response body
        response = "Data received and updated"
        self.wfile.write(response.encode())

    # Handle HEAD requests
    def do_HEAD(self):
        # Send an HTTP 200 OK response
        self.send_response(200)
        
        # Set the response headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Print a message indicating that a HEAD request was handled
        print("Handled HEAD request")

# Function to run the HTTP server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    # Define the server address and port
    server_address = ('', port)
    
    # Create an instance of the server
    httpd = server_class(server_address, handler_class)
    
    # Print a message indicating that the server is starting
    print(f"Starting httpd server on port {port}")
    
    # Start the server to handle requests indefinitely
    httpd.serve_forever()

# Entry point of the script
if __name__ == "__main__":
    # Run the server
    run()