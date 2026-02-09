import socket  # Provides low-level networking (TCP/UDP)

# Target server details
target_host = "www.google.com"
target_port = 80  # HTTP runs on port 80

# Create a TCP socket (IPv4 + TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote server
client.connect((target_host, target_port))

# Build a raw HTTP GET request
# \r\n = CRLF (required by HTTP protocol)
# Empty line (\r\n\r\n) ends headers
request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

# Send request (must be bytes, not string)
client.send(request.encode())

# Buffer to store full response
response = b""

# Receive data in chunks until server closes connection
while True:
    chunk = client.recv(4096)  # Read up to 4096 bytes
    if not chunk:              # No more data → connection closed
        break
    response += chunk          # Append chunk to response buffer

# Close the socket (important!)
client.close()

# Convert raw bytes into readable text
decoded_response = response.decode(errors="ignore")

# Save response line-by-line to a file
with open("output.txt", "w", encoding="utf-8") as f:
    for line in decoded_response.splitlines():
        f.write(line + "\n")

print("Response saved to output.txt")
