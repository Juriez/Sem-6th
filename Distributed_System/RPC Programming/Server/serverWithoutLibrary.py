import socket
import threading

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to handle client requests
def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Parse the input number
            number = int(data)
            
            if number < 0:
                response = "Error: Factorial is not defined for negative numbers."
            else:
                result = factorial(number)
                response = f"The factorial of {number} is: {result}"
            
            # Send the result back to the client
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        client_socket.send(f"Error: {str(e)}".encode('utf-8'))
    finally:
        client_socket.close()

# Main server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8000))
    server.listen(5)  # Listen for up to 5 connections
    print("Server is running on port 8000...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
