import socket

def start_client():
    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 8000))

    try:
        while True:
            # Take input from the user
            data = input("Enter a number to compute its factorial (or -1 to exit): ")
            if not data.isdigit() and data != "-1":
                print("Invalid input. Please enter an integer.")
                continue

            number = int(data)
            if number == -1:
                print("Exiting the client.")
                break

            # Send the number to the server
            client.send(data.encode('utf-8'))

            # Receive the response from the server
            response = client.recv(1024).decode('utf-8')
            print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
