import http.client

# Function to send a GET request
def send_get_request():
    # Create an HTTP connection to the server
    conn = http.client.HTTPConnection("localhost", 8000)
    
    # Send a GET request
    conn.request("GET", "/")
    
    # Get the server's response
    response = conn.getresponse()
    
    # Print the response status and reason
    print(f"GET Status: {response.status}")
    print(f"GET Reason: {response.reason}")
    
    # Read and print the response body
    data = response.read()
    print(f"GET Response: {data.decode()}")
    
    # Close the connection
    conn.close()

# Function to send a POST request
def send_post_request():
    # Create an HTTP connection to the server
    conn = http.client.HTTPConnection("localhost", 8000)
    
    # Set the headers for the request
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    
    # Define the body of the request
    body = "name=John&age=30"
    
    # Send a POST request with the body and headers
    conn.request("POST", "/", body, headers)
    
    # Get the server's response
    response = conn.getresponse()
    
    # Print the response status and reason
    print(f"POST Status: {response.status}")
    print(f"POST Reason: {response.reason}")
    
    # Read and print the response body
    data = response.read()
    print(f"POST Response: {data.decode()}")
    
    # Close the connection
    conn.close()

# Function to send a PUT request
def send_put_request():
    # Create an HTTP connection to the server
    conn = http.client.HTTPConnection("localhost", 8000)
    
    # Set the headers for the request
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    
    # Define the body of the request
    body = "name=Jane&age=25"
    
    # Send a PUT request with the body and headers
    conn.request("PUT", "/", body, headers)
    
    # Get the server's response
    response = conn.getresponse()
    
    # Print the response status and reason
    print(f"PUT Status: {response.status}")
    print(f"PUT Reason: {response.reason}")
    
    # Read and print the response body
    data = response.read()
    print(f"PUT Response: {data.decode()}")
    
    # Close the connection
    conn.close()

# Function to send a HEAD request
def send_head_request():
    # Create an HTTP connection to the server
    conn = http.client.HTTPConnection("localhost", 8000)
    
    # Send a HEAD request
    conn.request("HEAD", "/")
    
    # Get the server's response
    response = conn.getresponse()
    
    # Print the response status and reason
    print(f"HEAD Status: {response.status}")
    print(f"HEAD Reason: {response.reason}")
    
    # Note: HEAD responses do not contain a body
    # Close the connection
    conn.close()

# Entry point of the script
if __name__ == "__main__":
    
    # Send a GET request
    send_get_request()
    
    # Send a POST request
    send_post_request()
    
    # Send a PUT request
    send_put_request()
    
    # Send a HEAD request
    send_head_request()